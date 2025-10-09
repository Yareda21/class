given = input("Enter the given temprature: ")
con = input(" To 1. C\n"
            "    2. F\n"
            "    3. K\n")
temp = ["C","F","K"]
for index in range(len(given)):
    if given[index] in temp:

        form = given[index]
        num = int(given[:index])

        if given[index] == "C":
            if con == "F":
                print("Ans",(9/5)*num+32)
            elif con == "K":
                print("Ans",num + 273)
            elif con == "C":
                print("Ans",num)
            else:
                print("You have entered incorrect key")
                break
        elif given[index] == "F":
            if con == "C":
                print("Ans",(5/9)*(num-32))
            elif con == "K":
                print("Ans",((9/5)*num+32)+273)
            elif con == "F":
                print("Ans",num)
            else:
                print("You have entered incorrect key")
                break
        elif given[index] == "K":
            if con == "C":
                print("Ans",num-273)
            elif con == "F":
                print("Ans",(5/9)*((num-273)-32))
            elif con == "K":
                print("Ans",num)
            else:
                print("You have entered incorrect key")