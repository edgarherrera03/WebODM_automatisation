###############################################
###### MODULES UTILISÉS (NE PAS TOUCHER) ######
###############################################
import requests
import time


###############################################
################ Fonctions ####################
###############################################
def wait_for_url(url, timeout=60):
    start_time = time.time()
    while True:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print(f"Connexion au serveur réussie.")
                return
            else:
                print(f"Attente de l'URL {url}...")
        except requests.RequestException:
            print(f"Attente de disponibilité du serveur...")
        if time.time() - start_time >= timeout:
            print("Délai d'attente dépassé. L'URL n'est pas disponible.")
            return
        time.sleep(5)

url = "http://localhost:8000/login" 
wait_for_url(url)
