#!/usr/bin/env python
# -*- coding: utf-8 -*-
from readfile import ReadFile
import datetime
import time
from igraph import *

saida = open("saidaGraph.txt",'w')
saida1 = open("saidaTexto.txt",'w')

class TedTalks():
    def __init__(self, filename):
        self.filename = filename
        self.title = None
        self.related_talks = None
        self.tags = None
        self.ratings = None
        self.url = None
        self.duration = None
        self.main_speaker = None
        self.views = None
        self.comments = None
        self.description = None
        self.event = None
        self.languages = None
        self.speaker_occupation = None
        self.event = None
        self.film_date = None
        self.name = None
        self.published_date = None
        self.tags = None
        self.__n_nodes = None
        ReadFile(self)

    def set_n_nodes(self):
        self.__n_nodes = len(self.title)

    def get_n_nodes(self):
        return self.__n_nodes

    def ordenar(self,parametro,tamanho):
        list_ordenado = list(reversed(sorted(parametro)))
        for i in range(0,len(parametro)):
            for j in range(0,tamanho):
                if int(list_ordenado[j]) == int(parametro[i]):
                   saida1.write( str(j+1) + " " + "Nome: " + str(self.name[i]) + " " + " Parâmetro: " + str(parametro[i]) + " " +  "Descrição da palestra: " + str(self.description[i]) + " " + "Tags: " + str(self.tags[i]) + " " + "Data de publicação: " + str(time.ctime(int(self.published_date[i])))  + " " +  "Ocupação do palestrante: " + str(self.speaker_occupation[i]) + " " )
                   saida1.write("\n")

    def Tempo(self):
        for i in range(0,len(self.published_date)):
            print time.ctime(int(self.published_date[i]))

    def descobreId(self): #grafo total
        for i in range(0,len(self.related_talks)):
            for j in range(0,len(self.related_talks[i])):
                saida.write(str(i)+ " " + str(self.related_talks[i][j]['id']))
                saida.write("\n")

    def Grafo_Top(self,parametro,tamanho):
        list_value = []
        list_ordenado = list(reversed(sorted(parametro)))
        for i in range(0,len(parametro)):
            for j in range(0,tamanho):
                if int(list_ordenado[j]) == int(parametro[i]):
                    list_value.append(i)                    
        for i in list_value:
           for j in range(0,len(self.related_talks[i])):
                saida.write(str(i)+ " " + str(self.related_talks[i][j]['id']))
                saida.write("\n")
