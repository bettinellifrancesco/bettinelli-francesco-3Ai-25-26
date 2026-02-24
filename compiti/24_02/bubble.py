def bubbleSort(listaDaOrdine):
    n=len(listaDaOrdine)
    for i in range(n-1):
        for h in range(n-i-1):
            if listaDaOrdine[h]['cognome']>listaDaOrdine[h+1]['cognome']:
                listaDaOrdine[h],listaDaOrdine[h+1]=listaDaOrdine[h+1],listaDaOrdine[h]


lista=[{'nome':'carlo',
        'cognome':'bettinelli',
        'eta':'23'},
        {'nome':'claudio',
        'cognome':'bianchi',
        'eta':'23'},
        {'nome':'mauro',
        'cognome':'rossi',
        'eta':'23'}]
print(lista)#lista disordinata
bubbleSort(lista)
print(lista)#lista ordinata in maniera decrescente