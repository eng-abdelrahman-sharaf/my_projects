import datetime as dt

today = dt.date.today()

def get_birthday():
    user_birth = input("enter your date of birth in the format (yy mm dd):")
    try:
        return [int(i) for i in user_birth.split()]
    except ValueError:
        print("enter valid date")
        # it is important for while condition
        return []
while (len(user_birth:=get_birthday()) !=3):
    pass


user_birth = dt.date(user_birth[0] , user_birth[1] , user_birth[2])

age_days = (today  -  user_birth).days
print(f"your age is nearly : {age_days // 365}y {age_days % 365 // 30}m {age_days % 365 % 30}d")