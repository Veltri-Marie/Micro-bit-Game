
# Micro:bit Game - Cat and Player

## Description

Ce projet utilise deux micro:bits pour créer un jeu où un joueur (représenté par un "P") doit échapper à un chat (représenté par un "C") en se déplaçant sur un plateau. Les deux micro:bits communiquent entre eux via la radio pour échanger des informations et permettre au joueur de contrôler sa position en fonction de l'orientation du micro:bit (accéléromètre).

Le jeu fonctionne de la manière suivante :
1. Un micro:bit représente le **gamepad**, il envoie des commandes de direction (haut, bas, gauche, droite) via la radio en fonction de l'orientation du micro:bit.
2. L'autre micro:bit représente la **console**, qui affiche une carte du plateau avec les murs, le joueur et le chat. Le but est d'éviter que le chat attrape le joueur.

## Fonctionnalités

- Communication sans fil via la radio entre deux micro:bits.
- Affichage du plateau de jeu avec un joueur et un chat sur un micro:bit.
- Commande du joueur via le micro:bit "gamepad" en utilisant l'accéléromètre (haut, bas, gauche, droite).
- Affichage des flèches indiquant la direction du chat par rapport au joueur.
- Le jeu se termine lorsque le chat touche le joueur.

## Prérequis

- 2 micro:bits physiques
- Deux câbles USB pour connecter les micro:bits à un ordinateur.

## Installation

### 1. Cloner ce dépôt

Clone ce projet sur ton ordinateur avec la commande suivante :

```bash
git clone https://github.com/ton-utilisateur/ton-repository.git
```

### 2. Téléchargement du code sur les micro:bits

1. **Télécharge le fichier `gamepad.py`** sur le premier micro:bit (celui qui servira de manette).
    - Ouvre le fichier `gamepad.py` dans ton IDE (par exemple VS Code).
    - Connecte ton micro:bit à l'ordinateur avec un câble USB.
    - Télécharge le fichier sur le micro:bit via ton IDE.
  
2. **Télécharge le fichier `console.py`** sur le second micro:bit (celui qui servira de console).
    - Ouvre le fichier `console.py` dans ton IDE.
    - Connecte le second micro:bit à l'ordinateur avec un câble USB.
    - Télécharge le fichier sur le micro:bit via ton IDE.

### 3. Connexion des micro:bits

Assure-toi que les deux micro:bits sont allumés et à portée de radio (environ 10 mètres sans obstacles). Les deux micro:bits doivent être configurés sur le même groupe de radio (par défaut, `group_id = 29`).

### 4. Lancer le jeu

- Le **gamepad** enverra les mouvements de direction via l'accéléromètre.
- La **console** affichera l'état du plateau, avec la position du joueur et du chat. Le jeu continue jusqu'à ce que le chat atteigne le joueur.

## Commandes

Les directions envoyées par le **gamepad** sont basées sur l'orientation du micro:bit :

- **Gauche** : incliner le micro:bit vers la gauche.
- **Droite** : incliner le micro:bit vers la droite.
- **Haut** : incliner le micro:bit vers le haut.
- **Bas** : incliner le micro:bit vers le bas.

## Structure du code

- **`console.py`** : Contient la logique du jeu. Il crée un plateau avec des murs et des objets, et gère le mouvement du joueur et du chat.
- **`gamepad.py`** : Permet de détecter les mouvements du joueur en utilisant l'accéléromètre du micro:bit et d'envoyer les commandes de direction via la radio.

## Déroulé du jeu

Pour voir une démonstration du déroulé du jeu, voici une vidéo expliquant son fonctionnement :  
[Regarder la vidéo du déroulé du jeu](https://youtu.be/JSnIKgiI1E0)

## Aide et support

Si tu rencontres des problèmes ou si tu as des questions concernant l'installation ou le fonctionnement du jeu, n'hésite pas à ouvrir un **issue** sur GitHub ou à poser ta question dans la section dédiée.

---

Bon jeu !
