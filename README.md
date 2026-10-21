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
