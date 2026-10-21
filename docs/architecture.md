# Architecture actuelle

## Hébergement

- Poste physique : HP ZBook sous Windows 11 Pro.
- Hyperviseur : VMware Workstation.
- Serveur virtuel : Ubuntu Server, nommé djo-lab-01.
- Utilisateur Linux : djo, UID 1000 et GID 1000.
- Applications exécutées avec Docker Compose.

## Accès à Navidrome

L'iPhone utilise Tailscale pour rejoindre le réseau privé.

L'adresse HTTPS de Navidrome est :
https://djo-lab-01.tail4cb576.ts.net/

Tailscale Serve reçoit la connexion HTTPS sur le port 443,
puis transmet la requête à http://127.0.0.1:4533 dans Ubuntu.

Docker publie le port du conteneur Navidrome uniquement sur
l'adresse de boucle locale de la VM.

Une authentification Navidrome reste nécessaire pour écouter
la musique.

## Stockage persistant

| Dossier dans Ubuntu | Dossier dans le conteneur | Accès |
|---|---|---|
| ~/homelab/navidrome/data | /data | Lecture et écriture |
| ~/homelab/navidrome/music | /music | Lecture seule |

Ces dossiers sont des bind mounts et sont exclus de Git.

## Exercice Nginx

Nginx sert une page HTML sur le port 8080 de la VM.
Ses fichiers viennent de ~/homelab/nginx/html.

Le reverse proxy utilisé pour Navidrome est Tailscale Serve.

## Disponibilité

Navidrome possède la politique de redémarrage unless-stopped.

Le ZBook doit rester allumé, la VM démarrée et la connexion
Internet disponible pour permettre l'accès distant.

Toutes les VM dépendent du même ordinateur physique.
