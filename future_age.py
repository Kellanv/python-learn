current_date = input("Enter the today's date in mm/yyyy format: ")
birthday = input("Enter the your birthday in mm/yyyy format: ")
future_date = input("Enter the future date you would like to know your age on in mm/yyyy format: ")


def find_year(date):
    return (date[3]) + (date[4]) + (date[5]) + (date[6])


current_year = find_year(current_date)
birthday_year = find_year(birthday)
future_year = find_year(future_date)


def month(datev):
    return (datev[0]) + (datev[1])


current_month = month(current_date)
birthday_month = month(birthday)
future_month = month(future_date)


def zero_delete(monthv):
    str(monthv.startswith("0"))

    if monthv is True:
        return (monthv[1])
    else:
        return monthv
  

newc_month = zero_delete(current_month)
newb_month = zero_delete(birthday_month)
newf_month = zero_delete(future_month)

possible_age = int(current_year) - int(birthday_year)
month_calc1 = int(newc_month) - int(newb_month)

if month_calc1 < 0:
    real_age = int(possible_age) + 1
else:
    real_age = int(possible_age)

possible_added_age = int(future_year) - int(current_year)
month_calc2 = int(newf_month) - int(newc_month)

if month_calc2 > 0:
    added_age = int(possible_added_age) + 1
else:
    added_age = int(possible_added_age)

future_age = int(added_age) + int(real_age)

if int(newf_month) == 1:
    print_month = "January"
elif int(newf_month) == 2:
    print_month = "February"
elif int(newf_month) == 3:
    print_month = "March"
elif int(newf_month) == 4:
    print_month = "April"
elif int(newf_month) == 5:
    print_month = "May"
elif int(newf_month) == 6:
    print_month = "June"
elif int(newf_month) == 7:
    print_month = "July"
elif int(newf_month) == 8:
    print_month = "August"
elif int(newf_month) == 9:
    print_month = "September"
elif int(newf_month) == 10:
    print_month = "October"
elif int(newf_month) == 11:
    print_month = "November"
elif int(newf_month) == 12:
    print_month = "December"
else:
    print_month = "Invalid month"

print("Currently you are " + str(real_age) + " years old.")
print("In " + print_month + " " + str(future_year) + ", " + "you will be " + str(future_age) + " years old.")