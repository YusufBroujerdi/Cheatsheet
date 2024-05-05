with open('log', 'w') as file:
    file.write('')

def log(s):
    with open('log', 'a') as file:
        file.write(str(s) + '\n')

