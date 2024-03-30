
class Translit:
    """transliteration class"""
    def __init__(self):
        # ISO 9:1995, ГОСТ 7.79-2000 Система Б
        symbols = {"a":"а", "b":"б", "v":"в", "g":"г", "d":"д", "e":"е",
                   "yo":"ё", "zh":"ж", "z":"з", "i":"и", "j":"й", "k":"к",
                   "l":"л", "m":"м", "n":"н", "o":"о", "p":"п", "r":"р",
                   "s":"с", "t":"т", "u":"у", "f":"ф", "x":"х", "cz":"ц",
                   "ch":"ч", "sh":"ш", "shh":"щ", "``":"ъ", "y`":"ы", "`":"ь",
                   "e`":"э", "yu":"ю", "ya":"я", "-":"-"}
        
        self.symbols = symbols

    def convertlatin(self, text):
        """to latin"""
        resultlist = []
        for i in text:
            if type(i) == str:
                for k, v in self.symbols.items():
                    if v == i:
                        resultlist.append(k)
                        break
                    elif i == " ":
                        resultlist.append(i)
                        break
            else:
                resultlist.append(i)
        return resultlist

    def fngrams(self, text, ngrams):
        """function to make n-grams"""
        resultlist = []
        listtext = text.split(" ")
        for i in listtext:
            if type(i) == str:
                for x, j in enumerate(i):
                    tc = ""
                    trlist = []
                    for k in range(ngrams):
                        if k == 0:
                            tc = str(i[x + k])
                        elif k > 0:
                            try:
                                tc += str(i[x + k])
                            except IndexError:
                                break
                        trlist.append(tc)
                    resultlist.append(trlist)
                resultlist.append(" ")
            else:
                trlist.append(i)
                resultlist.append(trlist)
        return resultlist

    def convertcyrillic(self, text):
        """to cyrillic"""
        resultlist = []
        ngrams = 3
        ngtext = self.fngrams(text, ngrams)
        for i in ngtext:
            if i == " ":
                resultlist.append(i)
            else:
                for x, k in enumerate(i[::-1]):
                    if k in self.symbols.keys():
                        resultlist.append(self.symbols[k])
                        break
        return resultlist
