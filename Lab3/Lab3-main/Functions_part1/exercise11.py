def palindrom_or_not(word):
    if word[-1::-1]==word[0:]:
     print("True")
    else:
     print("False")



word=input()
palindrom_or_not(word)