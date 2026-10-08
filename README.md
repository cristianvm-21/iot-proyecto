# Sistema IoT para Simulación del Monitoreo de Temperatura y Humedad

<!-- Tabla de Contenido-->

<details>
<summary><h2 id="tabla-de-contenido">Tabla de Contenido</h2></summary>
<!-- Lista con Contenido Deplegable-->
 <ol>
   <li><a href="#acerca-del-proyecto">Acerca del Proyecto<a></li>
   <li><a href="#características-principales">Características Principales<a></li>
   <li><a href="#inicio-rápido">Inicio Rápido 🚀</a></li>
   <li><a href="#estructura-del-proyecto">Estructura del Proyecto 📁</a></li>
   <li><a href="#stack-tecnológico">Stack Tecnológico<a></li>
 </ol>
</details>

## Acerca del Proyecto

Este proyecto consiste en la implementación de un sistema IoT orientado a la simulación, transmisión, almacenamiento y visualización de datos provenientes de sensores.

El sistema utiliza una arquitectura basada en contenedores Docker y comunicación mediante el protocolo MQTT, permitiendo integrar distintos servicios para gestionar el flujo de información. El proyecto busca ofrecer una solución que permita:

- Simular la captura de datos provenientes de sensores.
- Publicar y recibir información mediante el protocolo MQTT.
- Almacenar los datos recopilados en una base de datos de series temporales.
- Visualizar las mediciones mediante paneles y gráficos en tiempo real.

## Características Principales

- 📡 Comunicación entre dispositivos mediante MQTT.
- 🌡️ Simulación y publicación de datos de sensores.
- 📨 Gestión de mensajes mediante el broker EMQX.
- 🗄️ Almacenamiento de datos utilizando InfluxDB.
- 📊 Visualización y monitoreo de datos mediante Grafana.
- 🐳 Contenedorización y orquestación de servicios con Docker y Docker Compose.
- 🐍 Implementación de los servicios Publisher y Subscriber utilizando Python.

## Inicio Rápido

Clona el repositorio en tu equipo:

```bash
git clone https://github.com/cristianvm-21/iot-proyecto.git
```

Ingresa a la carpeta del proyecto:

```bash
cd iot-proyecto
```

Asegúrate de tener instalado **Docker** y **Docker Compose** antes de continuar.

## Ejecutar

Para compilar las imágenes del proyecto y levantar todos los contenedores definidos en `docker-compose.yml`, ejecuta:

```bash
docker compose up -d --build
```

Puedes verificar que los contenedores se encuentren en ejecución con:

```bash
docker compose ps
```

Para detener los servicios:

```bash
docker compose down
```

## Visualizar los Servicios

Una vez levantados los contenedores, puedes acceder a las interfaces web de los principales servicios desde el navegador:

- **EMQX Dashboard**  
  [http://localhost:18083](http://localhost:18083)  
  Permite administrar el broker MQTT, visualizar conexiones, clientes, tópicos y mensajes.

- **InfluxDB**  
  [http://localhost:8086](http://localhost:8086)  
  Permite consultar y administrar los datos enviados por el servicio `subscriber` y almacenados en la base de datos.

- **Grafana**  
  [http://localhost:3000](http://localhost:3000)  
  Permite visualizar los datos almacenados en InfluxDB mediante un dashboard y gráficos.

<p align="right"><a href="#tabla-de-contenido">Indice</a></p>

## Estructura del Proyecto

````
iot-proyecto/
├── .env                    # Variables de entorno utilizadas por los servicios del proyecto
├── docker-compose.yml      # Orquesta y configura los contenedores Docker del sistema IoT
├── publisher/              # Servicio encargado de simular y publicar datos de sensores
│   ├── Dockerfile          # Define la imagen Docker del servicio publisher
│   ├── publisher.py        # Genera y publica datos mediante MQTT hacia el broker
│   └── requirements.txt    # Dependencias de Python necesarias para el publisher
└── subscriber/             # Servicio encargado de recibir y procesar los mensajes MQTT
    ├── Dockerfile          # Define la imagen Docker del servicio subscriber
    ├── requirements.txt    # Dependencias de Python necesarias para el subscriber
    └── subscriber.py       # Se suscribe a tópicos MQTT y procesa los datos recibidos
````

<p align="right"><a href="#tabla-de-contenido">Indice</a></p>

## Stack Tecnológico

- ![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
- ![Compose](https://img.shields.io/badge/Compose-7B42BC?style=for-the-badge&logo=docker&logoColor=white)
- ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
- ![EMQX](https://img.shields.io/badge/EMQX-00B173?style=for-the-badge&logo=emqx&logoColor=white)
- ![InfluxDB](https://img.shields.io/badge/InfluxDB-22ADF6?style=for-the-badge&logo=influxdb&logoColor=white)
- ![Grafana](https://img.shields.io/badge/Grafana-F46800?style=for-the-badge&logo=grafana&logoColor=white)
- ![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)

<p align="right"><a href="#tabla-de-contenido">Indice</a></p>