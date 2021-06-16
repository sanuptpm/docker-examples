# Install and run minikube
https://itnext.io/how-to-experiment-locally-on-kubernetes-with-minikube-and-your-local-dockerfiles-48833fcd90c9

# 1) install dependency
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube 

OR

$ curl -Lo minikube https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64 && chmod +x minikube
$ sudo mv minikube /usr/local/bin

# 2) Add your user to the 'docker' group:
sudo usermod -aG docker $USER && newgrp docker

# 3) Start your cluster
minikube start --driver=docker

# 4)get minikube status
$ minikube status

# ######################################################################

# Deploye resource to cluster
kubectl apply -f pod.yml

# get pods
kubectl get pods

# Get status of pods  
kubectl describe pods docker-examples

# go inside the pods
kubectl exec -it <podname> -- bash

# show running process
ps aux

# List the nodes in your cluster
kubectl get nodes

# List file with there permissions
ls -l