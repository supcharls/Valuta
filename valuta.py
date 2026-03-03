import argparse       
import requests        
import os                
from dotenv import load_dotenv

load_dotenv()

parser = argparse.ArgumentParser()
parser.add_argument("--key")

args = parser.parse_args()


# Hvis bruger har givet en key - gem til .env
if args.key:
    with open(".env", "w") as env_file:
        env_file.write(f"API_KEY={args.key}\n")
    print("API key er gemt")


# Get API key fra .env
api_key = os.getenv("API_KEY")


# Hvis ingen nøgle - stop program
if not api_key:
    print("Fejl - ingen API key fundet")
    print("Kør programmet første gang sådan:")
    print("python valuta.py --key DIN_API_KEY")
    exit()


# Bruger input
print("\nValutaomregner")

from_currency = input("Skriv valuta du vil omregne fra (fx EUR): ").upper()
to_currency = input("Skriv valuta du vil omregne til (fx DKK): ").upper()
amount = input("Beløb du vil omregne: ")


# Tjek for fejl input - fx bogstaver
try:
    amount = float(amount)
except:
    print("Ikke et gyldigt tal prøv igen.")
    exit()



# Kontakt til API for conversion resultater
url = f"https://v6.exchangerate-api.com/v6/{api_key}/pair/{from_currency}/{to_currency}/{amount}"

response = requests.get(url)
data = response.json()

# Tjek for API errors
if data["result"] == "error":
    print(f"API fejl: {data['error-type']}")
    print("Tjek om valutakoder er rigtige (fx DKK, USD, EUR)")
    exit()



# Resultat for brugeren
converted_amount = data["conversion_result"]
rate = data["conversion_rate"]

print(f"\nResultat:")
print(f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")