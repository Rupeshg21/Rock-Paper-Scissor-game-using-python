import random
def is_win(player,opponent):
    if(player=='r' and opponent=='s')or(player=='s'and opponent=='p')or(player=='p'and opponent=='r'):
        return True
def play():
    while True:
        user=input("what's your choice 'r' for rock ,'p' for paper,'s' for scissor :")
        computer=random.choice(['r','p','s'])
        if user==computer:
            print('its tie..')
        elif is_win(user,computer):
            print('you won')
            break
        else:
            print('you lost try again..')
play()
