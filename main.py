from translit import Translit

#transliteration from cyriilic to latin
print("transliteration from cyriilic to latin")
inp = input("Enter words: ")
tr = Translit()
ltr = tr.convertlatin(inp)
print("\ntransliteration from cyrillic to latin:\n", ltr)

#transliteration from latin to cyriilic
print("\ntransliteration from latin to cyriilic")
inp2 = input("Enter words: ")
tr2 = Translit()
ltr2 = tr.convertcyrillic(inp2)
print("\ntransliteration from latin to cyrillic:\n", ltr2)
