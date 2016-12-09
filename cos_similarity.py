import numpy as np
import pandas as pd
from numpy import ndarray
from math import *
import matplotlib.pyplot as plt

#Consoles name
console_a = 'Wii'
console_b = 'PS3'

#Read data from csv file
df = pd.read_csv('vgsales.csv')

genreList = ['Sports','Platform','Racing','Role-Playing','Puzzle','Misc','Shooter',
'Simulation','Action','Fighting','Adventure','Strategy']

print('This application tries to analyze the similarity among makets of different ',
'video game consoles')
print('Game genre in the data: ',genreList)

#Print the top 10 best-selling game on the console
print('Top 10 best-selling game on', console_a)
dataset_1 = df.loc[df['Platform'] == console_a]
print(dataset_1.head(10),'\n')

#Print the top 10 best-selling game on the console
print('Top 10 best-selling game on ',console_b)
dataset_2 = df.loc[df['Platform'] == console_b]
print(dataset_2.head(10),'\n')

#Generate the list of sales data which is ordered by genre
def dataBuilder_1():
    salesList_1 = ndarray((len(genreList),),float)

    for x in range (0,len(genreList)):
        salesTemp = dataset_1.loc[dataset_1['Genre'] == genreList[x]]['Global_Sales'].sum()
        salesList_1[x] = salesTemp

    print('Sales data of',console_a,' by genre: ',salesList_1,'\n')
    return salesList_1

#Generate the list of sales data which is ordered by genre
def dataBuilder_2():
    salesList_2 = ndarray((len(genreList),),float)

    for x in range (0,len(genreList)):
        salesTemp = dataset_2.loc[dataset_2['Genre'] == genreList[x]]['Global_Sales'].sum()
        salesList_2[x] = salesTemp

    print('Sales data of',console_b,' by genre: ',salesList_2,'\n')
    return salesList_2

set_1 = dataBuilder_1()
set_2 = dataBuilder_2()

#Use cosine similarity to calculate the sales data between two consoles
def cosine_similarity(x,y):
    numerator = sum(a * b for (a,b) in zip(x,y))
    denominator = round(sqrt(sum(a * a for a in x)) * sqrt(sum(b * b for b in y)),4)
    result = round(numerator / float(denominator),4)
    return result

print('The similarity between ',console_a,'and ',console_b,'is ', cosine_similarity(set_1,set_2))

#Die pie chart of sales data of each console
def pieBuilder(x,y):
    labels = genreList
    sizes = x
    plt.pie(sizes, labels = labels)
    plt.title(y)
    plt.show()

pieBuilder(set_1,console_a)
pieBuilder(set_2,console_b)
