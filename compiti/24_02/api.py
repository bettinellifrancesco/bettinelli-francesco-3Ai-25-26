import requests
def categorie():
      response = requests.get("https://fakeapi.net/products/categories")
      if response.status_code != 200:
       print("caricamento categoria non andato a buon fine!!")
      else:
         categorie=response.json()
         for i,categoria in enumerate(categorie):
           print(f"{i+1} - {categoria}")
         return categorie
def richiesta_utente(categorie):
      errore=True
      while errore:
         scelta=input("inserisci il nome della categoria che vuoi visualizzare: ")
         if scelta in categorie:
           errore=False
         else:
           print("Scelta non valida. Riprova.")
      return scelta
def Lista_Prodotti(scelta):
         lista_id=[]
         response = requests.get(f"https://fakeapi.net/products/category/{scelta}")
         if response.status_code != 200:
           print("Errore nel recupero dei prodotti della categoria selezionata.")
         else:
            prodotti = response.json()
            for prodotto in prodotti["data"]:
               print(f"ID: {prodotto['id']}, Nome: {prodotto['title']}, Prezzo: {prodotto['price']}")
               lista_id.append(prodotto["id"])  
            return lista_id
def Scelta():
       errore=True
       while errore:
         scelta=input("Vuoi vedere il dettaglio di un prodotto? (s/n): ")
         if scelta.lower() == "s" or scelta.lower() == "n":
           errore=False
         else:
           print("Scelta non valida. Riprova.")
         return scelta
def scelta_id(lista_id):
      errore=True
      while errore:
         try:
            id_scelto=int(input("Inserisci l'ID del prodotto di cui vuoi vedere il dettaglio: "))
            if id_scelto in lista_id:
               errore=False
               return id_scelto
            else:
               print("ID non valido. Riprova.")
         except:
           print("Inserisci un numero valido.")
def dettaglio_prodotto(id_scelto):
      response = requests.get(f"https://fakeapi.net/products/{id_scelto}")
      if response.status_code != 200:
       print("Errore nel recupero del dettaglio del prodotto.")
      else:
       prodotto = response.json()
       print(f"ID: {prodotto['id']}, Nome: {prodotto['title']}, Prezzo: {prodotto['price']}, Descrizione: {prodotto['description']}, Categoria: {prodotto['category']}, Brand: {prodotto['brand']}")
while True:
      elenco_categorie=categorie()
      scelta=richiesta_utente(elenco_categorie)
      lista_id=Lista_Prodotti(scelta)
      risposta=Scelta()
      if risposta.lower()=="s":
         id_scelto=scelta_id(lista_id)
         dettaglio_prodotto(id_scelto)