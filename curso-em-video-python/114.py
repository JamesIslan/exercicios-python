# Tratamento de erro incluso
import requests

try:
    requests.get('http://pudim.com.br/')
except requests.ConnectionError:
    print('O site do pudim está indisponível ;(')
else:
    print('O site do pudim está disponível :D')