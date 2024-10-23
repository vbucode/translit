
class Translit:
    """transliteration class"""
    def __init__(self):
        # ISO 9:1995, ГОСТ 7.79-2000 Система Б
        self.symbols = {"а":"a", "б":"b", "в":"v", "г":"g", "д":"d", "е":"e",
                        "ё":"yo", "ж":"zh", "з":"z", "и":"i", "й":"j", "к":"k",
                        "л":"l", "м":"m", "н":"n", "о":"o", "п":"p", "р":"r",
                        "с":"s", "т":"t", "у":"u", "ф":"f", "х":"x", "ц":"cz",
                        "ч":"ch", "ш":"sh", "щ":"shh", "ъ":"``", "ы":"y`", "ь":"`",
                        "э":"e`", "ю":"yu", "я":"ya"}

    def convertlatin(self, text):
        """to latin"""
        resultlist = []
        for i in text:
            if type(i) == str:
                if i in self.symbols:
                    resultlist.append(self.symbols[i])
                else:
                    resultlist.append(i)
            else:
                resultlist.append(i)
        return resultlist
