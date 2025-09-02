def find_vowels(args):
 vowels_num=0
 for alpha in args:
     if alpha=="a" or alpha=="e" or alpha=="o"or alpha=="u"or alpha=="i":
      vowels_num+=1
 return vowels_num

print(find_vowels("Mahan"))

