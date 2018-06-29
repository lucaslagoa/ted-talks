#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse, sys
from igraph import *
from tedtalks import *

def main(filename, tags, length):
    ted_talks = TedTalks(filename)
    for tag in tags:
        ted_talks.GrafoTop(ted_talks.getTag(tag), length)

if __name__ == "__main__":
    global data
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", type=str, default='../dataset/ted_talks.csv',
                        help="Nome do arquivo de entrada.")
    parser.add_argument("-t", nargs='*', default=["languages", "views"],
                        help="Tags a serem analisadas, separadas por espaço. Ex.: \"languages views\"")
    parser.add_argument("-n", type=int, default=10,
                        help="Tamanho do resultado.")

    args = parser.parse_args()
    filename = args.f
    tags = args.t
    length = args.n

    print "Arquivo:", filename, "\nTags:", tags, "\nTamanho:", length
    main(filename, tags, length)
