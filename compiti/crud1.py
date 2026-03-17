NOME_FILE = "fumetti.txt"  
def stampaMenu():
    print(" ------------- I MIEI FUMETTI --------------")
    print("Scegli:")
    print("1 - per inserire un nuovo film")
    print("2 - per modificare un film")
    print("3 - per visualizzare tutti i film")
    print("4 - eliminare un film")
    print("0 - terminare il programma")
def salva(l):
    file = open(NOME_FILE, "w")
    for f in l:
        file.write(f + "\n")
    file.close()
def carica():
    try:
        #apro il file
        file = open(NOME_FILE, "r")
        
        #carico la lista dei fumetti
        righe = file.read()
        righe = righe.split("\n")
        righe.pop(-1)   #rimuovo lo \n finale
        #chiudo il file
        file.close()

        #restituisco la lista recuperata da file
        return righe
    except:
        print("Impossibile caricare il file dei fumetti")
        return [] 
def scelta():
    corretto = False
    while not corretto:
        try:
            scelta = int(input("Scelta >> "))
            if scelta < 0 or scelta > 4:
                print("Scelta non valida")
                corretto = False
            else:
                corretto = True  
                return scelta          
        except:
            print("Formato scelta non valida")
            corretto = False
def chiedi_film(lista):
    film=input('inserisci il nome del film che vuoi salvare: ')
    if len(film)!=0:
        lista.append(film)
        return lista
    else:
        return 'film non valido!!'
def chiediPosizione(lista):
    corretto = False
    while not corretto:
        try:
            scelta = int(input("Indica il numero del fumetto da modificare "))
            if scelta < 1 or scelta > len(lista):
                print("Numero fumetto non valido")
                corretto = False
            else:
                return scelta  
        except:
            print("Formato numero fumetto non valido")
            corretto = False
def modificafilm(lista):
    visualizza(lista)
    posizione = chiediPosizione(lista)
    nome = chiedi_film(lista)
    lista[posizione-1] = nome
def visualizza(lista):
    if len(lista)>0:
        for i,lista in enumerate(lista):
            print(f"{i+1} - {lista}")
    else:
        return 'lista vuota'
def elimina_film(lista):
    visualizza(lista)
    posizione = chiediPosizione(lista)
    lista.pop(posizione-1)
lista=[]
lista = carica()

fine = False
while not fine:
    stampaMenu()
    s = scelta()
    if s == 1:
        n = chiedi_film(lista)
    elif s == 2:
        modificafilm(lista)
    elif s == 3:
        visualizza(lista)
    elif s == 4:
        elimina_film(lista)
    elif s == 0:
        #prima di chiudere il programma salvo la lista dei fumetti
        salva(lista)
        print("Arrivedorciiiii")
        fine = True
    



    
