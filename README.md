# k8s-python-api
Python API to run on Kubernetes using NGINX ingress controller as an example. 

* Please read the **TODO LIST** before using this example. It was a primitive implementation that will need more work to be ready for the production environment


## Requirements and Dev Tools

* Python3 - https://www.python.org/ - version 3.7.4
* Pipenv  - https://pipenv.kennethreitz.org/en/latest/ - version 2018.11.26
* Flask   - https://palletsprojects.com/p/flask/ - version 1.1.1
* Pylint  - https://www.pylint.org/ - version 2.4.3


## Development Environment (on macOS Mojave)

Intalling Minikube
```
$ brew install minikube
```

Starting Minikube
```
$ minikube start
```

Installing the first tools, Python3 and Pipenv
```
$ brew install python3
$ brew install pipenv
```

## HELM
The Helm is used to install the NGINX ingress controller. How to install Helm:

```
$ curl https://raw.githubusercontent.com/kubernetes/helm/master/scripts/get > get_helm.sh
$ chmod 700 get_helm.sh
$ ./get_helm.sh
$ helm init
```

## Nginx Ingress Controller
The installation process to NGINX Ingress controller:
```
$ helm install stable/nginx-ingress --name nginx-ingress --set controller.publishService.enabled=true
```

## Deployment the Python API Application

```
$ kubectl apply -f kube/python-api-service-deployment.yaml
$ kubectl apply -f kube/python-api-ingress.yaml
```

To see what is the external IP of load balancer created by NGINX ingress controller use this command:

```
$ kubectl get svc
```

## TODO LIST

1) The application could remove the port that will expose. It will be better to use the environment variables that will keep the configuration into ConfigMaps of Kubernetes.
2) Reduce the size of the image of the container. This example it's using a bigger image. Recommended to use alpine with uwsgi.ini configuration to load the main Python module of the application.
3) Use the Kubernetes on the cloud than minikube to test properly the NGINX ingress controller. Minikube can offer the external IP to the load balancer that will keep the status: pending...
4) Create a Helm chart to the application to keep the code of deployment in the DRY strategy that is easier to maintain, update and deployment with one unique command. 
5) Use the valid domain to allow to access without any custom configuration into /etc/resolv.conf or /etc/hosts to test it.
6) Add Cert-Manager to use [Let's Encrypt](https://letsencrypt.org/) or [Venafi](https://www.venafi.com/) to auto-generate and manage the HTTPS certificates on Kubernetes.  
