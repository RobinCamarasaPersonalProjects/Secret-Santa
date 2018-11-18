#!/usr/bin/env python
# -*- coding: utf-8 -*

import pandas
import numpy as np


def write_result(i, j, participants):
    file = open('./out/' + participants[i] + '.txt', 'w+')
    file.write(participants[i] + ' doit offrir son cadeau à ' + participants[j])
    file = open('./j_ai_pas_eu_mon_cadeau/' + participants[j] + '.txt', 'w+')
    file.write(participants[i] + ' doit offrir son cadeau à ' + participants[j])


def is_not_good_permutation(array):
    for i, j in enumerate(array):
        if i == j:
            return True
    return False


table = pandas.read_csv('./in/participants.csv')
shuffle_index = np.random.permutation(np.arange(table.size))
while is_not_good_permutation(shuffle_index):
    shuffle_index = np.random.permutation(np.arange(table.size))
for i, j in enumerate(shuffle_index):
    write_result(i, j, table.get('participants'))