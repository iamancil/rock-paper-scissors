import random, pprint

options = {0:"Rock",1:"Paper",2:"Scissors",0:"Stop"}

ans = random.choice(options)

print("1:Rock \n 2: Paper \n 3: Scissors \n 0: Stop")

try:

    is_running = True

    while is_running:

        choice = int(input("Enter your choice of number:"))

        choice -= 1

        if choice == -1:

            is_running = False

            break

        elif ans == choice:

            print("It turned out to be draw..XD!")

        elif choice >2:

            print("Enter value from the list")

        else:

            if ans == 0:

                if choice == 1:

                    print("You won to Rock")
                
                else:

                    print("You lost to Rock")
            
            elif ans == 1:

                if choice == 0:

                    print("You lost to Paper")

                else:

                    print("You won to Paper")

            else:

                if choice == 1:

                    print("You won to Scissors")

                else:

                    print("You lost to Scissors")

except:

    print("Ivalid Input!")
