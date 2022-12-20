def noReturnedMinCoins(listCoins):

    sumAux=0
    totalReturned=0
    indexStop=0
    listCoins.sort()
    validateExistsOne=False

    for i in range(len(listCoins)):
        if((i+1)<len(listCoins)):

            if(listCoins[i]==1):
                validateExistsOne=True
            
            if((listCoins[i]*2)<listCoins[i+1]):
                for j in range(i+1):
                    sumAux=sumAux+listCoins[j]
                    
                
                if ((sumAux+1)!=listCoins[i+1]):
                    
                    indexStop=i+1
                    
                    break
        
    for i in range(indexStop):
        totalReturned=totalReturned+listCoins[i]
    
    totalReturned=totalReturned+1
    if(validateExistsOne==False):
        totalReturned=1
    else:
        if(totalReturned==1):
            for i in range(len(listCoins)):
                totalReturned=totalReturned+listCoins[i]


    print(totalReturned)



noReturnedMinCoins([1,5,1,1,1,10,15,20,100])
noReturnedMinCoins([1,1,1,1,1])
noReturnedMinCoins([5,7,1,1,2,3,22])
noReturnedMinCoins([1,2,4,8,17])
noReturnedMinCoins([2,2,2])