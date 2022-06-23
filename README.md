# EKS-agrocd

this repo contains a blueprint that will create an EKS cluster and install agrocd using bitnami helm chart

then after installing the agrocd:

* add a sample repo that contains nginx inside the manifests
* add an application , then sync it which will trigger the creation of the nginx pod 
