from datetime import date, timedelta

today = date.today()
# print mm yy
today.month
print("\033[41m"+f"{today.month} {today.year}".center(27)+"\033[0m") 

# print days names from sun to sat
print("\033[44msun mon tue wed thu fri sat\033[0m")


day = date(today.year , today.month , 1)


#while day of the month is not sun
while day.weekday() != 6:
    # first_day=- 1
    day -= timedelta(days=1)
# then print first 35 days 
for i in range(42):
    # if  day.month =!= today.month 
    if day.month != today.month:
        # give it a grey color
        color = 248
    # elif the  day = today 
    elif day.day == today.day:
        # give it a red color
        color = 33
    # else
    else:
        # give it a white colour
        color = 230
    print(f"\033[38;5;{color}m{day.day:>3} ", end = '')
    if day.weekday() == 5:
        print("")
    day+= timedelta(days=1)
    # day += 1