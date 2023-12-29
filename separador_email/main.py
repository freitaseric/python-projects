email = input("Informe um email para separar: ")

username = email.split('@')[0]
domain = email.split('@')[1]
provider = ''

if username.__contains__('.'):
    username = username.split('.')[0]

if domain == "gmail.com":
    provider = "Google"
elif (domain == "hotmail.com" or domain == "outlook.com" or domain == "outlook.com.br"):
    provider = "Microsoft"
elif domain == "uol.com.br":
    provider = "UOL"
else:
    provider = "Desconhecido"

print(f"Este email pertence à: {username}")
print(f"O provedor do email é: {provider}")
print(f"Com o domínio: {domain}")
