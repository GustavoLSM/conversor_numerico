'''
    Ideia é fazer com o conhecimento atual um conversor de decimais para binário ou hexadecimal e ao contrário também
'''
import os

while True: #para o programa ser infinito
    pergunta = input('Qual conversão deseja fazer?\n'\
                    'decimal para binário [A]\n' \
                    'decimal para hexadecimal [B]\n' \
                    'binário para decimal [C]\n' \
                    'binário para hexadecimal [D]\n' \
                    'hexadecimal para binário [E]\n' \
                    'hexadecimal para decimal [F]\n' \
                    'Digite apenas a letra da opção: ').upper()
    if pergunta == 'A':
        while True:
            decimal = input('Digite um número decimal positivo: ')
            binario = ''
            try:
                decimal_int = int(decimal)
                while decimal_int > 0:
                    binario += str(decimal_int % 2)
                    decimal_int = decimal_int // 2
            except:
                print('Digite apenas números inteiro')
                continue
            os.system('cls')  
            print(f'O número {decimal} em binário fica = {binario[::-1]}')
            # print(bin(int(decimal))) # Para verificar a 
            break
    elif pergunta == 'B':
        while True:
            decimal = input('Digite um número decimal positivo: ')
            hexadecimal = ''
            expoente = 0
            try:
                decimal_int = int(decimal)
            except:
                print('Digite apenas números inteiro')
            divisor = int(decimal)
            while (divisor // 16) > 0:
                divisor = divisor // 16
                expoente += 1
        
            while expoente >= 0:
                hexa = decimal_int // (16**expoente)
                if hexa > 9:
                    if hexa == 10:
                        hexadecimal += 'A'
                    elif hexa == 11:
                        hexadecimal += 'B'
                    elif hexa == 12:
                        hexadecimal += 'C'
                    elif hexa == 13:
                        hexadecimal += 'D'
                    elif hexa == 14:
                        hexadecimal += 'E'
                    else:
                        hexadecimal += 'F'
                else:
                    hexadecimal += str(hexa)
                decimal_int = decimal_int - (hexa*(16**expoente))
                expoente -= 1
            os.system('cls')
            print(f'O número {decimal} em hexadecimal fica = {hexadecimal:>04}')
            # print(hex(int(decimal))) # Para verificar a resposta.
            break
    elif pergunta == 'C':
        while True:
            binario = input('Digite um número em binário: ')
            decimal = 0
            expoente = len(binario) - 1
            for i in binario:
                if i == '0' or i == '1':
                    i = int(i)
                    decimal += i*(2**expoente)
                    expoente -= 1  
                    falha = None
                else:
                    falha = True
                    print('Por favor digite um número binário.')
                    break
            if falha == None:
                os.system('cls')
                print(f'O número binário {binario} em decimal fica = {decimal}')
                # print(bin(decimal)) # Para verificar a resposta.
                break
    elif pergunta == 'D':
        while True:
            binario = input('Digite um número em binário: ')
            decimal = 0
            expoente = len(binario) - 1
            for i in binario:
                if i == '0' or i == '1':
                    i = int(i)
                    decimal += i*(2**expoente)
                    expoente -= 1  
                    falha = None
                else:
                    falha = True
                    print('Por favor digite um número binário.')
                    break
            if falha == None:
                while True:
                    hexadecimal = ''
                    expoente = 0
                    decimal_int = decimal
                    divisor = int(decimal)
                    while (divisor // 16) > 0:
                        divisor = divisor // 16
                        expoente += 1
                
                    while expoente >= 0:
                        hexa = decimal_int // (16**expoente)
                        if hexa > 9:
                            if hexa == 10:
                                hexadecimal += 'A'
                            elif hexa == 11:
                                hexadecimal += 'B'
                            elif hexa == 12:
                                hexadecimal += 'C'
                            elif hexa == 13:
                                hexadecimal += 'D'
                            elif hexa == 14:
                                hexadecimal += 'E'
                            else:
                                hexadecimal += 'F'
                        else:
                            hexadecimal += str(hexa)
                        decimal_int = decimal_int - (hexa*(16**expoente))
                        expoente -= 1
                    os.system('cls')
                    print(f'O número {binario} em hexadecimal fica = {hexadecimal:>04}')
                    # print(f'O número binário {binario} em decimal fica = {decimal}') # Para verificar a resposta.
                    # print(bin(decimal)) # Para verificar a resposta.
                    # print(hex(int(decimal))) # Para verificar a resposta.
                    break
                break
    elif pergunta == 'E':
        while True:
            hexadecimal = input('Digite um número hexadecimal: ').upper()
            decimal = 0
            expoente = len(hexadecimal) - 1
            for c in hexadecimal:
                falha = None
                try:
                    hexadecimal_int = int(c)
                except:
                    if c == 'A':
                        hexadecimal_int = 10
                    elif c == 'B':
                        hexadecimal_int = 11
                    elif c == 'C':
                        hexadecimal_int = 12
                    elif c == 'D':
                        hexadecimal_int = 13
                    elif c == 'E':
                        hexadecimal_int = 14
                    elif c == 'F':
                        hexadecimal_int = 15
                    else:
                        falha = True
                        print('Por favor digite um número hexadecimal válido.')
                        break
                decimal += hexadecimal_int*(16**expoente)
                expoente -= 1
            if falha == None:
                binario = ''
                decimal_int = decimal
                while decimal_int > 0:
                    binario += str(decimal_int % 2)
                    decimal_int = decimal_int // 2
                # os.system('cls')  
                print(f'O número hexadecimal {hexadecimal:>04} em binário fica = {binario[::-1]}')
                # print(f'O número {decimal} em binário fica = {binario[::-1]}')
                # print(bin(int(decimal))) # Para verificar a resposta.
                # print(f'O número hexadecimal {hexadecimal:>04} em decimal fica = {decimal}')
                # print(hex(decimal)) # Para verificar a resposta.
                break
    elif pergunta == 'F':
        while True:
            hexadecimal = input('Digite um número hexadecimal: ').upper()
            decimal = 0
            expoente = len(hexadecimal) - 1
            for c in hexadecimal:
                falha = None
                try:
                    hexadecimal_int = int(c)
                except:
                    if c == 'A':
                        hexadecimal_int = 10
                    elif c == 'B':
                        hexadecimal_int = 11
                    elif c == 'C':
                        hexadecimal_int = 12
                    elif c == 'D':
                        hexadecimal_int = 13
                    elif c == 'E':
                        hexadecimal_int = 14
                    elif c == 'F':
                        hexadecimal_int = 15
                    else:
                        falha = True
                        print('Por favor digite um número hexadecimal válido.')
                        break
                decimal += hexadecimal_int*(16**expoente)
                expoente -= 1
            if falha == None:
                os.system('cls')
                print(f'O número hexadecimal {hexadecimal:>04} em decimal fica = {decimal}')
                # print(hex(decimal)) # Para verificar a resposta.
                break
    else:
        print('Digite apenas a letra da opção')
        continue
    continuar = ''
    while True:
        continuar = input('Deseja fazer mais conversões?\n[S]im [N]ão: ').upper()
        if continuar == 'S':
            os.system('cls')
            break
        elif continuar == 'N':
            break
        else:
            print('Responda apenas com [S] ou [N]')
            continue
    if continuar == 'N':
        break
