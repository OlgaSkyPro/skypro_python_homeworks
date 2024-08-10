
num=input()
num=int (num)
#print (num)

def fizz_buzz(n):
    x=0
    for x in range (1,n+1):
        #print ("X=",x)
        if x%3==0 and x%5==0:
            print("FizzBuzz")
        else:
            if x%3==0:
                print ("Fizz")
            else:
                if x%5==0:
                    print("Buzz")
                else:
                    print (x)

print ("Rezult")
fizz_buzz (num)

               
        
