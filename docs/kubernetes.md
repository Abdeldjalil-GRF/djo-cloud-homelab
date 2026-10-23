# Kubernetes — environnement principal

## Infrastructure

- Hôte physique : HP ZBook sous Windows, avec VMware Workstation.
- VM principale : djo-k3s-01, sous Ubuntu Server.
- Distribution Kubernetes : K3s v1.36.5+k3s1.
- Un seul nœud assure le control plane et l'exécution des applications.
- Les conteneurs sont exécutés par containerd.
- Dépôt de travail : /home/djo/homelab sur djo-k3s-01.

## Application

- Navidrome 0.64.2.
- Namespace : music.
- Deployment : navidrome.
- Un replica, avec une stratégie Recreate.
- Exécution avec UID et GID 1000.
- Startup probe et readiness probe sur /ping.

## Accès

Adresse principale :

https://djo-k3s-01.tail4cb576.ts.net/

L'appareil client doit être connecté à Tailscale.

Tailscale Serve reçoit la connexion HTTPS sur le port 443.
Il transmet la requête à http://127.0.0.1:80 dans la VM.

Traefik utilise la règle Ingress pour rejoindre le Service
Navidrome, qui transmet ensuite la requête au Pod sur le port 4533.

L'authentification Navidrome reste nécessaire.

## Stockage

| PVC | Capacité déclarée | Montage | Accès applicatif |
|---|---|---|---|
| navidrome-data | 2Gi | /data | Lecture et écriture |
| navidrome-music | 20Gi | /music | Lecture seule |

Les deux PVC utilisent la StorageClass local-path-retain.

Les données restent sur le disque de djo-k3s-01.
Elles ne sont pas répliquées sur un autre nœud.

La politique Retain permet de conserver les volumes après la
suppression des PVC pour une récupération manuelle.
Elle ne remplace pas une sauvegarde.

## Exploitation

- Services : `systemctl is-active k3s tailscaled`
- Nœuds : `sudo k3s kubectl get nodes`
- Application : `sudo k3s kubectl get pods,pvc,service,ingress -n music`
- Logs : `sudo k3s kubectl logs deployment/navidrome -n music --tail=50`
- Déploiement : `sudo k3s kubectl rollout status deployment/navidrome -n music`
- Proxy HTTPS : `tailscale serve status`
- Test HTTP local : `curl -i http://127.0.0.1/ping`

## Migration et validations

Les données de l'ancienne installation Docker ont été restaurées
dans les PVC avec un Pod temporaire de restauration.

Validations réalisées :

- Connexion au compte et lecture de musique.
- Accès depuis le PC et l'iPhone.
- Accès distant privé avec Tailscale.
- Conservation des données après remplacement du Pod.
- Retour du service après redémarrage de la VM.
- Fonctionnement avec l'ancienne application Docker arrêtée.

L'ancienne installation reste conservée sur djo-lab-01.

## Configuration et sauvegardes

Git conserve les manifests et la documentation.
Les données applicatives et les fichiers musicaux sont sauvegardés
séparément.

Une sauvegarde Docker a été créée et sa restauration a été testée.
La procédure de sauvegarde manuelle depuis les PVC Kubernetes
reste à mettre en place.

Les déploiements sont actuellement appliqués avec kubectl.
GitOps avec Argo CD sera ajouté ultérieurement.

## Disponibilité

Le ZBook et la VM K3s doivent rester démarrés pour accéder au service.

Le cluster possède un seul nœud et dépend d'un seul ordinateur
physique.
