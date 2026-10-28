# Cluster K3s à deux nœuds

Version installée sur les deux nœuds : v1.36.5+k3s1.

## Machines

| Machine | Adresse VMware | Fonction |
|---|---|---|
| djo-k3s-01 | 192.168.52.129 | Serveur K3s et workloads |
| djo-k3s-worker-01 | 192.168.52.131 | Agent K3s et workloads |

Les deux VM communiquent sur le réseau VMware VMnet8.

## Réseau des Pods

- Serveur : 10.42.0.0/24.
- Worker : 10.42.1.0/24.
- Communication entre nœuds avec Flannel VXLAN.

## Validation effectuée

Un Pod client a été placé sur le worker avec nodeSelector.

Depuis ce Pod :
- accès direct au Pod Navidrome : HTTP 200 ;
- accès par la ClusterIP du Service : HTTP 200 ;
- résolution DNS du Service : réussie ;
- accès par le nom DNS du Service : HTTP 200.

Nom DNS testé :
navidrome.music.svc.cluster.local

Manifest du diagnostic :
operations/network-test/client.yaml

Le namespace lab-network est supprimé après le diagnostic.

## Monitoring

Node Exporter est présent sur les deux nœuds.
Les métriques du worker sont accessibles dans Grafana.

## Administration

Les commandes kubectl sont actuellement exécutées
sur djo-k3s-01 avec le kubeconfig d'administration K3s.

## Stockage

Les volumes existants de Navidrome, Grafana et Prometheus
restent locaux à djo-k3s-01.

Les deux VM dépendent du même ordinateur physique.
