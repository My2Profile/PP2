class string_:
    def getstring(self):
        self.string=input()
    def printstring(self):
        print(self.string.upper())


word=string_()
word.getstring()
word.printstring()