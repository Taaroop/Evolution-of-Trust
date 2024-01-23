# Evolution of Trust - Population Simulation
import random as r

# Cutoffs

ch_ch = 0 # both cheats
co_ch = 1 # one of them cooperates, other cheats (value given for cooperator)
ch_co = 3 # one of them cheats, other cooperates (value given for cheater)
co_co = 2 # both cooperates

# Strategies


def always_coop(li, fp, cround):
    if li == 0 and fp == 0 and cround == 0:
        return "Always Cooperate"
    return "Cooperate"
    
def always_cheat(li, fp, cround):
    if li == 0 and fp == 0 and cround == 0:
        return "Always Cheat"
    return "Cheat"
    
def copycat(li, fp, cround):
    if li == 0 and fp == 0 and cround == 0:
        return "Copycat"
    if li == []:
        return "Cooperate"
    else:
        return li[len(li)-1]

def grudger(li, fp, cround):
    if li == 0 and fp == 0 and cround == 0:
        return "Grudger"
    if li == []:
        return "Cooperate"
    elif "Cheat" in li:
        return "Cheat"

def random(li, fp, cround):
    if li == 0 and fp == 0 and cround == 0:
        return "Random"
    a = r.randrange(0, 100)
    if a < 50:
        return "Cooperate"
    else:
        return "Cheat"

def detective(li, fp, cround):
    if li == 0 and fp == 0 and cround == 0:
        return "Detective"
    if li == []:
        return "Cooperate"
    elif cround == 2:
        return "Cheat"
    elif cround == 3:
        return "Cooperate"
    elif cround == 4:
        return "Cooperate"
    else:
        if fp == detective:
            incr = 1
        else:
            incr = 0
            
        li_search = []
        for i in range(8+incr, len(li), 2):
            li_search.append(li[i])
        if li_search == [] or "Cheat" not in li_search:
            return always_cheat(li, fp, cround)
        else:
            return copycat(li, fp, cround)

def copykitten(li, fp, cround):
    if li == 0 and fp == 0 and cround == 0:
        return "Copykitten"
    if li == []:
        return "Cooperate"
    else:
        if li[len(li)-1] == "Cheat" and li[len(li)-3] == "Cheat":
            return "Cheat"
        else:
            return "Cooperate"

# My favorite - THE SIMPLETONNN !!!

def simpleton(li, fp, cround):
    if li == 0 and fp == 0 and cround == 0:
        return "Simpleton"
    if li == []:
        return "Cooperate"
    else:
        if li[len(li)-1] == "Cooperate":
            return li[len(li)-2]
        else:
            if li[len(li)-2] == "Cooperate":
                return "Cheat"
            else:
                return "Cooperate"

# Matchmaking function

def match(s1, s2, rounds): # for 'detective' purposes, there will be atleast 10 rounds
    li = []
    score1 = 0
    score2 = 0
    
    for i in range(1, rounds+1):
        m1 = s1(li, s1, i)
        m2 = s2(li, s1, i)
        li.append(m1)
        li.append(m2)
        
        if m1 == "Cheat" and m2 == "Cheat":
            score1 += ch_ch
            score2 += ch_ch
        
        elif m1 == "Cheat" and m2 == "Cooperate":
            score1 += ch_co
            score2 += co_ch
        
        elif m1 == "Cooperate" and m2 == "Cheat":
            score1 += co_ch
            score2 += ch_co
        
        else:
            score1 += co_co
            score2 += co_co
    
    if score1 > score2:
        winner = s1(0, 0, 0)
    elif score2 > score1:
        winner = s2(0, 0, 0)
    else:
        winner = "Tie"
        
    return winner

# Tournament Function
always_cheat = 15
always_coop = 15
copycat = 14
grudger = 10
detective = 20
copykitten = 19
simpleton = 200
pizza_taco = 11
