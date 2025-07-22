n = int(input(" Enter the number "))
if(n<0):
    print(" Number is negative")
elif(n>=2):
    if(n<=10):
        print("Number is between 3 and 10")
    elif(n>10 and n<=20):
        print("Number is between 11 and 20")
    elif(n<=100):
        print ("Number is addable")    
else:
  print("Number is positive")

