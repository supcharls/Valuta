## Valuta omregner:
Lille Python‑program der kan omregne et beløb fra en valuta til en anden vha. ExchangeRate‑API. Programmet kører i terminalen og spørger brugeren om valuta og beløb, hvorefter det henter den aktuelle kurs online.


## Krav: for at køre projektet skal du have:
En API‑key fra https://www.exchangerate-api.com/


## Installation - Klon projektet eller download som ZIP
- Åbn projektmappen i VS Code

- Opret og aktiver et virtual environment (terminal):
    Kode
    python -m venv .venv
    
    Windows:
    .venv\Scripts\activate
    
    Mac/Linux:
    source .venv/bin/activate
    
    Installer afhængigheder:
    pip install -r requirements.txt


## Første program kørsel - skal der angives din API‑key så den kan blive gemt i .env (terminal):
    Kode
    python valuta.py --key DIN_API_KEY
    
    
    Det opretter en .env‑fil med:
    API_KEY=DIN_API_KEY


## Brug af programmet
Når API‑key er gemt, kan programmet køres normalt:
    Kode (terminal)
    python valuta.py

    Programmet spørger om:
    Valuta du vil omregne fra (fx EUR)
    Valuta du vil omregne til (fx DKK)

    Beløb X

        Fx:
        Valutaomregner
        Skriv valuta du vil omregne fra (fx EUR): EUR
        Skriv valuta du vil omregne til (fx DKK): DKK
        Beløb du vil omregne: 100
        
            Output:
            Resultat:
            100.0 EUR = 745.32 DKK


## Valuta skal skrives som ISO‑koder (fx DKK, USD, EUR)