with open('Test2.txt', 'r') as file:
    File = file.read().split()

    for i in range(len(File)):
        word=File[i]
        BadLetters = 0
        vowel=0
        GoodLetters=0
        for j in word:

            if (j=="a" or j=="e" or j=="i" or j=="o" or j=="u" or j=="y"):
                vowel+=1
            else:
                if (j=="f" or j=="c" or j=="k" or j=="r"):
                    BadLetters+=1
                else:
                    GoodLetters+=1
        LenWord=len(File[i])-vowel
        print("H leksi einai:<",File[i],">apoteleitai apo:",LenWord,"simfona ta opoia:",GoodLetters,"einai ta kala kai:",BadLetters,"einai ta kaka ara bgainei to apotelesma:")
        if (BadLetters>GoodLetters):
            print ("Kakia leksi")
        elif (BadLetters==GoodLetters):
            print ("Kakia leksi")
        else:
            print ("Kali leksi")
        print("\n")
