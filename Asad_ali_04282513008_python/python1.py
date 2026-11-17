str = input("enter the string: ")
length = len(str)
vowels =0
for i in range (0,length):
    if ((str[i] == 'a') or (str[i]=='e') or (str[i]=='i') or (str[i]=='o') or (str[i]=='u')):
        vowels=vowels+1
    elif ( (str[i] == 'A') or (str[i]=='E') or (str[i]=='I') or (str[i]=='O') or (str[i]=='O')):
        vowels = vowels +1
print ("The number of vowels is: ", vowels)
