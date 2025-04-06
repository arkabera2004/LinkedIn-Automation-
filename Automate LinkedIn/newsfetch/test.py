def divide_numbers():
    try:
        # Taking user input
        num1 = float(input("Enter the numerator: "))
        num2 = float(input("Enter the denominator: "))

        # Performing division
        result = num1 / num2

    except ZeroDivisionError:
        print("Error: Cannot divide by zero please change the denominator!")
    
    except ValueError:
        print("Error: Invalid input! Please provide the missing nubers and try again")
    
    else:
        print(f"Result: {result}")

    finally:
        print("Execution completed.")

# Run the function
divide_numbers()



# num1 = float(input("Enter the numerator: "))
# num2 = float(input("Enter the denominator: "))

# # Performing division
# result = num1 / num2
# print(result)