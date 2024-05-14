@echo-off
start "" "C:\Program Files\Git\bin\bash.exe" --login -i "./Scripts_traitements/commande_start.sh"
python Scripts_traitements/server_handler.py
python Scripts_traitements/webodm_handler.py
start "" "C:\Program Files\Git\bin\bash.exe" --login -i "./Scripts_traitements/commande_stop.sh"



