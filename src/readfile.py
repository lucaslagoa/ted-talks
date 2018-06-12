#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse, sys
import pandas as pd
import ast

class ReadFile():
    def __init__(self, filename):
        self.filename = filename
        self.ted_talks = {'title': pd.read_csv(filename)['title'],
                          'related_talks': self.__parse('related_talks')}

        self.n_nodes = len(self.ted_talks['title'])

    def __parse(self, name):
        data = pd.read_csv(self.filename)[name]

        last_index = len(data[0])-1
        data = data[0][1:last_index].split('},')
        result = []
        for d in data:
            if d[-1] != '}':
                d = d+"}"
            result.append(ast.literal_eval(d.strip()))

        return result
