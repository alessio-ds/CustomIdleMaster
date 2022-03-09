from subprocess import Popen

lista=[]
appid='#'
cont=1
print("\nEnter your game's AppID (Up to 32 games simultaneously)\nPress ENTER to start\n\n")
while appid!='':
    appid=input(f'{cont}. AppID: ')
    cont+=1
    lista.append(appid)
print('Starting')
lista.pop(-1)

for g in lista:
    Popen(f'steam-idle.exe {g}', shell=True, stdin=None, stdout=None, stderr=None, close_fds=True)