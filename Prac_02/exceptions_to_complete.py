finished = False
result = 0
while not finished:
    try:
        result = int(input("Enter a integer: "))
        finished = True
    except ValueError:
        print("Please enter a integer.")
print("Valid result is:", result)