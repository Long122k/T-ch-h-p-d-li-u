import csv
from operator import index
from textwrap import indent
import pandas as pd
import numpy as np
from pyvi import ViTokenizer
from sympy import re

def convertStringToSet(dict, token):
    if not token in dict:
        return set()
    tmp = dict[token].replace('[', '').replace(']', '').replace(',', '').split(' ');
    return set(tmp)

def fullTextSearch(input):
    reader = csv.DictReader(open("crawlData/Data/invertedIndex.csv"))
    dict = {}
    for raw in reader:
        dict = raw

    text = input.lower()
    text = ViTokenizer.tokenize(text).split(' ')
    
    indexs = convertStringToSet(dict, text[0])

    for token in text:
        list = convertStringToSet(dict, token)
        indexs = indexs & list

    return getDataByIndex(indexs)


def getDataByIndex(indexs):
    df = pd.read_csv("crawlData/Data/dataTokenize.csv")
    list1 = []
    for idx in indexs:
        idx = int(idx)
        list1.append(df[idx:(idx+1)])
    print(np.array(list1[0:(len(list1)-1)]))
    # print(len(list1))
    return np.array(list1[0:(len(list1))])


# text = "samsung"
# fullTextSearch(text)