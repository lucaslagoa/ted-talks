#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse, sys
import pandas as pd
import ast

class ReadFile():
    def __init__(self, ted_talks):
        filename = ted_talks.filename
        ted_talks.title =  list(pd.read_csv(filename)['title'])
        ted_talks.related_talks =  list(self.__parse(ted_talks, 'related_talks'))
        ted_talks.ratings =  list(self.__parse(ted_talks, 'ratings'))
        ted_talks.tags =  list(pd.read_csv(filename)['tags'])
        ted_talks.url =  list(pd.read_csv(filename)['url'])
        ted_talks.duration =  list(pd.read_csv(filename)['duration'])
        ted_talks.main_speaker =  list(pd.read_csv(filename)['main_speaker'])
        ted_talks.views =  list(pd.read_csv(filename)['views'])
        ted_talks.comments =  list(pd.read_csv(filename)['comments'])
        ted_talks.description =  list(pd.read_csv(filename)['description'])
        ted_talks.event =  list(pd.read_csv(filename)['event'])
        ted_talks.languages =  list(pd.read_csv(filename)['languages'])
        ted_talks.speaker_occupation =  list(pd.read_csv(filename)['speaker_occupation'])
        ted_talks.event =  list(pd.read_csv(filename)['event'])
        ted_talks.film_date =  list(pd.read_csv(filename)['film_date'])
        ted_talks.name =  list(pd.read_csv(filename)['name'])
        ted_talks.published_date =  list(pd.read_csv(filename)['published_date'])
        ted_talks.tags =  list(pd.read_csv(filename)['tags'])

        ted_talks.set_n_nodes()

    def __parse(self, ted_talks, name):
        data = pd.read_csv(ted_talks.filename)[name]
        result = []

        for d in data:
            d = d[1:-1].split('},')
            rows = []

            for value in d:
                if value[-1] != '}':
                    value = value + '}'

                value = value.strip()
                rows.append(ast.literal_eval(value))

            result.append(rows)
        return result
