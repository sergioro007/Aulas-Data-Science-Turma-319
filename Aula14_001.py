#===================== IMPORTAR ==================
#importar o  sqlalchemy
import sqlalchemy

#Criar o motor de conexão
from sqlalchemy import create_engine
engine = create_engine('mysql+pymysql://root:@localhost:3306/loja319')

#declaração do banco de dados - base para a super classe
from  sqlalchemy.ext.declarative import declarative_base

#elementos da tabela
from sqlalchemy import Column, String, Integer

# Criar um sessão - Consulta e modificação
from sqlalchemy.orm import sessionmaker

# ================== CLASSE =======================
#Super classe
Base_dados = declarative_base()

#Super classe Sessão  - Consultar(SELECT) e Alterar os Dados (INSERT, UPDATE E DELETE)
Sessao  = sessionmaker(bind=engine)
Sessao = Sessao()

#Entidade
class Loja319(Base_dados):
   #criação da tabela
    __tablename__ = "usuario"

   #criar os campos
    nome_usuario= Column(String, primary_key=True)
    endereco_usuario = Column(String, nullable=False)
    idade_usuario = Column(Integer, nullable=False)

    #Exibir os dados
    def __repr__(self):
        return f'| NOME: {self.nome_usuario}, IDADE: {self.idade_usuario}\n'


#================== OBJETOS ========================

#sql

# #INSERT
# banco_insert = Loja319(nome_usuario = "João Almeida", endereco_usuario="Rua D", idade_usuario= 25)
# Sessao.add(banco_insert)
# Sessao.commit()

#SELECT
banco = Sessao.query(Loja319).all()
print(banco)

#UPDATE
Sessao.query(Loja319).filter(Loja319.nome_usuario == "Joana").update({"idade_usuario":30})
Sessao.commit()

#DELETE
Sessao.query(Loja319).filter(Loja319.nome_usuario == "Joana").delete()
Sessao.commit()

Sessao.close()
