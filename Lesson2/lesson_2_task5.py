num=input()
num=int (num)

def month_to_season(n):
    if n==12 or n==1 or n==2:
        season = "WINTER"
    elif n==3 or n==4 or n==5:
        season = "SPRING"
    elif n==6 or n==7 or n==8:
        season = "SUMMER"
    else:
        season = "AUTUMN"
    return (season)

season_rezult = month_to_season(num)
print(season_rezult)