LIST = ['cactus', 'pulse', 'giant', 'pizza', 'give', 'urban', 'shoot', 'hen', 'cheese', 'express', 'sing']

with open("passwords.txt",'a') as passwords:
    with open("words.txt", 'r') as words:
        lines = words.readlines()
        for line in lines:
            for i in range(12):
                p = LIST.copy()
                p.insert(i,line.strip())
                passwords.write(' '.join(p)+'\n')
