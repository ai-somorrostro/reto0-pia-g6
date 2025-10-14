# Rama contenedores

En esta rama nos encargamos de crear los diferentes contenedores necesarios para hacer la automatización de diferentes acciones como iniciar los servidores de influx, grafana y node-red, al igual que meter datos en influx con un .py de jupyter; meter datos en la base de datos SQL; y generar csv's.

# Rama main

En esta rama subimos todos los archivos creados para su exposición. En esta rama no se suelen hacer los cambios de los archivos si no en las ramas que derivan de esta como la de contenedores.

# 🚀 Instrucciones

Para poder utilizar este repositorio se necesita usar una maquina virtual o un wsl y utilizar linux.

---

## 📋 Requisitos previos

Asegúrate de tener instaladas las siguientes herramientas en tu sistema:

- [Git](https://git-scm.com/)
- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/)

Puedes verificar la instalación con:
```bash
git --version
docker --version
docker compose version
```
## Comandos necesarios

### Clonar el repo

```bash
git clone git@github.com:ai-somorrostro/reto0-pia-g6.git
```

### Entrar al directorio

```bash
cd contenedor-influx-grafana-nodered
```

### Levantar los contenedores

```bash
docker compose up -d
```
