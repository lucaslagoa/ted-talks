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
                          'ratings': self.__parse('ratings')}

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
