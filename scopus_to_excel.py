# This is a code to transform a txt file from a scopus search into a legible csv file.

# this is to import usual charachters or basics
import re
import os
#os.getcwd() #code for check in witch dir I was
#os.chdir('C:/Users/mariagranell/Desktop') #code to change dir


# open file to read
f = open('example_csv.csv', 'r')
data = f.readlines() #read the lines

# to put the data in a list
dat = []
counter = 0
for line in data:
    line = line.strip()
    dat.append(line)
    counter += 1
    if counter > len(data):
        break


# change the frist rows , for ;
dat[0] = dat[0].replace(',',';')

play = '"Kohlhoff, V.","Oxytocin, review",2022,"10.1016","https";"This , pro-© 2022 Elsevier Ltd","Adolescent; Behavior"'
new_character = ';'
counter = 0
number_of_comillas = 0
n_comas = 0
for character in play:
    if character == '"':
        number_of_comillas += 1
    if number_of_comillas = 2:
        n_comas += 1
        number_of_comillas = 0
    if character == ',':
        play = play[:counter] + new_character + play[counter+1:]
    counter += 1

print(play)

