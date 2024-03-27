import random
         
numeroSecreto = random.randint("1,101")
tentativas = 0
         
         
def jogar():
             
    print("********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("********************************")
             
    NivelDificuldade()
             
    print("numero secreto ", numeroSecreto)
    global tentativas
    while tentativas > 0:
        numeroDigitado = int (
            input("Digite um numero de 1 a 100 para tentar adivinhar o número secreto: "))
        if numeroDigitado == numeroSecreto:
            print("Parabéns o numero escolhido esta correto")
            print("O numero screto era",numeroSecreto)
            break
        else:
            tentativas -= 1
            print("O numero digitado esta correto")
            print(dica(numeroDigitado))
            if tentativas > 0:
                print("Tente novamente, você tem: ", tentativas, "tentativas")
            else: 
                print("Game Over")
                        
                        
                        def dica(numeroEscolhido: int):
                            print("Escolhido", numeroEscolhido, "Secreto", numeroSecreto)
                            if numeroEscolhido > numeroSecreto:
                                return "O numero Escolhido é Maior que o mundo secreto, ", numeroEscolhido
                            else:
                                return "O numero escolhido é menor que o numero secreto", numeroEscolhido
                                
                        
                        def NivelDificuldade():
                            print("Qual nível de dificuldade?")
                            print("(1) Fácil (2) Médio (3) Difícil")
                            dificuldade = int(input("Defina o nível: "))
                            global tentativas
                            if (dificuldade == 1):
                                tentativas = 10
                            elif(dificuldade == 2):
                                tentativas = 8
                            else:
                                tentativas = 6
                                
                        jogar() 