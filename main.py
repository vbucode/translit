from translit import Translit

#transliteration from cyriilic to latin
print("transliteration from cyriilic to latin")
inp = input("Enter words: ")
tr = Translit()
ltr = tr.convertlatin(inp)
print("".join(ltr))
