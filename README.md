# Geolocalización de IP
Este es un script en Python que permite geolocalizar una dirección IP utilizando la API de ***ipinfo.io***. El script toma una dirección IP como argumento y devuelve información detallada sobre su ubicación, proveedor de servicios, y más.

## Requisitos
Antes de ejecutar el script, asegúrate de tener los siguientes requisitos:

* Python 3.x instalado en tu sistema.

* Paquete ipinfo: usado para interactuar con la API de geolocalización.

* Paquete python-dotenv: utilizado para cargar variables de entorno desde un archivo .env (para el token de acceso).

* Token de acceso a la API de ipinfo.io: Necesitarás registrarte en ipinfo.io y obtener un token personal para hacer solicitudes a la API.

## Instalación
1. Clonar el repositorio:
```
git clone https://github.com/tu_usuario/tu_repositorio.git
cd tu_repositorio
```

2. Instalar dependencias:

Instalar las librerías necesarias:
```
pip install ipinfo python-dotenv
```
3. Configurar el archivo .env:

Crea un archivo llamado .env en el directorio raíz del proyecto y agrega tu token de acceso de la siguiente manera:
```
ACCESS_TOKEN=tu_token_de_ipinfo
```
> El archivo .env debe estar en el mismo directorio que el script.

## Uso
Para ejecutar el script, debes proporcionar la IP objetivo como argumento. El comando básico es el siguiente:

```
python geolocalizacion_ip.py -t <IP_OBJETIVO>
```
Ejemplo:
```
python geolocalizacion_ip.py -t 8.8.8.8
```
Este comando consultará la dirección IP 8.8.8.8 y te devolverá detalles sobre la ubicación de esa IP.

## Descripción del código
El script hace uso de los siguientes componentes:

1. **Carga del archivo .env**: El token de acceso se carga desde un archivo .env para mantener la seguridad del código.

2. **Argumentos de línea de comando**: El script utiliza la librería argparse para manejar los argumentos desde la línea de comandos. El único argumento requerido es la dirección IP que se desea geolocalizar.

3. **Consulta a la API de ipinfo.io**: Usando el token de acceso, se realiza una solicitud a la API de ipinfo.io para obtener detalles sobre la IP proporcionada.

4. **Manejo de errores**: Si ocurre un error al obtener los detalles de la IP (por ejemplo, si la API no responde o la IP no es válida), el script mostrará un mensaje de error y terminará la ejecución.

## Ejemplo de salida
Cuando ejecutes el script, la salida será algo similar a esto:

```
hostname : example.com
ip : 8.8.8.8
city : Mountain View
region : California
country : US
loc : 37.4056,-122.0775
org : AS15169 Google LLC
postal : 94043
timezone : America/Los_Angeles
```
