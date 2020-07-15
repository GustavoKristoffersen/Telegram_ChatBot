from funcoes import criar_pdf
from bot import bot
import time

def processar(msg):
  chat_id = msg['chat']['id']
  comando = msg['text'].lower()
  if comando == 'oi' or comando == '/start':
    mensagem = 'Olá, quantas contas você deseja? Veja as opções abaixo:\n14\n21\n28\n35\n42'
    bot.sendMessage(chat_id, mensagem)

  elif comando == '14' or comando == '21' or comando == '28' or comando == '35' or comando == '42':
    global qt_conta
    qt_conta = comando
    mensagem = 'Certo, qual operação? Veja as opções abaixo:\nAdição\nSubtração\nMultiplicação\nDivisão'
    bot.sendMessage(chat_id, mensagem)

  elif comando == 'adição' or comando == 'subtração' or comando == 'multiplicação' or comando == 'divisão':
    global tipo_conta
    tipo_conta = comando
    mensagem = 'Entendido, você quer o gabarino no arquivo?'
    bot.sendMessage(chat_id, mensagem)
  
  elif comando == 'sim' or comando == 'não':
    criar_pdf(qt_conta ,tipo_conta, chat_id, comando)
    
  else:
    bot.sendMessage(chat_id, 'Comando não válido')


bot.message_loop(processar)
while True:
  pass