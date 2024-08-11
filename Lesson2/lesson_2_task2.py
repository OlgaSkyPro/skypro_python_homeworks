year_input = input ("Input year:")
year = int (year_input)

#print (leap)
#print (year)
def is_year_leap (y):
        l = "False"
        if y%4==0:
            l="True"
        return(l)

leap = is_year_leap(year)
print("YEAR", year, " ", end='')
print (leap)
