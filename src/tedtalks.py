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
                   saida1.write( str(j+1) + " "  + "Id: " + str(i) + " "  + "Nome: " + str(self.name[i]) + " " + " Parâmetro: " + str(parametro[i]) + " " +  "Descrição da palestra: " + str(self.description[i]) + " " + "Tags: " + str(self.tags[i]) + " " + "Data de publicação: " + str(time.ctime(int(self.published_date[i])))  + " " +  "Ocupação do palestrante: " + str(self.speaker_occupation[i]) + " " )
                   saida1.write("\n")

    def imprimeInfos (self,palestra_id):
        print "Id: " + str(palestra_id) + " "  + "Nome: " + str(self.name[palestra_id]) +  " " +  "Descrição da palestra: " + str(self.description[palestra_id]) + " " + "Tags: " + str(self.tags[palestra_id]) + " " + "Data de publicação: " + str(time.ctime(int(self.published_date[palestra_id])))  + " " +  "Ocupação do palestrante: " + str(self.speaker_occupation[palestra_id])


    def Tempo(self):
        for i in range(0,len(self.published_date)):
            print time.ctime(int(self.published_date[i]))

    def getTag(self, tag):
        tags = {"title": self.title,
                "related_talks": self.related_talks,
                "tags": self.tags,
                "ratings": self.ratings,
                "url": self.url,
                "duration": self.duration,
                "main_speaker": self.main_speaker,
                "views": self.views,
                "comments": self.comments,
                "description": self.description,
                "event": self.event,
                "languages": self.languages,
                "speaker_occupation": self.speaker_occupation,
                "event": self.event,
                "film_date": self.film_date,
                "name": self.name,
                "published_date": self.published_date,
                "tags": self.tags}
        return tags[tag]

    def GrafoTop(self,parametro,tamanho):
        list_value = []
        list_ordenado = list(reversed(sorted(parametro)))

        print list_ordenado

        for i in range(0,len(parametro)):
            for j in range(0,tamanho):
                if int(list_ordenado[j]) == int(parametro[i]):
                    list_value.append(i)

        for i in list_value:
            for j in range(0, len(self.related_talks[i])):
                for k in range(0,len(self.title)) :
                    if self.related_talks[i][j]['title'] == self.title[k]:
                        saida.write(str(i) + " " + str(k))
                        saida.write("\n")
                        #print self.title[i], self.related_talks[i][j]['title']
