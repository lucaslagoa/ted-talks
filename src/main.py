#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse, sys
from igraph import *
from tedtalks import *

def main(filename):
    ted_talks = TedTalks(filename)
    #ted_talks.Tempo()
    #ted_talks.ordenarLanguages()
    #ted_talks.IdentificarInfos()
    #ted_talks.ordenarVizualizacoes()
    ted_talks.ordenarComentarios()
    #ted_talks.ordenarVisualizacoes()

if __name__ == "__main__":
    global data
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", type=str, default='../dataset/ted_talks.csv',
                        help="Nome do arquivo.")
    args = parser.parse_args()
    filename = args.f

    main(filename)
