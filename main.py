import os
from dotenv import load_dotenv

load_dotenv()

senha1 = os.getenv("SENHA")
senha = input("digite sua senha: ")
if senha1 == senha:
    print ("acesso liberado!")

else:
    print("acesso negado!")

print("ola andre")
print("Ola murillo")
print('teste')
print ("teste 2")
print ("teste secundaria")
print("mandando o codigo via merge")