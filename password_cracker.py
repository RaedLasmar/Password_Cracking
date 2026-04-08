import hashlib
import os
import subprocess
def generer_hashes(liste):
    hashe=[]
    hashed=[]
    for mot in liste:
        hashe.append(hashlib.md5(mot.encode()).hexdigest())
        hashed.append(hashlib.sha256(mot.encode()).hexdigest())
        
    return hashe, hashed

def sauvegarder_hashes(liste1, liste2):
    fichier=open("hashes_md5.txt","w")
    fichier2=open("hashes_sha256.txt","w")
    for mot in liste1:
        fichier.write(mot + "\n")
        
    for i in liste2:
        fichier2.write(i + "\n")

    fichier.close()
    fichier2.close()

def lancer_cracking():
    subprocess.run(["wsl", "-d", "kali-linux","john","--format=raw-md5","--wordlist=/usr/share/wordlists/rockyou.txt", "hashes_md5.txt"])
    subprocess.run(["wsl", "-d", "kali-linux","john","--format=raw-sha256","--wordlist=/usr/share/wordlists/rockyou.txt", "hashes_sha256.txt"])

liste = ["123456", "password", "azerty", "dragon99", "X7$kP#2mQ"]

md5_list, sha256_list = generer_hashes(liste)
sauvegarder_hashes(md5_list, sha256_list)
lancer_cracking()
def afficher_resultat(liste,liste1,liste2):
    choix = input("vous voulez les mots de passe en sha256(s) ou md5 (m)?")
    if(choix == "s"):
        for mot,hashe in zip(liste,liste2):
                print(mot,"=",hashe)
    elif(choix == "m"):
        for mot , hash in zip(liste,liste1):
            print(mot,"=",hash)
    else:
        print("Veuillez bien choisir la lettre qui correspond a la méthode")


afficher_resultat(liste,md5_list,sha256_list)