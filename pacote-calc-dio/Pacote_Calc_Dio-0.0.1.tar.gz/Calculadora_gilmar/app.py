def Calculadora(calculo, num1, num2): 
    if calculo != "soma" and calculo!= "subtração" and calculo!= "multiplicação" and calculo!= "divisão" and calculo!= "media":
        print("Favor informar uma operação válida")
    else:
        x = num1
        y = num2

    if calculo == 'soma':
        resultado = x+y
        return(resultado)
                
    elif calculo == 'subtração':
        resultado = x-y
        return(resultado)

    elif calculo == 'multiplicação':
        resultado = x*y
        return(resultado)

    elif calculo == 'divisão':
        resultado = x/y
        return(resultado)
                
    elif calculo == 'media':
        resultado = (x+y)/2
        return(resultado)
