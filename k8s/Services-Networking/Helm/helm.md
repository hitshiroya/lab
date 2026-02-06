Install Nginx Chart
helm repo add bitnami https://charts.bitnami.com/bitnami

helm install my-nginx bitnami/nginx --version 19.0.4
Other Helm Commands
helm list

helm repo list

helm search repo bitnami

helm search hub nginx

helm template bitnami/nginx

helm template bitnami/nginx > nginx.yaml

helm template bitnami/nginx -n custom-ns > nginx.yaml

helm uninstall my-nginx