# DJO CLOUD — Homelab personnel

Projet personnel pour apprendre Linux, Docker, Kubernetes et DevOps
en construisant progressivement un cloud personnel.

## Infrastructure actuelle

- Machine hote : HP ZBook sous Windows.
- Virtualisation : VMware Workstation.
- VM : Ubuntu Server, nommee djo-lab-01.
- Application personnelle : Navidrome.
- Exercice Docker : Nginx.
- Acces distant prive : Tailscale.
- Acces HTTPS : reverse proxy Tailscale Serve.

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

- [Architecture](docs/architecture.md)
- [Exploitation](docs/exploitation.md)
- [Sauvegarde et restauration](docs/sauvegarde-restauration.md)

## Kubernetes

- Nœud : djo-k3s-01, sous Ubuntu Server.
- Distribution : K3s v1.36.5+k3s1.
- Application : Navidrome 0.64.2.
- Stockage : deux PVC locaux avec une politique Retain.
- Entrée HTTP : Traefik.
- Accès HTTPS privé : Tailscale Serve.
- Manifests : kubernetes/navidrome/
- Pod temporaire d'import : operations/navidrome/restore-pod.yaml
- Migration en cours de validation avant bascule définitive.
