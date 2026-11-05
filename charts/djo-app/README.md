# Chart Helm djo-app

Chart personnel pour déployer une application HTTP dans DJO CLOUD.

## Ressources créées

- Un Deployment avec un nombre de réplicas configurable.
- Un Service ClusterIP pour joindre les Pods.
- Une readinessProbe HTTP pour vérifier leur disponibilité.

## Configuration

Le fichier charts/djo-app/values.yaml définit les valeurs par défaut :
image, nombre de réplicas, ports, ressources et chemin de vérification HTTP.

Le fichier kubernetes/lab-helm/values.yaml personnalise l'installation
web-helm et demande deux réplicas.

## Déploiement

Exécuter depuis la racine du dépôt :

```bash
sudo helm upgrade --install web-helm ./charts/djo-app \
  --namespace lab-helm \
  --create-namespace \
  --kubeconfig /etc/rancher/k3s/k3s.yaml \
  --values kubernetes/lab-helm/values.yaml \
  --wait \
  --timeout 180s
```

## Vérification

```bash
sudo k3s kubectl get deployment,pods,service -n lab-helm

sudo helm history web-helm \
  --namespace lab-helm \
  --kubeconfig /etc/rancher/k3s/k3s.yaml
```

Le Service est interne au cluster. Son adresse peut être consultée
avec la commande ci-dessus.

## État validé

- Installation initiale avec un réplica.
- Mise à jour avec un fichier de valeurs demandant deux réplicas.
- Deux Pods prêts et réponse HTTP 200.
