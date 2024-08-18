
class Calculadora():

    def soma(self, numero1, numero2):
        return numero1 + numero2
    
    def subtracao(self, numero1, numero2):
        return numero1-numero2

    def multiplicacao(self,numero1,numero2):
        return numero1*numero2
    
    def divisao(self,numero1,numero2):
        if numero2 == 0:
            return "Erro de divisão por zero"
        else:
            return numero1 / numero2

def Menu(titulo,menu):
    print(f' {titulo.center(30,"=")} ')
    for data in range(len(menu)):
        print(f'{data+1} - {menu[data]}')
    print("="*30)

def validaEntrada(opc):
    while True:
        try:
            opc = int(input('Escolha uma opção: '))
        except  ValueError:
            print("Opção inválida, insira uma opção válida!")
            continue
        else:
            return opc

def entrada(opc,calculator):

    v1 = int(input("Escreva o primeiro valor: "))
    v2 = int(input("Escreva o segundo valor: "))
    resultado = None

    if opc == 1:
        resultado = calculator.soma(v1,v2)
    elif opc == 2:
        resultado = calculator.subtracao(v1,v2)
    elif opc == 3:
        resultado = calculator.multiplicacao(v1,v2)
    elif opc == 4:
        resultado = calculator.divisao(v1,v2)
    
    print(f'O resultado é {resultado}')

