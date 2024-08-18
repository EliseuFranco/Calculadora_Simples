from funcoes import util

calculator = util.Calculadora()

while True:
    util.Menu("Calculadora simples",['Soma','Subração','Multiplicação','Divisão','Sair'])
    opc = util.validaEntrada("")
    if opc in [1,2,3,4]:
        util.entrada(opc,calculator)
    elif opc == 5:
        print('<< FIM DO PROGRAMA >>')
        break
    else:
       print("Opção fora do menu!")

