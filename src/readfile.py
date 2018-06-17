#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse, sys
import pandas as pd
import ast

class ReadFile():
    def __init__(self, filename):
        self.filename = filename
        self.ted_talks = {'title': pd.read_csv(filename)['title'],
                          'related_talks': self.__parse('related_talks'),
                          'tags': pd.read_csv(filename)['tags'],
                          'ratings': self.__parse('ratings'),
                          'url': pd.read_csv(filename)['url'],
                          'duration': pd.read_csv(filename)['duration'],
                          'main_speaker': pd.read_csv(filename)['main_speaker'],
                          'views': pd.read_csv(filename)['views'],
                          'comments': pd.read_csv(filename)['comments'],
                          'description': pd.read_csv(filename)['description'],
                          'event': pd.read_csv(filename)['event'],
                          'languages': pd.read_csv(filename)['languages'],
                          'speaker_occupation': pd.read_csv(filename)['speaker_occupation'],
                          'event': pd.read_csv(filename)['event'],
                          'film_date': pd.read_csv(filename)['film_date'],
                          'name': pd.read_csv(filename)['name'],
                          'published_date': pd.read_csv(filename)['published_date'],
                          'tags': pd.read_csv(filename)['tags']}

        self.n_nodes = len(self.ted_talks['title'])

    def __parse(self, name):
        data = pd.read_csv(self.filename)[name]
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