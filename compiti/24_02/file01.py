#/
#\\
#encoding permette di utilizzare caratteri speciali come la è accentata
f=open('compiti/24_02/peter pan.txt', encoding="utf-8")#se fai punto slash prende l'indirizzo in cui ti trovi se fai punto punto slash torni a quello precedente
righe=f.read()
f.close()
print(righe)
inserisci=''
while inserisci!='n' :
    scelta=input('inserisci la parola che vuoi cercare: ')
    if scelta in righe:
        l=righe.count(scelta)
        print(l)
        inserisci=input('vuoi continuare ad inserire? s/n: ')
        if inserisci!='s' and inserisci!='n':
            print("errore d'inserimento!!")
    else:
        print('nome non presente!!')