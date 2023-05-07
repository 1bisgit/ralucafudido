#!/usr/bin/env python
import requests

# Variáveis
user = input("Insira o usuário do Instagram: ")

# Função para denunciar a conta
def denunciar_conta():
    url = 'https://www.instagram.com/' + user
    payload = {'action': 'report_account'}
    r = requests.post(url, data=payload)
    print("Conta denunciada com sucesso!")

# Loop para denunciar a conta várias vezes
for i in range(0, 10):
    denunciar_conta()