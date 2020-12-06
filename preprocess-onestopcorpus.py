#!/usr/bin/env python
# coding: utf-8


import pandas as pd
import os
import numpy
import ftfy
import unidecode

curr_directory_path = os.path.abspath(os.getcwd())

data = []

#Level 0 
path = curr_directory_path + '/Ele-Txt/'
count = 0
files = os.listdir(path)
for f in files:
    count+=1
    with open(path+f, 'r', encoding="ISO-8859-1") as myfile:
        print(count)
        print('FILE:', path + f)
        text = myfile.read().replace('\n', ' ')
        text = ftfy.fix_text(text)
        this_text = text.replace('Ò', '\'').replace('Õ', '\'').replace('Ó', '\'').replace('Ñ', ' ').replace('Ð', '-').replace('Ô', '\'')
        text = unidecode.unidecode(text)
        data.append((f, text, 'ele'))


#Level 1

path = curr_directory_path + '/Int-Txt/'
count = 0
files = os.listdir(path)
for f in files:
    count+=1
    with open(path+f, 'r', encoding="ISO-8859-1") as myfile:
        print(count)
        print('FILE:', path + f)
        text = myfile.read().replace('\n', ' ')
        text = ftfy.fix_text(text)
        this_text = text.replace('Ò', '\'').replace('Õ', '\'').replace('Ó', '\'')                                    .replace('Ñ', ' ').replace('Ð', '-').replace('Ô', '\'')
        text = unidecode.unidecode(text)
        data.append((f,text, 'int'))



#Level 2

path = curr_directory_path + '/Adv-Txt/'
count = 0
files = os.listdir(path)
for f in files:
    count+=1
    with open(path+f, 'r', encoding="ISO-8859-1") as myfile:
        print(count)
        print('FILE:', path + f)
        text = myfile.read().replace('\n', ' ')
        text = ftfy.fix_text(text)
        this_text = text.replace('Ò', '\'').replace('Õ', '\'').replace('Ó', '\'')                                    .replace('Ñ', ' ').replace('Ð', '-').replace('Ô', '\'')
        text = unidecode.unidecode(text)
        data.append((f,text, 'adv'))



df = pd.DataFrame(data)


df.columns = ['Filename', 'Text', 'Level']
df.to_csv('onestop-english.csv')


