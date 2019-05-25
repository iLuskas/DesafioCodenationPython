import requests
import json
import hashlib

myToken = 'd8a3d091920759cbf510ccc3a3bf4de089c2408c'
url_request = 'https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token='
url_responde = 'https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token='
alpha = 'abcdefghijklmnopqrstuvwxyz'
decifrado ='the greatest performance improvement of all is when a system goes from not-working to working. john ousterhout'

def request(url, token):
    try:
        request = requests.get(url+token)
        dictionaryJson = json.loads(request.text)
        return dictionaryJson
    except Exception as e:
        return print("Erro ao requisitar a API: {0}".format(e))


def response(url, token):
    try:
        filename = "C:/Users/Lucaum-PC/PycharmProjects/EnviarEmail/answer.json"
        file = {'answer': ('answer.json', open(filename, 'rb'))}
        request = requests.post(url + token, files=file)
        dictionaryJson = json.loads(request.text)
        return dictionaryJson
    except Exception as e:
        print("Erro ao requisitar a API: {0}".format(e))
        return None


def printRequest(json):
   return 'Numero de casas: {0}\n' \
          'Token: {1}\n'\
          'Cifrado: {2}\n' \
          'Decifrado:{3}\n' \
          'Resumo criptografico: {4}'\
          .format(json['numero_casas'],
                  json['token'],
                  json['cifrado'],
                  json['decifrado'],
                  json['resumo_criptografico'])

def decrypt(text, chave):
    text_decrypt = ''
    for caractere in text:
        if caractere in alpha:
            caractere_index = alpha.index(caractere)
            text_decrypt += alpha[(caractere_index - chave) % len(alpha)]
        else:
            text_decrypt += caractere
    return text_decrypt

def encrypt(text, chave):
    text_decrypt = ''
    for caractere in text:
        if caractere in alpha:
            caractere_index = alpha.index(caractere)
            text_decrypt += alpha[(caractere_index + chave) % len(alpha)]
        else:
            text_decrypt += caractere
    return text_decrypt

def main():
    formatjson = request(url_request, myToken)
    request_cifrado = decrypt(formatjson['cifrado'], formatjson['numero_casas'])
    summary_response = hashlib.sha1()
    summary_response.update(request_cifrado.encode('utf-8'))

    response_api = response(url_responde, myToken)

    print('-----REQUEST----')
    print(summary_response.hexdigest())
    print(request_cifrado)
    print('-----RESPONSE----')
    print(response_api)
   print(response_api.status_code)



if __name__ == "__main__":
    main()
