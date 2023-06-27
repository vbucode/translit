# translit

transliteration from latin to cyrillic 

from words import Words
from translit import Translit

with open("data.txt", "r") as file:
    text = file.read()

# tokenize to words
tokword = Words(text)
tokwordl = tokword.load()

#transliteration from cyriilic to latin
tr = Translit()
ltr = tr.convertcyrillic(tokwordl)
print("\ntransliteration from cyrillic to latin:\n", ltr)

#transliteration from latin to cyrillic
trtonorm = Translit()
nor = trtonorm.convertlatin(ltr)
print("\ntransliteration from latin to cyrillic:\n", nor)
