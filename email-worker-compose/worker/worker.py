import redis
import json
import os
from time import sleep
from random import randint

if __name__ == '__main__':
    redis_host = os.getenv('REDIS_HOST', 'queue')
    r = redis.Redis(host=redis_host, port=6379, db=0)
    print('Aguardando mensaggens...')
    while True:
        mensagem = json.loads(r.blpop('sender')[1])
        #simulando envio de e-mail...abs
        print ('Mandando a mensagem', mensagem['assunto'])
        sleep(randint(8, 25))
        print('Mensagem', mensagem['assunto'], 'enviada')