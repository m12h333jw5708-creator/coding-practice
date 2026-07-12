while True:
    try:
        n = int(input("enter a number:"))
        if n % 2 == 0:
            print("even")
            break
        elif n % 2 == 1:
            print("odd")
            break
    except ValueError:
        print("error")