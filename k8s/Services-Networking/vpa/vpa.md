Create Nginx Deployment
nano nginx-deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
spec:
  replicas: 2
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:latest
        resources:
          requests:
            cpu: "50m"
            memory: "50Mi"
kubectl create -f nginx-deployment.yaml
Create VPA with updateMode to OFF
apiVersion: "autoscaling.k8s.io/v1"
kind: VerticalPodAutoscaler
metadata:
  name: nginx-vpa
spec:
  targetRef:
    apiVersion: "apps/v1"
    kind:       Deployment
    name:       nginx-deployment
  updatePolicy:
    updateMode: "Off"
kubectl get vpa

Run this after few minutes

kubectl describe vpa nginx-vpa
Update VPA mode to Auto
Terminal Tab 1

kubectl get pods -w
Terminal Tab 2

kubectl edit vpa nginx-vp