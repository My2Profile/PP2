def reverse_string(word):
    word2=word.split()
    word2.reverse()
    print(word,"->",str(word2).replace("[","").replace("]","").replace(",","").replace("'",""))
    

word=input()
reverse_string(word)
