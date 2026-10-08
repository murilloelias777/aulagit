import os
from dotenv import load_dotenv

load_dotenv()

senha1 = os.getenv("SENHA")
senha = input("digite sua senha: ")
if senha1 == senha:
    print ("acesso liberado!")

else:
    print("acesso negado!")
