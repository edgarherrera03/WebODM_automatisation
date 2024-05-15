# WebODM_automatisation
# Image Stitching

Python script that automates image stitching taken with a drone. The script utilizes the open-source project WebODM, accessible at [WebODM](https://www.opendronemap.org/webodm/), for uploading the images to stitch and downloading the results.

This program is designed for users who are not familiar with coding; hence, all commands are invoked by two .bat files that can be executed by users with a simple click.

The program is primarily developed for Windows users. Simply follow the instructions provided in the README.txt. Included in the package are the .exe files for the versions of Docker Desktop and Git with which the script has been tested. Additionally, two .bat files are provided to manage the main parts of the installation and the usage of the programs.

For Linux and macOS users, Docker Desktop, Git, and Python (tested with version 3.12 but should be compatible with later versions) need to be installed. The .bat files won't function on these systems; therefore, you'll have to input the commands manually. Refer to the README.txt, and instead of clicking on the .bat files, execute these commands in your terminal:

Installation :
1.  Place you in the main folder (WebODM_automatisation) and tap the next commands:
    ```bash
    python3 ./Installation/install_requirements.py
    git clone https://github.com/OpenDroneMap/WebODM --config core.autocrlf=input --depth 1
     ./WebODM/webodm.sh start
    ```
2. Follow the next steps descrived in the README.txt

Use : 
1. Place you in the main folder (WebODM_automatisation) and tap the next commands:
   ```bash
   ./WebODM/webodm.sh start
   python3 Scripts_traitements/webodm_handler.py
   ./WebODM/webodm.sh stop
   ```
2. Follow the next steps descrived in the README.txt
