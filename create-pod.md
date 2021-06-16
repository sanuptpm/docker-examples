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