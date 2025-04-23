import ipinfo
from dotenv import load_dotenv
import os
import sys
import argparse

#Función para cargar archivos .env
load_dotenv()

#Acceder a la información del archivo .env
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")

#Creación de objeto parser
parser = argparse.ArgumentParser(prog="Geolocalizacion de IP", description="Programa que geolocaliza una dirección IP")
parser.add_argument("--target", "-t", required=True, type=str, help="IP objetivo")
parser = parser.parse_args()

#Creación de función para consulta de geolocalización, la cual recibirá como parámatros: IP y TOKEN de búsqueda
def get_ip_details(ip_addr, token):
    '''
    Función de consulta de geolocalización de determinada IP usando API de ipinfo
    
    Parámetros: IP y Token de acceso a la API de ipinfo
    '''
    try:
        #Creación de objeto cliente para poder hacer uso del servicio de la API mediante el Token de acceso
        handler = ipinfo.getHandler(token)

        #Obtener detalles de la consulta
        details = handler.getDetails(ip_addr)

        #Retornar todos los detalles 
        return details.all

    except Exception as e:
        print(f"Error al obtener los detalles de la IP: {ip_addr}")
        sys.exit(1)#En caso de que haya error, el programa se cerrará

if __name__ == '__main__':
    details = get_ip_details(parser.target, ACCESS_TOKEN)
    
    print("\n")

    #Mostrar la información de manera detallada
    for key, value in details.items():
        print(f'\33[34m{key}\33[0m : \33[33m{value}\33[0m')

    print("\n")

