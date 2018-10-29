while True:
    try:
        num = int(input("Enter the numbers please\n"))
        print("The number is :" + str(num))
        break
    except ValueError:
        print("Enter the valid number")
    except:
        break
    finally:
        print('You are odd guys')