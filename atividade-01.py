#Calculadora
def operacao(n1, n2, op):
    if(op == 1):
        print(f"{n1} + {n2} = {n1+n2}")
    elif(op == 2):
        print(f"{n1} - {n2} = {n1-n2}")
    elif(op == 3):
        print(f"{n1} * {n2} = {n1*n2}")
    elif(op == 4):
        print(f"{n1} / {n2} = {n1/n2}")        
    else:
        print("Erro no operador!")    

def entrada():
    x1 = int(input("Digite um número: "))
    x2 = int(input("Digite outro número: "))

    op = int(input("1-Soma; 2-Subtração; 3-Multiplicação; 4-Divisão ->"))

    print("------------------------------")
    operacao(x1, x2, op)
    print("------------------------------")

def main():
    rep = "s"

    while(rep.lower() != "n"):
        entrada()
        rep = input("Deseja fazer outra conta? (s/ n): ")

main()