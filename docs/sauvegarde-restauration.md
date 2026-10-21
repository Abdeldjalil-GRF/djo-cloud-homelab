# Sauvegarde et restauration de Navidrome

## Méthode

Sauvegarde à froid : arrêt de Navidrome, création d'une
archive des fichiers, puis redémarrage du service.

L'archive contient :

- navidrome/compose.yaml
- navidrome/data/
- navidrome/music/

## Première archive

Nom : navidrome-20261021T183735Z.tar.gz

Une empreinte SHA-256 accompagne l'archive.

Emplacements :

- Ubuntu : /home/djo/homelab/backups/
- Windows : F:\homelab\backups\navidrome\

## Exercice de restauration

Les fichiers ont été extraits dans un dossier séparé,
sous /home/djo/homelab-restore/.

- Projet Compose : navidrome-restore-test
- Version Navidrome : deluan/navidrome:0.64.2
- Port publié : 127.0.0.1:14533
- Accès depuis Windows : tunnel SSH
- Données utilisées : copie extraite de l'archive

## Vérifications

- [x] Création de l'archive sans erreur.
- [x] Empreintes identiques sur Ubuntu et Windows.
- [x] Connexion avec un compte existant.
- [x] Présence de la playlist sauvegardée.
- [ ] Lecture d'un morceau dans la restauration.
- [ ] Modification de la copie sans effet sur le service principal.

## Limites actuelles

La sauvegarde et sa copie vers Windows sont manuelles.

Les deux copies restent sur le même ordinateur physique.
Une destination sur un support distinct reste à prévoir.
