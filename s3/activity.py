
#create a function that will calculate your age
#your year of birth minus the current year
#store it in a variable

def age_calculator(year_of_birth):
    try:
        #converts the year_of_birth to int
        year_of_birth = int(year_of_birth)

        current_year = 2025
        year_of_birth = int(year_of_birth)
        
        birthday = current_year - year_of_birth
        return birthday

    except ValueError:
        print(f"please enter a whole number")


year_of_birth = age_calculator(
    input("enter your birth year: "))

print(f"Your age is: {year_of_birth}")


