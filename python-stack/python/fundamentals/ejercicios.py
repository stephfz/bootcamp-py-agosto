
n = 5
m = 6

#n, m = 5,6

def imprime_matriz(num_filas, num_cols):
    for i in range( 0, num_filas - 1):
        print ("*" * num_cols)


#imprime_matriz(n,m)        




def numeros_primos(inicio, fin):
    contador = inicio
    num_primos = 0
    #contar desde n a m
    while (contador <= fin): #desde inicio a fin
        divisibles = 0
        i = 1
        while (i <= contador): 
            if (contador % i == 0):
                divisibles +=1
            i+=1
        if divisibles == 2:
            num_primos +=1
        contador += 1   
    print("Entre {} y {} hay {} numeros primos".format(inicio, fin, num_primos))             

numeros_primos(1,20)
