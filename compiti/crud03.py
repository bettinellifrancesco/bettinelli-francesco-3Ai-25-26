import json
NOME_FILE = "./compiti/archivio.txt"
film = []
def stampaMenu():
    print("---------ARCHIVIO-FILM--------")
    print("1. inserisci un nuovo film")
    print("2. modifica il nome di un film")
    print("3. visualizza i film nell'archivio")
    print("4. cancella un film")
    print("0. termina programma")
    print("------------------------------")
    scelta = int(input("Inserisci la tua scelta: "))
    return scelta
def carica():
    try:
        f = open(NOME_FILE, "r")
        s = f.read()
        l = json.loads(s)
        f.close()
        if s == "":
            return []
        return l
    except:
        print("Errore nel caricamento del file")
        return []
def salva(l):
    j = json.dumps(l)
    f = open(NOME_FILE, "w")
    f.write(j)
    f.close()
def aggiungi_film(l):
    corretto = False
    while not corretto:
        nome = input("Inserisci il nome del film da inserire: ").lower()
        if len(nome) < 2:
            print("Ciò che hai inserito è troppo corto o vuoto")
        elif nome in l:
            print("Film già presente")
        else:
            corretto = True
    corretto = False
    while not corretto:
        try:
            anno = int(input("Inserisci l'anno di uscita del film: "))
            if anno<1900 or anno>2026:
                print("Anno non valido")
            else:
                corretto = True
        except:
            print("Formato dell'anno non valido")
    corretto = False
    while not corretto:
        try:
            guadagni = float(input("Inserisci gli incassi al bottrghino del film: "))
            if guadagni<0:
                print("Guadagno non valido")
            else:
                corretto = True
                film.append({
                    "nome": nome,
                    "anno": anno,
                    "guadagni": guadagni
                })
        except:
            print("Formato non valido")
def visualizza_film(l):
    if len(l) == 0:
        print("L'archivio dei film è vuoto")
    else:
        print("--------ARCHIVIO-FILM--------")
        for c,i in enumerate(l):
            print(f"{c+1}. nome: {i["nome"]}, anno di uscita: {i["anno"]}, incassi al botteghino: {i["guadagni"]}€")
def modifica_film(l):
    if len(l) == 0:
        print("Archivio vuoto, nessun film da modificare")
    else:
        visualizza_film(l)
        corretto = False
        while not corretto:
            try:
                modifica = int(input("Inserisci il numero relativo al film: "))
                if modifica > len(l):
                    print("Non puoi inserire un numero maggiore dell'archivio")
                elif modifica < 1:
                    print("Il numero non può essere 0 o minore di esso")
                else:
                    indice = l.index(l[modifica-1])
                    nuovoNome = input("Inserisci il nuovo nome del film: ")
                    if len(nuovoNome) < 2:
                        print("Ciò che hai inserito è troppo corto o vuoto")
                    else:
                        l[indice]["nome"] = nuovoNome
                        corretto = True
            except:
                print("Formato non valido")
def elimina_film(l):
    if len(l) == 0:
        print("Archivio vuoto, nessun film da modificare")
    else:
        visualizza_film(l)
        corretto = False
        while not corretto:
            try:
                elimina = int(input("Inserisci il numero relativo al film che vorresti eliminare: "))
                if elimina > len(l):
                    print("Non puoi inserire un numero maggiore dell'archivio")
                elif elimina < 1:
                    print("Il numero non può essere 0 o minore di esso")
                else:
                    indice = l.index(l[elimina-1])
                    l.pop(indice)
                    corretto = True
            except:
                print("Formato non valido")
film = carica()
esci = False
while not esci:
    scelta = stampaMenu()
    if scelta == 1:
        aggiungi_film(film)
    elif scelta == 2:
        modifica_film(film)
    elif scelta == 3:
        visualizza_film(film)
    elif scelta == 4:
        elimina_film(film)
    elif scelta == 0:
        salva(film)
        print("ARRIVEDERCI!!!")
        esci = True
    else:
        print("Scelta non valida")
 