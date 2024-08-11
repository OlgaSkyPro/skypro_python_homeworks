invest=input ("SIZE OF INVEST:")
period=input ("DEPOSITE TERM: ")
invest=int(invest)
period=int(period)

def bank (x,y):
    sum=x
    for i in range (1,y+1):
        sum=sum+sum*0.1
        #print("sum", sum)
    return (sum)
   
s= bank(invest, period)
print ("TOTAL SUMMA=", s)