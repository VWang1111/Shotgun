import getpass
p1Ammo = 0
p1Shield = False
p1Power = 0
p2Ammo = 0
p2Shield = False
p2Power = 0

def firstPlayerPrompt():
    print "You have " + str(p1Ammo) + " rounds of ammunition. "
    print "Type the ammount of ammo you would like to use or 0 to shield or any other key to reload. "
    print "Press q to quit \n"

def secondPlayerPrompt():
    print "You have " + str(p2Ammo) + " rounds of ammunition. "
    print "Type the ammount of ammo you would like to use or 0 to shield or any other key to reload. "
    print "Press q to quit \n"

while True:
    firstPlayerPrompt()
    ch = getpass.getpass('First player move: ')
    if ch == 'q':
        break;
    if ch.isdigit():
        if ch == 0:
            p1Shield = True
        else:
            if int(ch) <= p1Ammo:
                p1Ammo -= int(ch)
                p1Power = int(ch)
    else:
        p1Ammo += 1

    secondPlayerPrompt()
    ch = getpass.getpass('Second player move: ')
    if ch == 'q':
        break;
    if ch.isdigit():
        if ch == 0:
            p2Shield = True
        else:
            if int(ch) <= p2Ammo:
                p2Ammo -= int(ch)
                p2Power = int(ch)
    else:
        p2Ammo += 1

    if p1Shield or p2Shield:
        p1Shield = False
        p2Shield = False
        p1Power = 0
        p2Power = 0
        continue;

    if p1Power > p2Power:
        print "Player 1 Wins"
        break;
    elif p2Power > p1Power:
        print "Player 2 Wins"
        break;
    elif p2Power == p1Power != 0:
        if p1Ammo > p2Ammo:
            print "Player 1 Wins"
        elif p2Ammo > p1Ammo:
            print "Player 2 Wins"
        else:
            print "Tie"
        break;




