from words import Words
from translit import Translit

with open("data.txt", "r") as file:
    text = file.read()

# tokenize to words
tokword = Words(text)
tokwordl = tokword.load()

#transliteration to cyrillic
tr = Translit(tokwordl)
ltr = tr.load()
print("\ntransliteration to cyrillic:\n", ltr)

#transliteration from cyrillic to latin
trtonorm = Translit(ltr)
nor = trtonorm.upload()
print("\ntransliteration from cyrillic to latin:\n", nor)
