#!/usr/bin/env python
# -*- coding: utf-8 -*

import pandas
import numpy as np


def write_result(i, j, participants):
    file = open('./out/' + participants[i] + '.txt', 'w+')
    file.write(participants[i] + ' doit offrir son cadeau à ' + participants[j])
    file = open('./j_ai_pas_eu_mon_cadeau/' + participants[j] + '.txt', 'w+')
    file.write(participants[i] + ' doit offrir son cadeau à ' + participants[j])


table = pandas.read_csv('./in/participants.csv')
shuffle_index = np.random.permutation(np.arange(table.size))
for i in shuffle_index:
    write_result(i, (i+1) % table.get('participants').size, table.get('participants'))
