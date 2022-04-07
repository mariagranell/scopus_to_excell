# Scopus to CSV

A normal database on which to search literature articles is Scopus. This is a powerful website where is possible to save the matches of your querries and export them in different formats. In this way, you can organize and skim through articles in a systematic way.

However, the CSV file produced by Scopus is not well-read in excel. Collums and rows are not properly recognized by the software. The main problem is the overuse of commas within the text. Thus, the best way is to separate the text into semicolons. This requires a little change in format that can be solved with this piece of code.

For this literature search I asked Scopus to extract:

* Author(s)
* Title
* Year
* DOI
* Abstrackt
* Key words

Find in ```example_csv.csv``` what Scopus produce when retrieving two articles.

The desired output can be found in ```example_csv_manualdofiy.csv``` where I manually changed the commas that separate the different rows by semicolons.

In the ```scopus_to_csv.py``` you can find a python code I created to automatically do that change so it looks flawless in excel.

This is the first time I use regex to do this kind of selection! I found it extremely difficult but satisfying! The output file that can be smoothly read in excel is called ```output_file.csv```