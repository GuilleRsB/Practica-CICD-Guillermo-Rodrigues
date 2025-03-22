# Practica-CICD-Guillermo-Rodrigues
Practica CICD Guillermo Rodrigues


## INDICE

* [*Primera parte*](#primera-parte) : Objetivo y Requisitos
* [*Segunda parte*](#segunda-parte) : Estrcutura y Comandos
* [*Tercera parte*](#tercera-parte) : Archivos
* [*Cuarta parte*](#cuarta-parte) :


## Primera parte

En esta práctica vamos a implementar un pipeline de CI/CD utilizando **CircleCI** para una aplicación Flask, lo desplegará e Kubernetes utilizando **ArgoCD**. Este pipeline automatiza varias tareas, como por ejemplo la construcción de la imagen de Docker, ejecución de tests, análisis de seguridad, análisis estático de código y el despliegue de la aplicación.

* Nuestro proyecto tendrá la siguiente estructura:

```bash
D:\Escritorio\DEVOPS\CICD\Practica final CICD
│
├── __pycache__                   # Archivos de cache generados por Python
│
├── .circleci                      # Configuración de CircleCI
│
├── .pytest_cache                  # Archivos de cache generados por pytest
│
├── app                             # Código de la aplicación
│   └── app.py                      # Código fuente principal de la aplicación
│
├── k8s                             # Manifiestos de Kubernetes
│   ├── deployment.yaml            # Definición del Deployment
│   ├── ingress.yaml               # Definición del Ingress (aunque estás evitando Ingress)
│   └── service.yaml               # Definición del Service
│
├── .coverage                       # Archivo de cobertura de código generado por pytest
├── .dockerignore                   # Archivos y carpetas a excluir en la construcción de la imagen Docker
├── .gitignore                      # Archivos y carpetas a excluir del repositorio Git
├── application.yaml                # Archivo de configuración para la aplicación
├── coverage.xml                    # Informe de cobertura de código generado por pytest
├── Dockerfile                      # Definición de la imagen Docker
├── kind-config.yaml                # Configuración del clúster Kind
├── kubectl                         # Script o archivo de configuración para interactuar con Kubernetes
├── README.md                       # Documentación del proyecto
├── repo.sh                         # Script para gestionar el repositorio
├── requirements.txt                # Dependencias de Python
└── test_app.py                     # Archivo de prueba de la aplicación
```