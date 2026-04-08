# Password Cracking Lab 🔐

## ⚠️ Avertissement
Ce projet est réalisé dans un cadre strictement éducatif.
Tous les hashes ont été générés par mes soins.
Ne jamais utiliser ces techniques sur des systèmes sans autorisation.

## Description
Projet de password cracking qui démontre que les mots de passe simples 
sont très faciles à cracker. Ce projet a été réalisé car le domaine de 
la cybersécurité m'intéresse fortement et que je souhaite évoluer dans 
ce secteur.

## Objectifs
- Comprendre la vraie méthode de brute force
- Comprendre pourquoi on privilégie un mot de passe fort plutôt que faible
- Comprendre ce qu'est le hashing et le salage

## Outils utilisés
- Python + hashlib + subprocess
- John the Ripper
- Hashcat
- rockyou.txt (14 millions de mots de passe)
- Kali Linux (WSL)

## Résultats
- ✅ `123456` cracké en **0.415s** avec wordlist
- ✅ `raed` cracké en **1.490s** en brute force pur
- ❌ `X7$kP#2mQ` — introuvable même après 0.973s de recherche
- ❌ `passwordx7k9` (hash salé) — résiste totalement à rockyou.txt
- ✅ Le même mot de passe avec 2 sels différents génère 3 hashes différents
  ## Screenshots
  -![resultat sur le mot de passe "123456"](screenshots/1775687299368_image.png)
  -![resultat sur le mot de passe "raed"](screenshots/1775687267210_image.png)
  -![resultat sur un mot de passe fort](screenshots/1775687313762_image.png)
  -![resultat sur un hash salé](screenshots/1775687355261_image.png)
  
  
  

## Comment lancer le projet
1. Modifier la variable `liste` à la ligne 42 du fichier `password_cracker.py`
2. Lancer le script depuis le terminal :
```bash
python password_cracker.py
```

## Ce que j'ai appris
- Utiliser John the Ripper et Hashcat
- Hashcat est plus rapide que John the Ripper grâce au GPU
- Fonctions de la bibliothèque `hashlib`
- Lancer des commandes Kali Linux depuis Python avec `subprocess`

## Améliorations futures
- Ajouter une attaque par règles (rule-based)
- Tester avec des wordlists plus grandes
- Ajouter une interface graphique
