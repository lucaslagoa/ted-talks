#!/usr/bin/env python
# -*- coding: utf-8 -*-
from readfile import ReadFile
import datetime
import time

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

    def ordenarLanguages(self):
        list_ordenado = list(reversed(sorted(self.languages)))
        for i in range(0,len(self.languages)):
            for j in range(0,10):
                if int(list_ordenado[j]) == int(self.languages)[i]:
                    print  j+1 , "º mais traduzido: " , self.name[i], " e foi traduzido para: " , self.languages[i], " línguas."

    def ordenarVisualizacoes(self):
        list_ordenado = list(reversed(sorted(self.views)))
        for i in range(0,len(self.views)):
            for j in range(0,10):
                if int(list_ordenado[j]) == int(self.views[i]):
                    print  j+1 , "º mais visto: " , self.name[i], " e ", self.views[i], " visualizações"

    def ordenarComentarios(self):
        list_ordenado = list(reversed(sorted(self.comments)))
        for i in range(0,len(self.comments)):
            for j in range(0,10):
                if int(list_ordenado[j]) == int(self.comments[i]):
                    print  j+1 , "º mais comentado: " , self.name[i], "Ocupação: " , self.speaker_occupation[i] , " e ", self.comments[i], " comentarios e os trabalhos relacionados são: " , self.related_talks[i]

    def Tempo(self):
        for i in range(0,len(self.published_date)):
            print time.ctime(int(self.published_date[i]))
