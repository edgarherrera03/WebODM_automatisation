@echo off
python ./Installation/install_requirements.py
start "" "C:\Program Files\Git\bin\bash.exe" --login -i "./Installation/commandes.sh"


