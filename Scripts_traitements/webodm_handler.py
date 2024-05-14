import os
import requests
import time
import json
from image_crop import draw_rectangle

# Define WebODM server URL and credentials
WEBODM_URL = 'http://localhost:8000'  
USERNAME = 'edgar.herrera@etu.emse.fr'             
PASSWORD = 'Lolliers2024'            

def check_task_status(task_id, project_id, headers):
    url = f"{WEBODM_URL}/api/projects/{project_id}/tasks/{task_id}/"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        task_status = response.json()['status']
        progress = 100*response.json()['running_progress']
        return task_status, progress
    else:
        print("Échec de la vérification du statut de la tâche.")
        return None, None

def download_orthophoto(task_id, project_id, headers):
    url = f"{WEBODM_URL}/api/projects/{project_id}/tasks/{task_id}/download/orthophoto.png"
    response = requests.get(url, headers=headers, stream=True)
    with open("./Resultats/orthophoto.png", "wb") as f:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
    print("Resultats sauvegardés ./Resultats/orthophoto.png")
    return "./Resultats/orthophoto.png"

def delete_project(project_id, headers):
    url = f"{WEBODM_URL}/api/projects/{project_id}/"
    response = requests.delete(url, headers=headers)
    if response.status_code==204:
        print("Mémoire liberée")
    else:
        print("Echec dans la libération de la mémoire.")


# Function to upload images to WebODM
def upload_images(image_folder):
    url = f"{WEBODM_URL}/api/projects/"

    # Login to WebODM et obtention du token d'authentication token
    login_data = {'username': USERNAME, 'password': PASSWORD}
    response = requests.post(f"{WEBODM_URL}/api/token-auth/", data=login_data)
    if response.status_code == 200:
        token = response.json()['token']
    elif response.status_code == 400:
        print("Identifiant ou mot de passe incorrect")
        return
    else:
        print("La connexion a échoué")
        return

    headers = {'Authorization': f'JWT {token}'}

    # Création d'un nouveau projet
    project_data = {'name': 'ProjetTest', 'description': 'Au revoir'}  
    response = requests.post(url, headers=headers, json=project_data)
    if response.status_code == 201:
        project_id = response.json()['id']
        print(f"Projet créé avec succès avec l'identifiant : {project_id}")
    else:
        print("Échec de la création d'un nouveau projet.")
        return

    # Télécharger les images au projet
    print("Téléchargement des images...")
    image_files = [f for f in os.listdir(image_folder) if f.endswith(('.jpg', '.jpeg', '.png', '.JPG'))]
    files = [('images[]', (image_file, open(os.path.join(image_folder, image_file), 'rb'), 'image/jpeg')) for image_file in image_files]
    task_name = 'DronLollier' 
    options = json.dumps([
            {
                'name': 'auto-boundary',
                'value': True
            },
            {
                'name': 'fast-orthophoto',
                'value': True
            }, 
            {
                'name': 'orthophoto-png',
                'value': True
            }
        ])
    data = {'name': task_name,'options': options, 'resize_to': 2048} 


    response = requests.post(f"{WEBODM_URL}/api/projects/{project_id}/tasks/", headers=headers, files=files, data=data)
    if response.status_code == 201:
        print("Images téléchargées avec succès.")
        task_id = response.json()['id']
        print("Veuillez patienter pendant le démarrage du traitement d'images...")
        while True:
            task_status, progress = check_task_status(task_id, project_id, headers)
            if task_status == 40:
                print("Tâche terminée avec succès.")
                break
            elif task_status == 20:
                print(f"La tâche est toujours en cours de traitement... Avancement : {progress:.2f}%")
            elif task_status == 30:
                print("Échec de la tâche.")
                return
            elif task_status == 50:
                print("Tâche annulée.")
                return
            time.sleep(5)  # Vérification du statut tout les 5 secondes 
        print("Téléchargement des résultats...")
        orthophoto_path = download_orthophoto(task_id, project_id, headers)
        delete_project(project_id, headers)
        draw_rectangle(orthophoto_path)
    else:
        print("Échec de téléchargement des images.")

# Fonction principale
def main():
    resultats_folder = "./Resultats"
    if not os.path.exists(resultats_folder):
        # Si le dossier "Resultats" n'existe pas, le créer
        os.makedirs(resultats_folder)
        print(f"Dossier {resultats_folder} créé avec succès.")
        
    image_folder = './Images'  # Chemin du fichier où se trouvent les images à traiter
    upload_images(image_folder)


if __name__ == "__main__":
    main()
