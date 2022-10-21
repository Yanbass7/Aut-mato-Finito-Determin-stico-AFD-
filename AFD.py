# -*- coding: utf-8 -*-

estados = input().split(" ")
simbalf = input().split(" ")
qtdtrans = int(input())

afd = {}

for estado in estados:
    afd[estado] = {}

for i in range(0, qtdtrans):
    i, c, f = input().split(" ")
    if c not in afd[i]:
      afd[i][c] = f

estado_inicial = input()
estados_finais = input().split(" ")
palavras = input().split(" ")

for palavra in palavras:
    estado_atual = estado_inicial
    estado_de_erro = 0
    for char in palavra:
        try:
            estado_atual = afd[estado_atual][char]
        except KeyError:
            estado_de_erro = 1
            break
    if(estado_de_erro == 1 or estado_atual not in estados_finais):
        print('N')
    else:
        print('S')
