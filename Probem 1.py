# Dice Game Truth Table
# 1 point per odd number
# 3 points if sum of both dice even
# truth table on paper in notebook

def roll_dice (die1,die2):
    if ((die1%2==0) and (die2%2==0)):
        print ('You get 3 points!')
    elif ((die1%2==1) and (die2%2==1)):
        print ('You get 5 points!')
    elif ((die1%2==1) and (die2%2==0)):
        print ('You get 1 point.')
    elif ((die1%2==0) and (die2%2==1)):
        print ('You get 1 point.')
    else:
        pass

die1=int(input('Roll the first die:'))
die2=int(input('Roll the second die:'))

print (roll_dice(die1,die2))