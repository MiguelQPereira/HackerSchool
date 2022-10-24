#Slot machine

import time
from random import randrange

class Slot:
    a = [0,0,0]
    r = ['@','@','@']
    
    def spin(self):
        for e in range(0, 3):
            i = randrange(1, 157)
            self.a[e] = i
            if i <51:
                self.r[e] = '@'
            elif i<91:
                self.r[e] = '&'
            elif i<121:
                self.r[e] = '+'
            elif i<141:
                self.r[e] = '%'
            elif i<151:
                self.r[e] = '!'
            elif i<156:
                self.r[e] = 'w'
            elif i<157:
                self.r[e] = '$'
            
        return self.r, self.a
    
    def result (self):
        print(' _______ \n/       \  ')
        i = 0
        for i in range(0, 50):
            self.spin (self)
            print ('\r|',self.r[0], self.r[1], self.r[2], '|', end='')
            time.sleep(0.2)
        print ('\n\_______/')
        
        return self.r

game = Slot

print ('Slot Machine\n\n')
cash = int(input("Depositar créditos: "))

while not (cash>0):
    print("Input inválido. Tenta inserir outro valor")
    cash = int(input("Depositar créditos: "))

print ("Créditos aceites")
        
print('Balanço ',cash,'$')

menu = input('\nEnter para jogar\n \nh para ver as regras ')

while menu != '' and menu != 'h' :
    menu = input('Input inválido. '+'\nEnter para jogar\n \nh para ver as regras')

if menu == 'h':
    print("""
Regras da Slot Machine:

Escolhe quanto vais apostar e ganha se calharem três simbolos iguais

Simbolo 1:  $               x100 000
Simbolo 2:  w                 x1 000
Simbolo 3:  !                   x200
Simbolo 4:  %                    x70
Simbolo 5:  +                    x20
Simbolo 6:  &                    x10
Simbolo 7:  @                     x5

Se ficares sem crédito o jogo acaba.
Joga com moderação""")
sair=0
while cash > 0 and sair==0:
    sair=0
    bet = int(input('Aposta: '))

    while bet<=0 or bet>cash:
        print('Valor inválido.')
        
        bet = int(input('Tenta de novo:'))

    cash = cash - bet
    
    print('Apostado:', bet, '$\nBalanço:', cash, '$')
    
    play = game.result(game)
    
    if (play[0]==play[1]) and (play[1]==play[2]):
        print ('\n!!!VENCEDOR!!!\n')
        
        if game.r[0]=='$':
            bet=bet*100000
        elif game.r[0]=='w':
            bet = bet*1000
        elif game.r[0]=='!':
            bet = bet*200
        elif game.r[0]=='%':
            bet = bet*70
        elif game.r[0]=='+':
            bet = bet*20
        elif game.r[0]=='&':
            bet = bet*10
        elif game.r[0]=='@':
            bet = bet*5
        
        print(cash+bet,'=',cash,'+',bet)
        cash = cash + bet
    else:
        print ('\nTenta Novamente\n')
    
    c = input('Queres continuar [y/n]: ')
    
    while c != 'y' and c != 'n':
        c = input('Input inválido. Queres continuar a jogar[y/n]: ')
    
    if c=='n':
        sair=-1

if cash == 0:
    print('\n\nFicas-te sem créditos, volta mais tarde')

else:
    print('\n\nTerminas-te com', cash,'$')