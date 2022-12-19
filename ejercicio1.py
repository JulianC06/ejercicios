#Lista con el resultado
newList=list()

#función para eliminar los números según sea el limite que se ingrese por parámetro
def deleteNumbersInLimit(listNumbers,limitS):

    listNumbers=orderReverse(listNumbers)
    
    #solo se agrega el número una vez. Ej. para limit 6, el número 596 entraría dos veces, entonces con esta variable
    #se limita a que entre una sola vez.
    #también esta variable revisa que si no hay un digito mayor al limit, entonces no es necesario dividir el número
    #por ejemplo, para limit 6, el número 301, no debería agregarse como [3,0,1] sino como [301]
    isDivisble=False

    #recorrer la lista general
    for number in listNumbers:
        #recorrer número por número (1980 -> 1,9,8,0)
        for numberStr in str(number):
            if((int(numberStr)>=limitS) and (not isDivisble)):
                isDivisble=True
                divisibleNumber(number,limitS)
                #newList.append(int(numberStr))
        
        if(not isDivisble):
            newList.append(number)
        else:
            isDivisble=False
    print(newList)


#función que se encarga de agregar digito por digito a la lista de resultado en dado caso que exista un digito mayor al limit
def divisibleNumber(number, limitS):
    for numberStr in str(number):
        if(int(numberStr)<limitS):
            newList.append(int(numberStr))

def orderReverse(listNumbers):
    reverseLIst=list()
   
    for i in range(len(listNumbers)+1):
        if(i!=0):
            reverseLIst.append(listNumbers[-i])
    return reverseLIst

deleteNumbersInLimit([60, 6, 5, 4, 3, 2, 7, 7, 29, 1],2)
#array1=[1,2,3,4]

#array1.reverse()
#print(orderReverse(array1))