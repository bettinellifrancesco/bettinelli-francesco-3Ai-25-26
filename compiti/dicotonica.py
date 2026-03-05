def ricercaDicotomica(l, n):
   f = len(l)-1
   m = (f)//2
   lista1 =[]
   while True:  
        if l[m] == n:
           return True
        if l[m] > n:
           m -= (f - m + 2) // 2
           if m <= 0:
               m = 0
               return False
        elif l[m] < n:
           m += (f - m + 2) // 2
           if m > f:
               return False
        lista1.append (m)
        if len(lista1) > f:
            return False
lista = [10, 12, 44, 72, 88, 96, 104, 1000]
print(ricercaDicotomica(lista, 1000))