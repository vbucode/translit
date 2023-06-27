# ISO 9:1995, ГОСТ 7.79-2000 Система Б
symbols = {"a":"а", "b":"б", "v":"в", "g":"г", "d":"д", "e":"е",
           "yo":"ё", "zh":"ж", "z":"з", "i":"и", "j":"й", "k":"к",
           "l":"л", "m":"м", "n":"н", "o":"о", "p":"п", "r":"р",
           "s":"с", "t":"т", "u":"у", "f":"ф", "x":"х", "cz":"ц",
           "ch":"ч", "sh":"ш", "shh":"щ", "``":"ъ", "y`":"ы", "`":"ь",
           "e`":"э", "yu":"ю", "ya":"я", "-":"-"}


class Translit:
    
    """класс для транслитерации"""
    def __init__(self):
        pass

    def convertcyrillic(self, text):
        """транслитерация в латиницу"""
        tlist = []
        for i in text:
            strtranslit = ""
            if type(i) == str:
                for j in i:
                    c = 0
                    for k, l in symbols.items():
                        c += 1
                        if l == j:
                            strtranslit += k
                            break
                        if c == len(symbols.items()):
                            strtranslit += j
                            break
                tlist.append(strtranslit)
            else:
                tlist.append(i)
        return tlist

    def convertlatin(self, text):
        """транслитерация в кириллицу"""
        ulist = []
        ngram = 3
        memo = " "

        def fngrams(text, ngrams):
            """ function to make n-grams"""
            nlist = []
            for i in text:
                wlist = []
                if type(i) == str:
                    for x, j in enumerate(i):
                        trlist = []
                        tc = ""
                        for k in range(ngrams):
                            if k == 0:
                                tc = str(i[x + k])
                            elif k > 0:
                                try:
                                    tc += str(i[x + k])
                                except IndexError:
                                    break
                            trlist.append(tc)
                        wlist.append(trlist)
                    nlist.append(wlist)
                else:
                    nlist.append(i)
            return nlist

        ngtext = fngrams(text, ngram)

        for x, i in enumerate(ngtext):
            if type(i) != int:
                stranslit = ""
                for j in i:
                    for x, k in enumerate(j[::-1]):
                        if memo == " ":
                            if k in symbols.keys():
                                stranslit += symbols[k]
                                memo = k
                                break
                        else:
                            if memo[-1] != k or len(memo) == 1:
                                if k in symbols.keys():
                                    stranslit += symbols[k]
                                    memo = k
                                    break
                ulist.append(stranslit)
            else:
                ulist.append(i)
        return ulist
