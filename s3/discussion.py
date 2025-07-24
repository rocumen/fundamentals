#function



#function



def print_name(nickname):
    print(f"Hello {nickname}")



# print_name("reynald")

# def print_something():
#     print("something you print")

# def convert_c_to_f(celcius):
#     print(f"the temperature from c to f is: {(celcius * 9/5) + 32}")

# convert_c_to_f(int(input("Enter Celsius: ")))

# def convert_f_to_c(fahrenheight):
#     print(f"the tem from f to c is: {(fahrenheight * 5/9) - 32}")

# convert_f_to_c(float(input("Enter Fahrenheight")))

#error handler
def compute_grade(grade):
    try:      
        grade = int(grade)

        if grade >= 70 and grade <= 79:
            print("C")
        elif grade >= 80 and grade <= 89:
            print("B")
        elif grade >= 90:
            print("A")

    except ValueError:
        print("Invalid input: Please entere a whole number")

# compute_grade(input("Enter your Grade: "))


def calculator(operation, value1, value2):
    try:
        # if operation != "+" or operation != "-" or operation != "*" or operation != "/":
        #     print("String is not valid operation")
        value1 = int(value1)
        value2 = int(value2)

        if operation == "+":
            print (f"the total sum is: {value1 + value2}")
            return value1 + value2
        elif operation == "-":
            print(f"The difference is: {value1 - value2}")
            return value1 - value2
        elif operation == "*":
            print(f"The product is: {value1 * value2}")
            return value1 * value2
        elif operation == "/":
            print(f"The quotient is: {value1 / value2}")
            return value1 / value2
        else:
            print("Invalid operation")
        
    except ValueError:
        print("Invalid input: Please entere a whole number")


# calculator(
#     input("Enter Operation: "), 
#     input("Enter first Value: "), 
#     input("Enter 2nd Value:")
#     )


calculated_difference = calculator(
    input("Enter Operation: "), 
    input("Enter first Value: "), 
    input("Enter 2nd Value:")
    )

calculated_sum = calculator(
    input("Enter Operation: "), 
    input("Enter first Value: "), 
    input("Enter 2nd Value:")
    )

total = calculated_difference + calculated_sum

print(total)