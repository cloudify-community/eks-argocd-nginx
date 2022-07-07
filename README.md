# eks-nginx-argocd

This repository contains three blueprints:

1. A main environment blueprint ([blueprint.yaml](./blueprint.yaml)) that deploys EKS, ArgoCD, and NGINX via ArgoCD using Service Composition
2. An ArgoCD blueprint ([argocd.yaml](./argocd.yaml)) that deploys ArgoCD into EKS
3. An NGINX blueprint ([nginx.yaml](./nginx_argocd.yaml)) that deploys NGINX using ArgoCD
