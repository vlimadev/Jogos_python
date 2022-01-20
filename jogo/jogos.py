import jogo_adivinha
import forca


print("**********************************")
print("*Escolha o jogo que deseja jogar!*")
print("**********************************")

print("(1)Forca (2) Adivinhação")

jogo = int(input("Qual jogo deseja jogar?:"))

if(jogo == 1):
    print("Jogando forca")
    forca.jogar()
elif(jogo == 2):
    print("jogando adivinhação")
    jogo_adivinha.jogar()


