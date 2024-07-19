minikube start --vm-driver=hyperv --force
kubectl apply -f ./  


Run minikube delete in your terminal to remove the existing container
Run minikube start --kubernetes-version=v1.23.12
Then
Run minikube kubectl -- get pods -A to see your running kubelets