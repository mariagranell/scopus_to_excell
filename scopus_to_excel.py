#This is a code to transform a txt file from a scopus search into a legible csv file.

#this is to be able to use regex expressions
import re

#this is my first time using regex! website: https://regex101.com/
#this is the expression that i used: (?<=\")(,)(?=\")|(?<=\")(,)(?=\d)|(?<=\d)(,)(?=\")
#(?<=\")(,)(?=\") this matches characters between a " and a " that is are ,
#(?<=\")(,)(?=\d) this matches characters between a " and a number that is are ,
#(?<=\d)(,)(?=\") this matches characters between a number and a " that is are ,
#to put them all together you can to use |

# open file to read
f = open('example_csv.csv', 'r')
data = f.readlines() #read the lines

#to put the data in a list and apply the regex command
dat = []
COUNTER = 0
for line in data:
    #separates the lines
    line = line.strip()
    #the next line replaces the matches in the regex code for ; for each line
    line = re.sub('(?<=\")(,)(?=\")|(?<=\")(,)(?=\d)|(?<=\d)(,)(?=\")', ';', line)
    #puts the lines together
    dat.append(line)
    COUNTER += 1
    if COUNTER > len(data):
        break

#change the frist rows , for ;
dat[0] = dat[0].replace(',',';')

#funtion for exporting a list into a csv file, each item into a row
def write_to_csv(example_file):
    with open('output_file.csv', 'w') as csvfile:
        for domain in example_file:
            csvfile.write(domain + '\n')

#export dat into a csv file
write_to_csv(dat)
