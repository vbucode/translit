# ISO 9:1995, ГОСТ 7.79-2000 Система Б
symbols = {"а":"a", "б":"b", "в":"v", "г":"g", "д":"d", "е":"e",
           "ё":"yo", "ж":"zh", "з":"z", "и":"i", "й":"j", "к":"k",
           "л":"l", "м":"m", "н":"n", "о":"o", "п":"p", "р":"r",
           "с":"s", "т":"t", "у":"u", "ф":"f", "х":"x", "ц":"cz",
           "ч":"ch", "ш":"sh", "щ":"shh", "ъ":"``", "ы":"y`", "ь":"`",
           "э":"e`", "ю":"yu", "я":"ya", "-":"-"}

class Translit:
    """класс для транслитерации"""
    def __init__(self, text):
        self.text = text

    def load(self):
        """транслитерация в кириллицу"""
        tlist = []
        for i in self.text:
            strtranslit = ""
            if type(i) == str:
                for j in i:
                    if j in symbols.keys():
                        strtranslit += symbols[j]
                    else:
                        strtranslit += str(j)
                tlist.append(strtranslit)
            else:
                tlist.append(i)
        return tlist

    def upload(self):
        """транслитерация в латиницу"""
        ulist = []
        var = 0
        ngrams = 3
        for i in self.text:
            strtranslit = ""
            if type(i) == str:
                for x, j in enumerate(i):
                    while var > 0:
                        var -= 1
                        break
                    else:
                        trlist = []
                        tc = ""
                        tx = x
                        c = 0
                        for k in range(ngrams):
                            if k == 0:                                  
                                tc = str(i[tx])
                            elif k > 0:
                                try:
                                    tc += str(i[tx])
                                except IndexError:
                                    break
                            trlist.append(tc)
                            tx += 1
                        for l in trlist[::-1]:
                            c += 1
                            for k, v in symbols.items():
                                if v == l:
                                    strtranslit += k
                                    var = len(trlist) - c
                                    break
            else:
                ulist.append(i)
            ulist.append(strtranslit)
        return ulist
