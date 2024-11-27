def eat_ghost(power_pellet_active, touching_ghost):    
    if power_pellet_active and touching_ghost == True:
        print(True)
    else: 
        print(False)

#eat_ghost(True, True)

def score(touching_power_pellet, touching_dot):
    if touching_dot or touching_power_pellet == True:
        print(True)
    else:
        print(False)

#score(True, False)

def lose (power_pellet_active, touching_ghost):
    if power_pellet_active == False and touching_ghost == True:
        print(True)
    else:
        print(False)
    
#lose(True,False)



def win(has_eaten_all_dots, power_pellet_active, touching_ghost):
    if has_eaten_all_dots == True and power_pellet_active == True and touching_ghost == True:
        print(True)
    if has_eaten_all_dots and power_pellet_active == True and touching_ghost == False:
        print(True)
    else:
        print(False)
    
