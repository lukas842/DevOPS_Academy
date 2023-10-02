#n1 = int(input("Write number: "))
#n2 = int(input("Write second number: "))

#result = n1 + n2

#print("The sum of", n1, "and" , n2, "is" , result)

print("This is calculator where you can make operations +, -, x, /")


while True:

    answer = input("Type 'stop' if you want to exit calculator: ")

    if answer.lower() == 'stop':
        break

    else:

        menu = int(input("For + type 1, - type 2, x type 3, / type 4 : "))
        n1 = int(input("Write first number: "))
        n2 = int(input("Write second number: "))

        #Calculator variable
        sum = n1 + n2
        sub = n1 - n2
        multi = n1 * n2
        div = n1 / n2


        if menu == 1:
            print("The sum of", n1, "and" , n2, "is" , sum)

        elif menu == 2:
            print("The sub of", n1, "and" , n2, "is" , sub)

        elif menu == 3:
            print("The multi of", n1, "and" , n2, "is" , multi)

        elif menu == 4:
            print("The div of", n1, "and" , n2, "is" , div)

        else:
            print("You writed wrong number, write only number from 1-4")
