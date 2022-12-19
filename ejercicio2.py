def squareOfIntegers(array, limitS):
    resultList = list()
    rangeOut = int(str(limitS)+str(limitS))
    
    if (len(array['array']) != 0):
        for number in array['array']:
            square = (number)**2
            if (square <= rangeOut):
                resultList.append(square)
    else:
        print("Error. Array is empty.")

    return sortListAscending(resultList)


def sortListAscending(listSquares):

    for i in range(len(listSquares)-1):
        for j in range(len(listSquares)-1-i):
            if listSquares[j] > listSquares[j+1]:
                listSquares[j], listSquares[j+1] = listSquares[j+1], listSquares[j]

    return listSquares


print(squareOfIntegers({"array": [-10, 10]},6))

