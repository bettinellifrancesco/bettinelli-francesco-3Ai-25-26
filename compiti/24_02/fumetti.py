NOME_FILE = "fumetti.txt"   #nome del file

#collezionare i manga che leggo di solito (solo il nome fumetto)

#questa funzione si occupa di visualizzare il menù principale
def stampaMenu():
    print(" ------------- I MIEI FUMETTI --------------")
    print("Scegli:")
    print("1 - per inserire un nuovo fumetto")
    print("2 - per visualizzare tutti i fumetti che leggi di solito")
    print("3 - modificare un fumetto")
    print("4 - eliminare un fumetto")
    print("0 - terminare il programma")

#la funzione salva prende la lista dei fumetti e li memorizza su file di testo sequenziale
def salva(l):
    file = open(NOME_FILE, "w")
    for f in l:
        file.write(f + "\n")
    file.close()

#carica la lista dei fumetti da file e la memorizza nella lista
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
        return []   #restituisco una lista vuota, altrimenti restituisce None


#carica la lista dei fumetti da file e la memorizza nella lista
"""
def carica():
    #apro il file
    file = open(NOME_FILE, "r")
    
    risultato = []
    #carico la lista dei fumetti
    s = file.readline()[:-1]
    while s != "":       
        risultato.append(s)[:-1]
        s = file.readline()
    
    #chiudo il file
    file.close()

    #restituisco la lista recuperata da file
    return risultato
"""

#questa funzione si occupa di 
    # - chiede all'utente la sua scelta
    # - controlla che la scelta sia valida
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


def chiediFumetto():
    corretto = False
    while not corretto:
        nome = input("Inserisci il nome del fumetto").strip().lower()
        #TODO: da controllare se il fumetto è gia presente
        if len(nome) == 0:
            print("Nome fumetto non valido")
            corretto = False
        else:
            corretto = True
    return nome

def inserisciFumetto(f):
    nome = chiediFumetto()
    f.append(nome)

def eliminaFumetto(f):
    visualizzaFumetti(f)
    posizione = chiediPosizione(f)
    f.pop(posizione-1)

def chiediPosizione(f):
    corretto = False
    while not corretto:
        try:
            scelta = int(input("Indica il numero del fumetto da modificare "))
            if scelta < 1 or scelta > len(f):
                print("Numero fumetto non valido")
                corretto = False
            else:
                return scelta  
        except:
            print("Formato numero fumetto non valido")
            corretto = False

def modificaFumetto(f):
    visualizzaFumetti(f)
    posizione = chiediPosizione(f)
    nome = chiediFumetto()
    f[posizione-1] = nome

def visualizzaFumetti(f):
    if len(f) == 0:
        print("Nessun fumetto in archivio")
    else:
        for i,f in enumerate(f):
            print(f"{i+1} - {f}")

fumetti = []

#carico i fumetti all'avvio del programma
fumetti = carica()

fine = False
while not fine:
    stampaMenu()
    s = scelta()
    if s == 1:
        n = inserisciFumetto(fumetti)
    elif s == 2:
        visualizzaFumetti(fumetti)
    elif s == 3:
        modificaFumetto(fumetti)
    elif s == 4:
        eliminaFumetto(fumetti)
    elif s == 0:
        #prima di chiudere il programma salvo la lista dei fumetti
        salva(fumetti)
        print("Arrivedorciiiii")
        fine = True
    


