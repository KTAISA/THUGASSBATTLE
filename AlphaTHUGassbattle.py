__author__ = 'JAWASSMACPRO'
#Thug Ass Battle - By Bitch Ass Jaw Mother - 11/8/13

import random, sys

def wordGrabLooper(numWords):
    dictionaryFile = open('thugassbattleDICT.txt')
    englishWords = []
    for word in dictionaryFile.read().split('\n'):
        englishWords.insert(1, word)
    random.shuffle(englishWords)

    finalLIST = []
    #print('got here')
    for i in range(numWords):
        pickedWORD = englishWords[i]
        finalLIST.insert(i, pickedWORD)
        #print(pickedWORD)
    #print(finalLIST)
    return(finalLIST)

def diceRoll():
    roll = random.randint(1,20)
    return(roll)

def equipPLAYER():
    ###### equipment sketch pad
    """

    equipment = [armor, weapon]
    armor = [helm, chest, leggings]
    helm = ['crazy ass helm', armor rate]
    weapon = [sword]
    sword ['crazy ass sword', attack rate]

    """

    crazyHELM = ['Crazy Ass Helm', 13]
    shittyHELM = ['Dir Ass Shi Ass Helm', 9]
    JAWHELM = ['Straight pimpin Ultima Helmet', 20]

    HELMS = [crazyHELM, shittyHELM, JAWHELM]

    crazyCHEST = ['Crazy Ass Chest Plate', 17]
    shittyCHEST = ['Dir Ass Shi Ass Chest thang', 11]
    JAWCHEST = ['Straight pimpin Ultima Jacket', 30]

    CHESTS = [crazyCHEST, shittyCHEST, JAWCHEST]

    crazyLEGS = ['Crazy Ass leg armor', 16]
    shittyLEGS = ['Dir Ass Shi Ass Women Stockings', 2]
    JAWLEGS = ['Straight pimpin Ultima Slacks from Thom Browne', 50]

    LEGS = [crazyLEGS, shittyLEGS, JAWLEGS]

    helm = random.choice(HELMS)
    chest = random.choice(CHESTS)
    legs = random.choice(LEGS)

    ARMOR = []

    ARMOR.insert(0, helm)
    ARMOR.insert(1, chest)
    ARMOR.insert(2, legs)

    crazySWORD = ['Crazy fucking sword', 13]
    shittyCLUB = ['Shitty Ass club thang', 9]
    JAWGLOCK = ['Badass fucking GLOCK but only for PISTOL WHIPPING', 19]
    legendMACE = ['DUUUDE FUCKING LEGENDARY MACE', 28]


    WEAPONS = [crazySWORD, shittyCLUB, JAWGLOCK, legendMACE]

    weapon = random.choice(WEAPONS)

    EQUIPMENT = []

    EQUIPMENT.insert(0, ARMOR)
    EQUIPMENT.insert(1, weapon)

    return(EQUIPMENT)

def configAI(EQUIPMENT):
    AIplayer = []
    AIhp = 100
    attackRATE = 50
    armorRATE = 50
    weaponAttack = EQUIPMENT[1][1]
    helm = EQUIPMENT[0][0][1]
    chest = EQUIPMENT[0][1][1]
    legs = EQUIPMENT[0][2][1]
    totalATTACK = attackRATE + weaponAttack
    totalARMOR = armorRATE + helm + chest + legs

    AIplayer.insert(0, AIhp)
    AIplayer.insert(1, totalATTACK)
    AIplayer.insert(2, totalARMOR)
    #print(AIplayer)
    return(AIplayer)

def configPC(EQUIPMENT):
    #player stats [hps, attack rate, armor rate]
    PCplayer = []
    PChp = 100
    attackRATE = 50
    armorRATE = 50
    weaponAttack = EQUIPMENT[1][1]
    helm = EQUIPMENT[0][0][1]
    chest = EQUIPMENT[0][1][1]
    legs = EQUIPMENT[0][2][1]
    totalATTACK = attackRATE + weaponAttack
    totalARMOR = armorRATE + helm + chest + legs

    PCplayer.insert(0, PChp)
    PCplayer.insert(1, totalATTACK)
    PCplayer.insert(2, totalARMOR)
    #print(PCplayer)
    return(PCplayer)

def displayPCequip(EQUIPMENT, PCplayer):
    # equipment = [armor, weapon]
    # playerstats = [hp, attack, armor]
    print('Want to see Jaw equipment')
    print('Jaw weapon is: {}' .format(EQUIPMENT[1][0]))
    print('Weapon Attack Power: {}' .format(EQUIPMENT[1][1]))
    print('JAW wearing {}, {}, & {}' .format(EQUIPMENT[0][0][0], EQUIPMENT[0][1][0], EQUIPMENT[0][2][0]))
    print('{} adds {} Defense' .format(EQUIPMENT[0][0][0], EQUIPMENT[0][0][1]))
    print('{} adds {} Defense' .format(EQUIPMENT[0][1][0], EQUIPMENT[0][1][1]))
    print('{} adds {} Defense' .format(EQUIPMENT[0][2][0], EQUIPMENT[0][2][1]))
    print('')
    print('JAW player stats be')
    print('JAW HPS: {}' .format(PCplayer[0]))
    print('JAW Attack Rating: {}' .format(PCplayer[1]))
    print('JAW Armor is: {}' .format(PCplayer[2]))
    print('')

def displayAIequip(EQUIPMENT, AIplayer):
    # equipment = [armor, weapon]
    # stats = [hp, attack, armor]
    print('Peeping Fool ass enemy equipment')
    print('Dudes weapon be: {}' .format(EQUIPMENT[1][0]))
    print('His Weapon Attack Power: {}' .format(EQUIPMENT[1][1]))
    print('Sporting {}, {}, & {}' .format(EQUIPMENT[0][0][0], EQUIPMENT[0][1][0], EQUIPMENT[0][2][0]))
    print('{} adds {} Defense' .format(EQUIPMENT[0][0][0], EQUIPMENT[0][0][1]))
    print('{} adds {} Defense' .format(EQUIPMENT[0][1][0], EQUIPMENT[0][1][1]))
    print('{} adds {} Defense' .format(EQUIPMENT[0][2][0], EQUIPMENT[0][2][1]))
    print('')
    print('Dude stats be')
    print('Fool ASS HPS: {}' .format(AIplayer[0]))
    print('HIS Attack Rating: {}' .format(AIplayer[1]))
    print('HIS Armor is: {}' .format(AIplayer[2]))
    print('')

def attack(attackRATE):
    #example user move ['attack', 'attack description', attack damage]
    roll = diceRoll()
    finalROLL = ['Attack']
    if roll == 1:
        finalROLL.insert(1, 'Big ass Miss')
        finalROLL.insert(2, 0)
        return(finalROLL)
    if roll >= 2 and roll <= 10:
        finalROLL.insert(1, 'Decent hit')
        finalROLL.insert(2, int(((attackRATE * .2) + roll)))
        return(finalROLL)
    if roll >= 11 and roll <= 17:
        finalROLL.insert(1, 'HIIIIIIITTTTTT')
        finalROLL.insert(2, int(((attackRATE * .4) + roll)))
        return(finalROLL)
    if roll >= 18:
        finalROLL.insert(1, 'MASSSSIVE ASS HIT')
        finalROLL.insert(2, int(((attackRATE * .6) + roll)))
        return(finalROLL)

def block(armorRATE):
    roll = diceRoll()
    finalROLL = ['Block']
    if roll == 1:
        finalROLL.insert(1, 'Jaw missed jaw block')
        finalROLL.insert(2, 0)
        return(finalROLL)
    if roll >= 2 and roll <= 10:
        finalROLL.insert(1, 'Mild ass block')
        finalROLL.insert(2, int(((armorRATE * .4) + roll)))
        return(finalROLL)
    if roll >= 11 and roll <= 17:
        finalROLL.insert(1, 'Medium BLOCK')
        finalROLL.insert(2, int(((armorRATE * .8) + roll)))
        return(finalROLL)
    if roll >= 18:
        finalROLL.insert(1, 'JAW did MASSIVE BLOCK')
        finalROLL.insert(2, int(((armorRATE * 1.2) + roll)))
        return(finalROLL)

def HEAL():
    roll1 = diceRoll()
    roll2 = diceRoll()
    heal = ((roll1 + roll2) * 2)
    #print(heal)
    return(heal)

def corpPOR():
    spell = ['Spell', 'Corp Por']
    roll1 = int(diceRoll())
    #print(roll1)
    roll2 = int(diceRoll())
    #print(roll2)
    finaldamage = (roll1 + ((roll2 * 3)/2))
    spell.insert(2, finaldamage)
    #print(spell)
    return(spell)

def armorWEAK():
    spell = ['Spell', 'JAW weak ass Armor nah']
    roll1 = int(diceRoll())
    #print(roll1)
    finaldmg = (roll1 + ((roll1 * 2)/2))
    spell.insert(2, finaldmg)
    #print(spell)
    return(spell)

def armorBUFF():
    spell = ['Spell', 'ARMOR BUFF ME']
    roll = int(diceRoll())
    #print(roll)
    finaldmg = (roll + (roll + (roll + 20)/2))
    spell.insert(2, finaldmg)
    #print(spell)
    return(spell)

def attackBUFF():
    spell = ['Spell', 'Buff my Attack']
    roll = int(diceRoll())
    #print(roll)
    finalbuff = (roll + ((roll * 3)/2) + 5)
    spell.insert(2, finalbuff)
    #print(spell)
    return(spell)

def SPELL():
    print('What Spell you wanna cast?')
    print('D - Corp Por')
    print('W - Armor Weaken')
    print('A - Armor Buff')
    print('K - Attack buff')
    spellCHOICE = input(str('Spell: '))
    spellCHOICE = spellCHOICE.upper()
    if spellCHOICE == 'D':
        spell = corpPOR()
        return(spell)
    if spellCHOICE == 'W':
        spell = armorWEAK()
        return(spell)
    if spellCHOICE == 'A':
        spell = armorBUFF()
        return(spell)
    if spellCHOICE == 'K':
        spell = attackBUFF()
        return(spell)

def aiSPELLsetUP(spellCHOICE):
    #print(spellCHOICE)

    if spellCHOICE == 'D':
        spell = corpPOR()
        return(spell)
    if spellCHOICE == 'W':
        spell = armorWEAK()
        return(spell)
    if spellCHOICE == 'A':
        spell = armorBUFF()
        return(spell)
    if spellCHOICE == 'K':
        spell = attackBUFF()
        return(spell)

def aiSPELLchoice(PCplayer, AIplayer):

    # DECISIONS FOR LOWER THAN PC
    if PCplayer[0] and AIplayer[0] == 100:
        choose = ['D', 'D', 'K', 'A', 'D', 'K', 'A', 'D']
        spellCHOICE = random.choice(choose)
        spell = aiSPELLsetUP(spellCHOICE)
        #print(spell)
        return(spell)
    if PCplayer[0] >= AIplayer[0] and AIplayer[0] > 65:
        choose = ['D', 'K', 'A', 'K','W', 'D', 'D', 'A']
        spellCHOICE = random.choice(choose)
        spell = aiSPELLsetUP(spellCHOICE)
        #print(spell)
        return(spell)
    if PCplayer[0] >= AIplayer[0] and AIplayer[0] > 45:
        choose = ['A' , 'D', 'A', 'A']
        spellCHOICE = random.choice(choose)
        spell = aiSPELLsetUP(spellCHOICE)
        #print(spell)
        return(spell)
    if PCplayer[0] >= AIplayer[0] and AIplayer[0] <= 45:
        choose = ['A', 'A', 'A', 'D']
        spellCHOICE = random.choice(choose)
        spell = aiSPELLsetUP(spellCHOICE)
        #print(spell)
        return(spell)
    #DECISIONS FOR HIGHER HPS THAN PC
    if PCplayer[0] <= AIplayer[0] and AIplayer[0] > 65:
        choose = ['A', 'W', 'D', 'D', 'K', 'W', 'A']
        spellCHOICE = random.choice(choose)
        spell = aiSPELLsetUP(spellCHOICE)
        #print(spell)
        return(spell)
    if PCplayer[0] <= AIplayer[0] and AIplayer[0] > 45:
        choose = ['A', 'D', 'K', 'A', 'D']
        spellCHOICE = random.choice(choose)
        spell = aiSPELLsetUP(spellCHOICE)
        #print(spell)
        return(spell)
    if PCplayer[0] <= AIplayer[0] and AIplayer[0] > 25:
        choose = ['A', 'A', 'D']
        spellCHOICE = random.choice(choose)
        spell = aiSPELLsetUP(spellCHOICE)
        #print(spell)
        return(spell)

def menuINPUT():
    print('Input Key to make jaw move')
    print('A - Attack')
    print('B - Block')
    print('S - Spells')
    print('H - Heal')
    print('E - View JAW Equipment')
    print('C - Check the ENEMY Equipment')
    MOVE = input(str('JAW MOVE: '))
    print('-------------------------')
    MOVE = MOVE.upper()
    return(MOVE)

def AIfight(PCplayer, AIplayer, AIturn):
    if AIturn == 'A':
        attackRATE = AIplayer[1]
        finalMOVE = attack(attackRATE)
        return(finalMOVE)

    if AIturn == 'B':
        AR = AIplayer[2]
        finalMOVE = block(AR)
        return(finalMOVE)

    if AIturn == 'H':
        healrate = HEAL()
        finalMOVE = ['Heal', 'In Vas Mani']
        finalMOVE.insert(2, healrate)
        #print(finalMOVE)
        return(finalMOVE)

    if AIturn == 'Sai':
        AIspell = aiSPELLchoice(PCplayer, AIplayer)
        return(AIspell)

def PCFIGHT(MOVE, player):
    if MOVE == 'A':
        attackRATE = player[1]
        finalMOVE = attack(attackRATE)
        return(finalMOVE)

    if MOVE == 'B':
        AR = player[2]
        finalMOVE = block(AR)
        return(finalMOVE)

    if MOVE == 'H':
        healrate = HEAL()
        finalMOVE = ['Heal', 'In Vas Mani']
        finalMOVE.insert(2, healrate)
        return(finalMOVE)

    if MOVE == 'S':
        spell = SPELL()
        return(spell)

def AImove(PCplayer, AIplayer):
    AIturn = []
    # DECISIONS FOR LOWER THAN PC
    numWords = 5
    AItaunt = wordGrabLooper(numWords)
    print('Computer Says - "JAW {} IS {}. YOU {} {} NEWB. {} yourself' .format(AItaunt[0], AItaunt[1], AItaunt[2], AItaunt[3], AItaunt[4]))
    print('---------------------------------------------------------')
    if PCplayer[0] and AIplayer[0] == 100:
        choose = ['A', 'Sai', 'B']
        AIturn = random.choice(choose)
        return(AIturn)
    if PCplayer[0] >= AIplayer[0] and AIplayer[0] > 65:
        choose = ['A', 'Sai', 'B']
        AIturn = random.choice(choose)
        return(AIturn)
    if PCplayer[0] >= AIplayer[0] and AIplayer[0] > 45:
        choose = ['H' , 'B']
        AIturn = random.choice(choose)
        return(AIturn)
    if PCplayer[0] >= AIplayer[0] and AIplayer[0] <= 45:
        AIturn = 'H'
        return(AIturn)
    #DECISIONS FOR HIGHER HPS THAN PC
    if PCplayer[0] <= AIplayer[0] and AIplayer[0] > 65:
        choose = ['A', 'Sai']
        AIturn = random.choice(choose)
        return(AIturn)
    if PCplayer[0] <= AIplayer[0] and AIplayer[0] > 45:
        choose = ['A', 'Sai', 'H']
        AIturn = random.choice(choose)
        return(AIturn)
    if PCplayer[0] <= AIplayer[0] and AIplayer[0] > 25:
        AIturn = 'A'
        return(AIturn)
    else:
        AIturn = 'H'
        return(AIturn)

def battleMATH(userMOVE, AIround, PCplayer, AIplayer):
    #print(userMOVE)
    #print(AIround)
    if userMOVE[0] == 'Attack':
        if AIround[0] == 'Block':
            if userMOVE[2] > AIround[2]:
                damage = userMOVE[2] - AIround[2]
                AIplayer[0] = AIplayer[0] - damage
                print('Fool blocked but you powered THRU doing {} damage' .format(damage))
                return(PCplayer, AIplayer)
            if userMOVE[2] <= AIround[2]:
                print('FOOL blocked JAW attack')
                return(PCplayer, AIplayer)
        else:
            AIplayer[0] = AIplayer[0] - userMOVE[2]
            print('Jaw attacked with a {} for {} damage' .format(userMOVE[1], userMOVE[2]))

    if userMOVE[0] == 'Block':
        if AIround[0] == 'Block':
            print('Both Jaw puss asses blocked like women. No one takes damage')
            return(PCplayer, AIplayer)
        if AIround[0] == 'Attack':
            if AIround[2] > userMOVE[2]:
                damage = AIround[2] - userMOVE[2]
                PCplayer[0] = PCplayer[0] - damage
                print('JAW tried to block but FOOL ASS powered thru. You take {} damage.' .format(damage))
                return(PCplayer, AIplayer)
            if AIround[2] <= userMOVE[2]:
                print('jaw blocked BUT hes SWINGING....')
                print('NIIIIIIICE block. NO damage')
                return(PCplayer, AIplayer)
        else:
            print('You Blocked NOTHING')



    if userMOVE[0] == 'Heal':
        if AIround[0] == 'Attack':
            if AIround[2] > userMOVE[2]:
                print('JAW tried to heal but fool attacked you for more damage than jaw heal')
                damage = AIround[2] - userMOVE[2]
                PCplayer[0] = PCplayer[0] - damage
                print('Jaw still take {} damage' .format(damage))
                return(PCplayer, AIplayer)
            else:
                heal = userMOVE[2] - AIround[2]
                PCplayer[0] = PCplayer[0] + heal
                print('Jaw healed for {} HPS' .format(heal))
                return(PCplayer, AIplayer)
        if AIround[1] == 'Corp Por':
            if AIround[2] > userMOVE[2]:
                damage = AIround[2] - userMOVE[2]
                PCplayer[0] = PCplayer[0] - damage
                print('JAW healed but FOOL Corp Por you for {} damange' .format(damage))
                return(PCplayer, AIplayer)
            else:
                heal = userMOVE[2] - AIround[2]
                PCplayer[0] = PCplayer[0] + heal
                print('FOOL tried to Corp Por Jaw but your heal was better')
                print('JAW healed {} HPS' .format(heal))
                return(PCplayer, AIplayer)
        else:
            PCplayer[0] = PCplayer[0] + userMOVE[2]
            print('Jaw healed for {} HPS' .format(userMOVE[2]))


    if userMOVE[0] == 'Spell':
        print(userMOVE[1])
        if userMOVE[1] == 'Corp Por':
            AIplayer[0] = AIplayer[0] - userMOVE[2]
            print('Corp ASS Por Mother FUCKER')
            print('You do {} damange' .format(userMOVE[2]))
        if userMOVE[1] == 'Jaw weak Armor':
            AIplayer[2] = AIplayer[2] - userMOVE[2]
            print('JAW weaked FOOLs armor by {} points' .format(userMOVE[2]))
        if userMOVE[1] == 'Buff Armor':
            PCplayer[2] = PCplayer[2] + userMOVE[2]
            print('JAW BUFFFFED JAW ARMOR for {} points' .format(userMOVE[2]))
        if userMOVE[1] == 'Buff my Attack':
            PCplayer[1] = PCplayer[1] + userMOVE[2]
            print('JAW BUFF attack up by {} points' .format(userMOVE[2]))

    if AIround[0] == 'Attack':
        #print(AIround)
        PCplayer[0] = PCplayer[0] - AIround[2]
        print('Fool ass attacked you with a {} hit for {} damage' .format(AIround[1], AIround[2]))
        return(PCplayer, AIplayer)

    if AIround[0] == 'Block':
        print('Fool ass blocked but there was nothing to block')
        return(PCplayer, AIplayer)

    if AIround[0] == 'Heal':
        AIplayer[0] = AIplayer[0] + AIround[2]
        print('FOOL ASS says "{}"' .format(AIround[1]))
        print('Bitch ass healed for {} HPS' .format(AIround[2]))
        return(PCplayer, AIplayer)

    if AIround[0] == 'Spell':
        print('Computer Casting - {}' .format(AIround[1]))
        if AIround[1] == 'Corp Por':
            PCplayer[0] = PCplayer[0] - AIround[2]
            print('FOOL ASS CORP PORing')
            print('dude did do {} damange to ya' .format(AIround[2]))
            return(PCplayer, AIplayer)
        if AIround[1] == 'Jaw weak Armor':
            PCplayer[2] = PCplayer[2] - AIround[2]
            print('FOOL weaked jaw armor by {} points' .format(AIround[2]))
            return(PCplayer, AIplayer)
        if AIround[1] == 'Buff Armor':
            AIplayer[2] = AIplayer[2] + AIround[2]
            print('Dude just got buffed by {} points' .format(AIround[2]))
            return(PCplayer, AIplayer)
        if AIround[1] == 'Buff my Attack':
            AIplayer[1] = AIplayer[1] + AIround[2]
            print('hes mad buffing his attack by {} points' .format(AIround[2]))
            return(PCplayer, AIplayer)

    return(PCplayer, AIplayer)

def PCmove(MOVE, PCplayer, AIplayer, AIturn):
    userMOVE = PCFIGHT(MOVE, PCplayer)
    AIround = AIfight(PCplayer, AIplayer, AIturn)
    #print(userMOVE)
    #print(AIround)
    PCplayer, AIplayer = battleMATH(userMOVE, AIround, PCplayer, AIplayer)
    return(PCplayer, AIplayer)

def ROUND(PCplayer, AIplayer, pcEQUIPMENT, aiEQUIPMENT):
    print('-------------------------')
    print('JAWASS HPS: {}' .format(PCplayer[0]))
    print('Fool Ass Enemy HPS: {}' .format(AIplayer[0]))
    print('-------------------------')
    MOVE = menuINPUT()
    #print(MOVE)
    if MOVE == 'A':
        AIturn = AImove(PCplayer, AIplayer)
        #print(AIturn)
        PCplayer, AIplayer = PCmove(MOVE, PCplayer, AIplayer, AIturn)
        return(PCplayer, AIplayer, pcEQUIPMENT, aiEQUIPMENT)
    if MOVE == 'B':
        AIturn = AImove(PCplayer, AIplayer)
        #print(AIturn)
        PCplayer, AIplayer = PCmove(MOVE, PCplayer, AIplayer, AIturn)
        return(PCplayer, AIplayer, pcEQUIPMENT, aiEQUIPMENT)
    if MOVE == 'H':
        AIturn = AImove(PCplayer, AIplayer)
        #print(AIturn)
        PCplayer, AIplayer = PCmove(MOVE, PCplayer, AIplayer, AIturn)
        return(PCplayer, AIplayer, pcEQUIPMENT, aiEQUIPMENT)
    if MOVE == 'S':
        AIturn = AImove(PCplayer, AIplayer)
        #print(AIturn)
        PCplayer, AIplayer = PCmove(MOVE, PCplayer, AIplayer, AIturn)
        return(PCplayer, AIplayer, pcEQUIPMENT, aiEQUIPMENT)
    if MOVE == 'E':
        displayPCequip(pcEQUIPMENT, PCplayer)
        return(PCplayer, AIplayer, pcEQUIPMENT, aiEQUIPMENT)
    if MOVE == 'C':
        displayAIequip(aiEQUIPMENT, AIplayer)
        return(PCplayer, AIplayer, pcEQUIPMENT, aiEQUIPMENT)

def battleLOOP(PCplayer, AIplayer, pcEQUIPMENT, aiEQUIPMENT):
    PCplayer, AIplayer, pcEQUIPMENT, aiEQUIPMENT = ROUND(PCplayer, AIplayer, pcEQUIPMENT, aiEQUIPMENT)
    #print(PCplayer)
    #print(AIplayer)
    #print(pcEQUIPMENT)
    #print(aiEQUIPMENT)
    if PCplayer[0] > 100:
        PCplayer[0] = 100
    if AIplayer[0] > 100:
        AIplayer[0] = 100
    if PCplayer[0] <= 0:
        print('JAWASS DIED')
        sys.exit()
    if AIplayer[0] <= 0:
        print('JAW KILLED HIS ASS. YOU WON')
        sys.exit()
    else:
        #print('succesful loop')
        battleLOOP(PCplayer, AIplayer, pcEQUIPMENT, aiEQUIPMENT)

def main():
    print('Thug Ass Battle - Alpha as shit')
    aiEQUIPMENT = equipPLAYER()
    pcEQUIPMENT = equipPLAYER()
    AIplayer = configAI(aiEQUIPMENT)
    PCplayer = configPC(pcEQUIPMENT)
    #never comes back to main - game exits within battle loop
    battleLOOP(PCplayer, AIplayer, pcEQUIPMENT, aiEQUIPMENT)

main()



