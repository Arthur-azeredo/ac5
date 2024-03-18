import random

def main():
    vida_aventureiro = 100
    ataque_aventureiro = random.randint(10, 20)
    defesa_aventureiro = random.randint(1, 5)

    vida_monstro = random.randint(60, 80)
    ataque_monstro = random.randint(20, 30)

    cont = 0

    while vida_aventureiro > 0 and vida_monstro > 0:
        cont += 1
    
        print(f"vida aventureiro: {vida_aventureiro} -  ataque aventureiro: {ataque_aventureiro} - defesa aventureiro: {defesa_aventureiro}")
        print(f"vida monstro: {vida_monstro} - ataque monstro: {ataque_monstro}")
        print(f"Rodada: {cont}")
        
        vida_monstro = vida_monstro - random.randint(1, ataque_aventureiro)
        if vida_monstro <= 0:
            print("monstro morreu")
            break
        
        dano = random.randint(1, ataque_monstro) - defesa_aventureiro
        vida_aventureiro -= dano
        if vida_aventureiro <= 0:
            print("aventureiro morreu")
            break

main()


        
    


    