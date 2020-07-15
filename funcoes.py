from reportlab.pdfgen import canvas
import random
from classe import ContaBasica
import string
from bot import bot
import time

def criar_pdf (pergunta_qt, tipo, chat, gabarito):

  if pergunta_qt == '14':
    qt1 = 2; qt2 = 7
  elif pergunta_qt == '21':
    qt1 = 3; qt2 = 7
  elif pergunta_qt == '28':
    qt1 = 4; qt2 = 7
  elif pergunta_qt == '35':
    qt1 = 5; qt2 = 7
  elif pergunta_qt == '42':
    qt1 = 6; qt2 = 7

  if tipo == 'adição':
    lista, pdf = adicao(qt1, qt2)
  elif tipo == 'subtração':
    lista, pdf = subtracao(qt1, qt2)
  elif tipo == 'multiplicação':
    lista, pdf = multiplicacao(qt1, qt2)
  elif tipo == 'divisão':
    lista, pdf = divisao(qt1, qt2)

  time.sleep(1)
  atribuir(pdf, lista, pergunta_qt)

  ultima = lista[-1].posi_y
  if gabarito == 'sim':
    gabarito_func(pdf, lista, ultima)

  pdf.save()
  print('Pdf gerado!')
  file = 'Exercícios.pdf'
  bot.sendDocument(chat, document=open(file, 'rb'))
  bot.sendMessage(chat, 'Tá na mão!')











#Adição --------------------------------------------------
def adicao (qt1, qt2):
  x = 40
  y = 800
  pdf = canvas.Canvas('Exercícios.pdf')
  lista = []
  for i in range(qt1):
    x = 40
    for u in range(qt2):
      num = ContaBasica(random.randint(100,999),random.randint(100,999),'','','',  x, y)

      num.resultado = num.primeiro + num.segundo
      num.simbolo = '+'

      lista.append(num)

      pdf.drawString(x, y, str(num.primeiro))
      pdf.drawString(x - 8, y - 10, num.simbolo)
      pdf.drawString(x, y -20, str(num.segundo))
      pdf.drawString(x - 13, y - 25, ' ______ ')

      x = x + 80
    y = y -70
  return lista, pdf



#Subtração ----------------------------------------------
def subtracao (qt1, qt2):
  x = 40
  y = 800
  pdf = canvas.Canvas('Exercícios.pdf')
  lista = []
  for i in range(qt1):
    x = 40
    for u in range(qt2):
      num = ContaBasica(random.randint(500,999),random.randint(100,500),'','','',  x, y)

      num.resultado = num.primeiro - num.segundo
      num.simbolo = '-'

      lista.append(num)

      pdf.drawString(x, y, str(num.primeiro))
      pdf.drawString(x - 8, y - 10, num.simbolo)
      pdf.drawString(x, y -20, str(num.segundo))
      pdf.drawString(x - 13, y - 25, ' ______ ')

      x = x + 80
    y = y -70
  return lista, pdf



#Multiplicação -------------------------------------------
def multiplicacao (qt1, qt2):
  x = 40
  y = 800
  pdf = canvas.Canvas('Exercícios.pdf')
  lista = []
  for i in range(qt1):
    x = 40
    for u in range(qt2):
      num = ContaBasica(random.randint(100,999),random.randint(1,99),'','','',  x, y)

      num.resultado = num.primeiro * num.segundo
      num.simbolo = 'x'

      lista.append(num)

      pdf.drawString(x, y, str(num.primeiro))
      pdf.drawString(x - 8, y - 10, num.simbolo)
      pdf.drawString(x + 7, y -20, str(num.segundo))
      pdf.drawString(x - 13, y - 25, ' ______ ')

      x = x + 80
    y = y -70
  return lista, pdf

#Divisão --------------------------------------------
def divisao (qt1, qt2):
  x = 40
  y = 800
  pdf = canvas.Canvas('Exercícios.pdf')
  lista = []
  for i in range(qt1):
    x = 40
    for u in range(qt2):
      num = ContaBasica(random.randrange(100,999,2),random.randrange(10,99,2),'','','',  x, y)

      num.resultado = num.primeiro / num.segundo
      num.resultado = '{:.2f}'.format(num.resultado)
      num.simbolo = '÷'

      lista.append(num)

      pdf.drawString(x, y, str(num.primeiro))
      pdf.drawString(x - 8, y - 10, num.simbolo)
      pdf.drawString(x + 7, y -20, str(num.segundo))
      pdf.drawString(x - 13, y - 25, ' ______ ')

      x = x + 80
    y = y -70
  return lista, pdf


#Atribuir uma letra/número a cada questão ------------------
def atribuir(pdf, lista, pergunta_qt):
  letras = list(string.ascii_lowercase)

  if pergunta_qt == '14' or pergunta_qt == '21':
    for i in range(len(lista)):
      lista[i].letraNumero = letras[i]
  else: 
    for i in range(len(lista)):
      lista[i].letraNumero = str(i+1)
  
  for conta in lista:
    pdf.drawString(conta.posi_x - 25, conta.posi_y, conta.letraNumero + ') ')


#Gabarito ------------------------------------------------
def gabarito_func(pdf, lista, y):
  y = y - 70
  pdf.drawString(15, y, 35*'_' + 'G A B A R I T O' + 35*'_')
  y = y - 50
  x = 20

  for i in range(len(lista)):
    pdf.drawString(x , y, lista[i].letraNumero + ') ' + str(lista[i].resultado))
    x = x + 70
    if i == 7 or i == 15 or i == 23 or i == 31 or i == 39:
      y = y - 40
      x = 20
