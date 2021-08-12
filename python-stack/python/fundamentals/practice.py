# 1. Factorial
# ejemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120

'''
contador = 1
factorial = 1
factorial = factorial x 1

contador = 2
factorial = factorial x 2

contador = n
factorial = factorial x n

'''

'''
numero_ingresado = input("Ingrese un numero: ") 
while (numero_ingresado.isalpha()):
    numero_ingresado = input("Ingrese un numero: ")  
 
factorial = 1
# convertir un str a un int
numero = int(numero_ingresado)
for contador in range(1, numero + 1): #range(inicio, fin) pero itera hasta fin - 1
    factorial = factorial * contador
print(factorial)    

'''


'''
lst = 'h', 'o','l','a'
inverso = ''

inverso.join(lst.pop() -> 'a') -> 'a'
inverso.join(lst.pop() -> 'l') -> 'al'
inverso.join(lst.pop() -> 'o') -> 'alo'
inverso.join(lst.pop() -> 'h') -> 'aloh'
'''


def isPalindrome(aword):
    lst_original = list(aword)
    reversed_lst = []
    for i in range( 0, len(aword)):
        reversed_lst.append(lst_original.pop())
    print (reversed_lst)    
    reversed_word = ''
    reversed_word = reversed_word.join(reversed_lst) 
    print(reversed_word) 
    return (reversed_word == aword) 

wordi = "maremoto"
#print(isPalindrome(wordi) )

def palindromeB(aword):
    reversed_word = aword[::-1]
    print(reversed_word)
    return (reversed_word == aword) 

print(palindromeB(wordi) )    