# Scopus to CSV

When making a search in Scopus the CSV file produces is a mess and excell cannot read it properly. 

Find in ```example_csv.csv``` what scopus produce when retrieving two searches. When uplading that file to escell the collums and the content is not properly devided.

The desired output can be find in ```example_csv_manualdofiy.csv``` in where I manyúally changed the , that separed the different rown by ;

In the ```scopus_to_csv.py``` you can find a python code I created to automatically do that change so it looks flawless in excel.

This is the first time I use regex to do this kind of selection! I found it extremely difficult but satifiying!