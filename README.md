# DJO CLOUD — Homelab personnel

Projet personnel pour apprendre Linux, Docker, Kubernetes et DevOps
en construisant progressivement un cloud personnel.

## Infrastructure actuelle

- Machine hôte : HP ZBook sous Windows 11 Pro.
- Virtualisation : VMware Workstation.
- VM principale : Ubuntu Server, nommée djo-k3s-01.
- Orchestration : Kubernetes avec K3s.
- Application principale : Navidrome.
- Accès distant privé : Tailscale.
- Accès HTTPS : reverse proxy Tailscale Serve.
- VM historique : djo-lab-01, avec l'ancienne installation Docker arrêtée.
- Exercices Docker et Nginx conservés dans le dépôt.

## Configuration des applications

- nginx/compose.yaml
- navidrome/compose.yaml

## Donnees persistantes

Les dossiers navidrome/data/ et navidrome/music/ sont exclus de Git.
Leur sauvegarde et leur restauration seront documentees separement.

## Prochaines evolutions

- Sauvegarde et restauration de Navidrome.
- Kubernetes avec K3s.
- Monitoring avec Prometheus et Grafana.
- CI/CD et GitOps avec Argo CD.
- Interface de gestion DJO CLOUD.

## Documentation

- [Architecture Docker — historique](docs/architecture.md)
- [Exploitation Docker — historique](docs/exploitation.md)
- [Sauvegarde et restauration Docker](docs/sauvegarde-restauration.md)
- [Kubernetes — environnement principal](docs/kubernetes.md)
- [Monitoring](docs/monitoring.md)

## Kubernetes

- Nœud : djo-k3s-01, sous Ubuntu Server.
- Distribution : K3s v1.36.5+k3s1.
- Application : Navidrome 0.64.2.
- Stockage : deux PVC locaux avec une politique Retain.
- Entrée HTTP : Traefik.
- Accès HTTPS privé : Tailscale Serve.
- Manifests : kubernetes/navidrome/
- Pod temporaire d'import : operations/navidrome/restore-pod.yaml
- Bascule vers Kubernetes validée.
- Lecture validée depuis le PC et l'iPhone.
- Retour du service après redémarrage de la VM validé.
- Ancienne installation Docker conservée comme point de retour.
