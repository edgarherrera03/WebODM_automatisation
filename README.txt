*************************************************************************
******Script python pour le traitement des images prise par un drone*****
*************************************************************************

******************
* Installation : *
******************

1.Dirigez-vous vers le dossier Installation/Logiciels et installez les 
logiciels Docker Desktop et Git.

2. Ouvrez le logiciel Docker Desktop puis acceptez les conditions d'utilisation.
Puis, cliquez sur "Continuer sans se connecter" et sautez le questionnaire. Fermez
la fenêtre une fois le processus d'initialisation terminé.

3. Cherchez sur Microsoft Store Python3.12 et téléchargez-le.

4. Après l'installation de ces trois logiciels, double cliquez sur le 
fichier installation.bat (celui-ci va installer toutes les extensions
utilisées dans le script python et va initialiser le logiciel open source 
Webodm). L'installation prend un peu de temps, attendez jusqu'à lire sur le 
Terminal "Open a web browser and navigate to http://localhost:8000". Ne fermez
pas la fenêtre.

5. Tapez sur votre navigateur http://localhost:8000. Ceci va vous diriger
vers le login de Webodm. 

6. Créez un compte avec un utilisateur et mot de passe (ces données 
seront sauvegardés en local donc les identifiants n'existeront que dans 
l'ordinateur où le programme est installé)

7. Une fois le compte créé vous pouvez fermer la fenêtre ainsi que le terminal.

8. Dirigez-vous dans le dossier Scripts_traitements et ouvrez le fichier
webodm_handler.py sur Bloc de notes.

9. Dans le code cherchez la variable USERNAME et PASSWORD en haut du script, 
et modifiez les valeurs avec les identifiants que vous venez de créer.

10. Sauvegardez le fichier puis fermez-le.

11. Félicitations, vous avez fini l'installation du logiciel.

*******************
** Utilisation:  **
*******************
1. Initialisez le logiciel Docker Desktop.

2. Collez les images que vous souhaitez traiter dans le dossier Images.

3. Double cliquez sur le fichier lancement_traitement.bat, le traitement
des images va être déclenché. Cette tâche prend environ 5 min, s'ouvre et se 
ferme toute seule.

4. Quand toutes les fenêtres sont fermées cela veut dire que le traitement 
a terminé.

5. Vous retrouverez vos résultats dans le dossier Resultats.
