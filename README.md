# WebODM_automatisation

Python script that automates image stitching taken with a drone. The script uses the open source project WebODM at **https://www.opendronemap.org/webodm/** to upload the images to stitch and downloading the results.

This program is destined for user that do not know how to code, that is why all commands are called by two .bat files that just need to be clicked by users.

The all program is mainly done for windows users, you just need to follow the instructions given in the README.txt. I included the .exe files of the version of Docker Desktop and Git the script was tested. Two files .bat are also included that will be the ones to admnistrate main part of the installation and the use of the programs. 

For Linux and MacOs users, you'll need to install Docker Desktop, Git and Python (the script was tested with version 3.12 but should work with later versions). The .bat files will not work, so you'll need to write the commands by your self. Follow the README.txt and instead of cliquing in the .bat tap these command in your terminal : 

Installation :
1.  Place you in the main folder (WebODM_automatisation) and tap the next commands:
    ```
    python3 ./Installation/install_requirements.py
    git clone https://github.com/OpenDroneMap/WebODM --config core.autocrlf=input --depth 1
     ./WebODM/webodm.sh start
    ```
2. Follow the next steps descrived in the README.txt

Use : 
1. Place you in the main folder (WebODM_automatisation) and tap the next commands:
   ```
   ./WebODM/webodm.sh start
   python3 Scripts_traitements/webodm_handler.py
   ./WebODM/webodm.sh stop
   ```
2. Follow the next steps descrived in the README.txt
