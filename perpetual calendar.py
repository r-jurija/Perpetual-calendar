#Perpetual calendar
def script():
    print("Insert a date in the format dd mm yyyy:")
    print("(Only for dates after 15 October 1582 and before 31 December 2399 (included))")


    gg, mm, ssaa = map(int,input().split())

    str_ssaa = str(ssaa)
    str_ss = str_ssaa[0:2]
    str_aa = str_ssaa[2:4]

    
    ss = int(str_ss)
    aa = int(str_aa)

    print_date = f"{gg}/{mm}/{ss}{aa}"


    #Define G
    G = gg%7

    #Define M
    if mm == 1:
        M = 6

    elif mm == 2:
        M = 2

    elif mm == 3:
        M = 2

    elif mm == 4:
        M = 5

    elif mm == 5:
        M = 0

    elif mm == 6:
        M = 3

    elif mm == 7:
        M = 5

    elif mm == 8:
        M = 1

    elif mm == 9:
        M = 4

    elif mm == 10:
        M = 6

    elif mm == 11:
        M = 2

    elif mm == 12:
        M = 4

    #Define S

    if ss == 15:
        S = 1

    elif ss == 16:
        S = 0

    elif ss == 17:
        S = 5

    elif ss == 18:
        S = 3

    elif ss == 19:
        S = 1

    elif ss == 20:
        S = 0

    elif ss == 21:
        S = 5

    elif ss == 22:
        S = 3

    elif ss == 23:
        S = 1


    A = aa%28
    B = int(aa%28/4)

    if mm == 1 or mm == 2 and ss%4:
        M = mm - 1


    def Sum():
        Sum = (G + M + S + A + B)%7

        if Sum == 0:
            print("Sunday")

        elif Sum == 1:
            print("Monday")

        elif Sum == 2:
            print("Tuesday")

        elif Sum == 3:
            print("Wednesday")

        elif Sum == 4:
            print("Thursday")

        elif Sum == 5:
            print("Friday")

        elif Sum == 6:
            print("Saturday")

    #Handling exceptions
    if gg < 15 and mm <= 10 and ss <= 15 and aa <= 82:
        print("Insert a date before 15 October 1582")

    elif gg == 29 and mm == 2 or mm > 12 and aa%4 > 0:
        print("This date does not exist!")

    elif gg == 30 or gg == 31 and mm == 2:
        print("This date does not exist!")

    elif gg == 31 and mm == 11 or gg == 31 and mm == 4 or gg == 31 and mm == 6 or gg == 31 and mm == 9:
        print("This date does not exist!")

    else:
        print(print_date)
        Sum()


    restart = input("Would you like to restart this program? y/n" "\n")
    if restart == "yes" or restart == "y":
                    print("\n")
                    script()
    elif restart == "no" or restart == "n":
        print("Script terminating. Goodbye.")

script()
















