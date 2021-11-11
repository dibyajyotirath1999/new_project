while True:
    a=input("enter a string:")
    for i in a:
        if i==("1","2","3","4","5") in a:
            print("not allowed")
    

        if len(a[0:])>4:
            print("congratulatin u got the result")
            print("the result is:",a[4:])
            break
        elif len(a[0:])==4:
            print("the word has only 4 letters\nso u r not going to get any result")
        
        

        if len(a[0:])<4:
            print("sorry it has less then 4 letters\nplz think a big number")
            print("my name is dibya jyoti rath")
            print(" i am a software aspirant")

