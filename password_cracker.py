import hashlib
import os
import subprocess

#Fonctions

def generer_hashes(liste):
    md5_list = []
    sha256_list = []
    for mot in liste:
        md5_list.append(hashlib.md5(mot.encode()).hexdigest())
        sha256_list.append(hashlib.sha256(mot.encode()).hexdigest())
    return md5_list, sha256_list

def sauvegarder_hashes(liste1, liste2):
    fichier = open("hashes_md5.txt", "w")
    fichier2 = open("hashes_sha256.txt", "w")
    for mot in liste1:
        fichier.write(mot + "\n")
    for i in liste2:
        fichier2.write(i + "\n")
    fichier.close()
    fichier2.close()

def lancer_cracking():
    subprocess.run(["wsl", "-d", "kali-linux", "john", "--format=raw-md5", "--wordlist=/usr/share/wordlists/rockyou.txt", "/mnt/c/Users/raedr/OneDrive/Bureau/Projets/hashes_md5.txt"])    
    subprocess.run(["wsl", "-d", "kali-linux", "john", "--format=raw-sha256", "--wordlist=/usr/share/wordlists/rockyou.txt", "/mnt/c/Users/raedr/OneDrive/Bureau/Projets/hashes_sha256.txt"])
    subprocess.run(["wsl", "-d", "kali-linux", "john", "--format=raw-md5", "--show", "/mnt/c/Users/raedr/OneDrive/Bureau/Projets/hashes_md5.txt"])
def afficher_resultat(liste, liste1, liste2):
    choix = input("Afficher les hashes en sha256 (s) ou md5 (m) ? ")
    if choix == "s":
        for mot, hashe in zip(liste, liste2):
            print(mot, "=", hashe)
    elif choix == "m":
        for mot, hashe in zip(liste, liste1):
            print(mot, "=", hashe)
    else:
        print("Choix invalide, entrez 's' ou 'm'.")

#Programme principal 

liste = ["123456", "password", "azerty", "dragon99", "X7$kP#2mQ"]

md5_list, sha256_list = generer_hashes(liste)
sauvegarder_hashes(md5_list, sha256_list)
lancer_cracking()
afficher_resultat(liste, md5_list, sha256_list)
