# Monitoring du homelab

## Installation

Le monitoring fonctionne sur le nœud djo-k3s-01,
dans le namespace monitoring.

Il est installé avec Helm :
- Release : monitoring
- Chart : kube-prometheus-stack
- Version du chart : 92.11.0
- Configuration : kubernetes/monitoring/values.yaml

## Composants

- Prometheus collecte et conserve les métriques.
- Grafana affiche les métriques dans les dashboards.
- Node Exporter expose les métriques de la VM Linux.
- kube-state-metrics expose l'état des objets Kubernetes.
- Prometheus Operator gère les ressources de monitoring.

## Accès

Grafana est accessible avec Tailscale connecté :
https://djo-k3s-01.tail4cb576.ts.net/grafana/

Tailscale Serve termine HTTPS et transmet les requêtes
à Traefik, qui dirige le chemin /grafana vers Grafana.

## Dashboard DJO CLOUD

Le dashboard contient 32 panneaux de métriques couvrant :
- la santé du cluster ;
- le CPU, la mémoire, le disque et le réseau de la VM ;
- les Pods, les namespaces et les PVC ;
- Navidrome ;
- les composants du monitoring.

Son export JSON est conservé dans :
kubernetes/monitoring/dashboards/djo-cloud-overview.json

Il peut être réimporté depuis l'interface Grafana
en sélectionnant la source de données Prometheus.

## Persistance

Grafana utilise un PVC de 1 Gi.
Prometheus utilise un PVC de 5 Gi.
Les deux utilisent la StorageClass local-path-retain.

Le dashboard a été retrouvé après remplacement du Pod Grafana.

Ces volumes sont locaux au nœud et ne sont pas répliqués.
Git conserve la configuration et le dashboard ;
les données des volumes nécessitent une sauvegarde distincte.

## Collecte Grafana

Le ServiceMonitor de Grafana utilise /grafana/metrics
pour collecter directement ses métriques en interne.

## Limites actuelles

- Un seul nœud Kubernetes.
- Historique Prometheus configuré sur deux jours.
- Alertmanager désactivé.
- Aucune notification d'alerte configurée.
