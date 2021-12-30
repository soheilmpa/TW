from insert_to_form import Insert
from change_mac_address import MAC
from change_ip import IP
from time import sleep


with open("save.txt", 'r') as save:
    start = s = int(save.read())



with open("passwords.txt", 'r') as file:
        passwords = file.readlines()

        for num, password in enumerate(passwords[start:]):
            Insert(password.strip()+'\n')
            print(num)
            # sleep(0.5)

            s+=1
            with open("save.txt", 'w') as save:
                save.write(str(s))

            if num%3==0:
                IP()
            if num%10==0:
                MAC()
                break



