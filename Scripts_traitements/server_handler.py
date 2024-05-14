import requests
import time

def wait_for_url(url, timeout=60):
    start_time = time.time()
    while True:
        try:
            # Essayer de faire une requête GET à l'URL
            response = requests.get(url)
            # Vérifier si le code de statut de la réponse est 200 (OK)
            if response.status_code == 200:
                print(f"Connexion au serveur réussie.")
                return
            else:
                print(f"Attente de l'URL {url}...")
        except requests.RequestException:
            print(f"Attente de disponibilité du serveur...")
        # Attendre avant de réessayer
        if time.time() - start_time >= timeout:
            print("Délai d'attente dépassé. L'URL n'est pas disponible.")
            return
        time.sleep(5)

# Test de la fonction avec l'URL localhost:8000/login
url = "http://localhost:8000/login"
wait_for_url(url)
