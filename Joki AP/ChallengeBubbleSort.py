#Soal 1
##kalimat = input("Kalimat : ")
##kata = kalimat.split()
##
##for i in range(len(kata)):
##    for j in range(i+1,len(kata)):
##        if (len(kata[i])>len(kata[j])):
##            kata[i],kata[j]=kata[j],kata[i]
##        elif (len(kata[i])==len(kata[j])):
##            if (kata[i]>kata[j]):
##                kata[i],kata[j]=kata[j],kata[i]
##
##for i in range(len(kata)):
##    print(kata[i],end=" ")

##def count_vowels(kata):
##    count=0
##    for i in range(len(kata)):
##        if (kata[i]=="a" or kata[i]=="A"):
##            count+=1
##        elif (kata[i]=="e" or kata[i]=="E"):
##            count+=1
##        elif (kata[i]=="i" or kata[i]=="I"):
##            count+=1
##        elif (kata[i]=="o" or kata[i]=="O"):
##            count+=1
##        elif (kata[i]=="u" or kata[i]=="U"):
##            count+=1
##    return count
##
#Soal 2
##kalimat = input("Kalimat : ")
##kata = kalimat.split()
##
##for i in range(len(kata)):
##    for j in range(i+1,len(kata)):
##        if (count_vowels(kata[i])>count_vowels(kata[j])):
##            kata[i],kata[j]=kata[j],kata[i]
##        elif (count_vowels(kata[i])==count_vowels(kata[j])):
##            if (len(kata[i])>len(kata[j])):
##                kata[i],kata[j]=kata[j],kata[i]
##            elif (len(kata[i])==len(kata[j])):
##                if (kata[i]>kata[j]):
##                    kata[i],kata[j]=kata[j],kata[i]
##
##for i in range(len(kata)):
##    print(kata[i],end=" ")
