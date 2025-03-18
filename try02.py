num_try = 0

while True:
    try:
        num1 = int(input("enter number 1:"))
        num2 = int(input("enter number 2:"))
    
        print(f"{num1} / {num2} = {num1/num2}")

    except ZeroDivisionError as err:
        print("division by zero")
        num_try += 1
    else: 
        print("good job")

    finally:
        with open("try04.txt", "a") as log:
            if input("would you like to continue(y/n: ") == "n":
                log.write(str(num_try))
                break


