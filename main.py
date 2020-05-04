#!/usr/bin/python3 
# -*- coding: utf-8 -*-
# GoTube

from pytube import YouTube #Convertidor de Youtube
from pytube.cli import on_progress #Barra de descarga...

class GoTube():
    def __init__(self):
        print("-------Convertidor de Youtube------")
        self.url = input("URL: ") #Ingresa una URL
        print("")

    def prepare_download(self):
        print("Preparando Descarga...")
        #Creamos un atributo y le asignamos la 'URL' y una 'Barra de Descarga'
        self.yt = YouTube(self.url, on_progress_callback=on_progress)

    def start_download(self):
        print("\nIniciando Descarga...")
        self.yt.streams.first().download() #Iniciamos la Descarga.
        print("\n¡Descarga Completada ;)!")

if __name__ == '__main__':
    gt = GoTube() #Creamos nuestro objeto.
    gt.prepare_download()
    gt.start_download()


