while True: # X AND Y ARE TAKEN VARIABLES
    from random import randint
    import time
    
    
    sworddmg = 20
    bowdmg = 35
    bleed = 0
    playerbleed = 0
    
    print(" ")
    print("A challenger approaches!")
    print(" ")
    time.sleep(1)

    enemyclass = input("What class is your enemy? [mage] [knight] [ninja] [warrior] [random]")

    if (enemyclass == "Random") or (enemyclass == "random"):
        enemyclass = randint(1,4)
    
    if (enemyclass == "mage") or (enemyclass == "Mage") or (enemyclass == 1):
        enemyclass = "mage"
        enemyhealth = 70
        print("Your enemy is a mage!")

    elif (enemyclass == "knight") or (enemyclass == "Knight") or (enemyclass == 2):
        enemyclass = "knight"
        enemyhealth = 100
        print("Your enemy is a knight!")

    elif (enemyclass == "warrior") or (enemyclass == "Warrior") or (enemyclass == 3):
        enemyclass = "warrior"
        enemyhealth = 125
        print("Your enemy is a warrio!")

    elif (enemyclass == "ninja") or (enemyclass == "Ninja") or (enemyclass == 4):
        enemyclass = "ninja"
        enemyhealth = 80
        print("Your enemy is a ninja!")

    else:
        print("That is not a class!")
        continue
                

        
    time.sleep(1)   

    clazz = input("What class are you? Type help to see the classes and what they do. ")
    print(" ")
    if (clazz == "Knight") or (clazz == "knight"):

        health = 100
        
        while True:
            
            enemydagger = randint(1,8)
            daggerrandom = randint(1,8)
            enemydmg = 5 * enemydagger
            bowchance = randint(0,100)
            daggerdmg = 5 * daggerrandom
        
            
            print(" ")

            #YOUR TURN BEGINS
        
            weapon = input("Do you want to use your sword, bow or dagger? Type help for more info. ")
            print(" ")

            time.sleep(1)

            if (weapon == "sword") or (weapon == "Sword"):
                enemyhealth = enemyhealth - sworddmg
            
                print(" ")

                print("You attack! You do",(sworddmg),"damage!")
                time.sleep(1)

            elif (weapon == "dev"):
                enemyhealth = 0

            elif (weapon == "dagger") or (weapon =="Dagger"):
                enemyhealth = enemyhealth - daggerdmg

                print(" ")
            
                print("You attack and hit",(daggerrandom),"times! You do",(daggerdmg),"damage!")
                time.sleep(1)

            elif (weapon == "bow") or (weapon == "Bow"):
        
                if bowchance <= 50:
            
                    enemyhealth = enemyhealth - bowdmg

                    print("You attack! You do",(bowdmg),"damage!")
                    print(" ")
                    time.sleep(1)

                else:
                    print("You missed!")
                    time.sleep(1)

            elif (weapon == "help") or (weapon == "Help"):
                print("The sword does 20 damage, and will always hit.")
                print(" ")
                time.sleep(0.5)
                print("The dagger does 5 damage, but can hit up to 8 times in one go.")
                print(" ")
                time.sleep(0.5)
                print("The bow does 35 damage, but has a 50% chance to miss.")
                time.sleep(0.5)
                continue

            elif (weapon == "health") or (weapon == "Health"):
                print("Your health is",(health),"!")
                continue



            else:
                print("That isn't a weapon!")
                time.sleep(1)
                continue

            #YOUR TURN ENDS

            #ENEMY TURN BEGINS//////////////////////////////////////////////////////////////////////////////////////////////////////////

            if (enemyclass == "Knight") or (enemyclass == "knight"):

        
                enemyweapon = randint(1,3)

                print(" ")

                if health <= 20:
                    health = health - sworddmg
                    print("The enemy attacks with a sword! They do",(sworddmg),"damage!")
                    time.sleep(1)

                elif enemyweapon == 1:
                    print("The enemy attacks with a sword! They do",(sworddmg),"damage!")
                    health = health - sworddmg
                    time.sleep(1)

                elif enemyweapon == 2:
                    print("The enemy attacks with a dagger and hits",(enemydagger),"times! They do",(enemydmg),"damage!")
                    health = health - enemydmg
                    time.sleep(1)

                elif enemyweapon == 3:
                    print("The enemy attacks with a bow!")
                    enemybow = randint(0,100)
                    time.sleep(1)
                    if enemybow <=50:
                        health = health - bowdmg
                        print("They do",(bowdmg),"damage!")
                        time.sleep(1)

                    else:
                        print("They miss!")
                        time.sleep(1)


            elif (enemyclass == "mage") or (enemyclass == "Mage"):



                while True:

                    enemyice = randint(1,10)
                    enemyicedmg = 5 * enemyice
                    enemyfirehits = randint(1,2)
                    enemyfire = 20 * enemyfirehits
                    enemyfreezechance = randint(0,100)
                    enemyweapon = randint(1,3)


                    if enemyweapon == 1:
                        print("The enemy attacks with a fireball spell! They do",(enemyfire),"damage!")
                        health = health - enemyfire
                        time.sleep(1)
    
                    elif enemyweapon == 2:
                        print("The enemy attacks with the ice-jab spell! They hit",(enemyice),"times, and deal",(enemyicedmg),"damage!")
                        health = health - enemyicedmg

                        if enemyfreezechance <= 50:
                            print(" ")
                            print("You are frozen for the rest of this turn!")
                            continue
                        
                        time.sleep(1)
    
                    elif enemyweapon == 3:
                        print("The enemy uses a heal spell!")
                        enemyhealchance = randint(0,100)
                        time.sleep(1)
                        if enemyhealchance <=50:
                            enemyhealth = enemyhealth + 40
                            print("They heal 40 damage!")
                            time.sleep(1)
    
                        else:
                            print("Their heal spell fails!")
                            time.sleep(1)
                    break


            elif (enemyclass == "Warrior") or (enemyclass == "warrior"):

                while True:
                    enemyweapon = randint(1,3)
                    chargedmg = 35
                    greatsworddmg = 20

                    if enemyweapon == 1:
                        print("The enemy attacks with their greatsword! They do",(greatsworddmg),"damage!")
                        health = health - greatsworddmg
                        time.sleep(1)

                    elif enemyweapon == 2:
                        enemychargechance = randint(0,100)
                        print("The enemy charges at you!")
                        time.sleep(1)

                        if enemychargechance <= 35:
                            health = health - chargedmg
                            print(" ")
                            print("The enemy did 35 damage and you were stunned!")
                            continue

                        else:
                            print(" ")
                            print("The enemy missed the charge!")
                            time.sleep(1)

                    elif enemyweapon == 3:
                        enemyblockchance = randint(0,100)
                        time.sleep(1)
                        if enemyblockchance <=70:
                            enemyhealth = enemyhealth + 10
                            print("The enemy manages to block your next attack and heal 10 health!")
                            time.sleep(1)
                            continue

                        else:
                            print("The enemy attempts to block your next attack but fails!")
                            time.sleep(1)
                    break

            elif (enemyclass == "Ninja") or (enemyclass == "ninja"):

                while True:
                    enemyweapon = randint(1,3)
                    enemyknifehits = randint(1,8)
                    enemybleedchance = randint(0,100)
                    enemyswordhits = randint(1,2)
                    enemysworddmg = 15 * enemyswordhits
                    enemyshurikendmg = 20
                    enemyknifedmg = 5 * enemyknifehits

                    if enemyweapon == 1:
                        print(" ")
                        print("The enemy slices you with a sword",(enemyswordhits),"time(s), and does",(enemysworddmg),"damage!")
                        time.sleep(1)
                        health = health - enemysworddmg

                    elif enemyweapon == 2:
                        print(" ")
                        print("The enemy throws shurikens at you! It does 20 damage!")
                        health = health - enemyshurikendmg
                        time.sleep(1)

                    elif enemyweapon == 3:
                        print(" ")
                        print("The enemy throws",(enemyknifehits),"knives at you! It does",(enemyknifedmg),"damage!")
                        health = health - enemyknifedmg
                        time.sleep(1)

                        if enemybleedchance <= 50:

                            print("The knives caused you to bleed! You will now take 10 dage per turn until death.")
                            playerbleed = playerbleed + 1

                    break
                        
        

            # ENEMY TURN IS OVER///////////////////////////////////////////////////////////////////////////////////////////////////////////////
            time.sleep(1)
            print(" ")
            
            print("The enemy's health is",(enemyhealth))
            time.sleep(1)
            print(" ")

            if playerbleed >= 1:
                print("You're bleeding! You take 10 damage!")
                health = health - 10

            if enemyhealth <= 0:
                print("You won!")
                break
        
            print("Your health is",(health))


            if health <= 0:
                print("You lost!")
                break

        print(" ")
    

        x = input("Do you want to keep playing?: ")
        if (x == "y") or (x == "yes") or (x == "Yes") or (x == "Y") or (x == "yeah") or (x == "yea"):
            continue
        
        else:
            break
        break

                    
    elif (clazz == "Mage") or (clazz == "mage"):
        health = 70
        while True:
            firehits = randint(1,2)
            firedmg = 20 * firehits
            enemydagger = randint(1,8)
            icejabrandom = randint(1,10)
            icejabdmg = 5 * icejabrandom
            enemydmg = 5 * randint(1,8)
            daggerrandom = randint(1,8)
            daggerdmg = 5 * daggerrandom
            enemydmg = 5 * enemydagger
            bowchance = randint(0,100)
            
            heal = 40

            print(" ")

        
            weapon = input("Do you want to use your fireball, ice-jab or heal? Type help for more info. ")
            healchance = randint(0,100)
            freeze = randint(0,100)
            
            print(" ")

            time.sleep(1)

            if (weapon == "fireball") or (weapon == "Fireball"):
                enemyhealth = enemyhealth - firedmg
            
                print(" ")

                print("You attack! You do",(firedmg),"damage!")
                time.sleep(1)

            elif (weapon == "health") or (weapon == "Health"):
                print("Your health is",(health),"!")
                continue


            elif (weapon == "dev"):
                enemyhealth = 0

            elif (weapon == "icejab") or (weapon =="Icejab") or (weapon == "ice-jab") or (weapon == "Ice-jab") or (weapon =="Ice jab") or (weapon =="ice jab"):
                enemyhealth = enemyhealth - icejabdmg

                print(" ")
            
                print("You attack and hit",(icejabrandom),"Times! You do",(icejabdmg),"damage!")



                if freeze <=50:
                    print("The enemy has been frozen for the rest of this turn!")
                    continue

                else:
                    print(" ")
                    

                    
                    
                    
                time.sleep(1)

            elif (weapon == "heal") or (weapon == "Heal"):
        
                if healchance <= 50:
            
                    health = health + heal

                
            
                    print("You cast a healing aura! You heal",(heal),"damage!")
                    print(" ")
                    time.sleep(1)

                else:
                    print("Healing failed!")
                    time.sleep(1)

            elif (weapon == "help") or (weapon == "Help"):
                print("Fireball does 20 damage, but has a chance to hit twice.")
                print(" ")
                time.sleep(0.5)
                print("Ice-jab does 5 damage, but can hit up to 10 times in one go, it also has a 50% chance to cause the enemy to not attack this turn.")
                print(" ")
                time.sleep(0.5)
                print("The heal has a 50% chance to heal you, and heals 40 health.")
                time.sleep(0.5)
                continue



            else:
                print("That isn't a spell!")
                time.sleep(1)
                continue
            
            if health > 70:
                health = 70
                print("Health cant be more than max!")

        
            if (enemyclass == "Knight") or (enemyclass == "knight"):

        
                enemyweapon = randint(1,3)

                print(" ")

                if health <= 20:
                    health = health - sworddmg
                    print("The enemy attacks with a sword! They do",(sworddmg),"damage!")
                    time.sleep(1)

                elif enemyweapon == 1:
                    print("The enemy attacks with a sword! They do",(sworddmg),"damage!")
                    health = health - sworddmg
                    time.sleep(1)

                elif enemyweapon == 2:
                    print("The enemy attacks with a dagger and hits",(enemydagger),"times! They do",(enemydmg),"damage!")
                    health = health - enemydmg
                    time.sleep(1)

                elif enemyweapon == 3:
                    print("The enemy attacks with a bow!")
                    enemybow = randint(0,100)
                    time.sleep(1)
                    if enemybow <=50:
                        health = health - bowdmg
                        print("They do",(bowdmg),"damage!")
                        time.sleep(1)

                    else:
                        print("They miss!")
                        time.sleep(1)


            elif (enemyclass == "mage") or (enemyclass == "Mage"):



                while True:

                    enemyice = randint(1,10)
                    enemyicedmg = 5 * enemyice
                    enemyfirehits = randint(1,2)
                    enemyfire = 20 * enemyfirehits
                    enemyfreezechance = randint(0,100)
                    enemyweapon = randint(1,3)


                    if enemyweapon == 1:
                        print("The enemy attacks with a fireball spell! They do",(enemyfire),"damage!")
                        health = health - enemyfire
                        time.sleep(1)
    
                    elif enemyweapon == 2:
                        print("The enemy attacks with the ice-jab spell! They hit",(enemyice),"times, and deal",(enemyicedmg),"damage!")
                        health = health - enemyicedmg

                        if enemyfreezechance <= 50:
                            print(" ")
                            print("You are frozen for the rest of this turn!")
                            continue
                        
                        time.sleep(1)
    
                    elif enemyweapon == 3:
                        print("The enemy uses a heal spell!")
                        enemyhealchance = randint(0,100)
                        time.sleep(1)
                        if enemyhealchance <=50:
                            enemyhealth = enemyhealth + 40
                            print("They heal 40 damage!")
                            time.sleep(1)
    
                        else:
                            print("Their heal spell fails!")
                            time.sleep(1)
                    break


            elif (enemyclass == "Warrior") or (enemyclass == "warrior"):

                while True:
                    enemyweapon = randint(1,3)
                    chargedmg = 35
                    greatsworddmg = 20

                    if enemyweapon == 1:
                        print("The enemy attacks with their greatsword! They do",(greatsworddmg),"damage!")
                        health = health - greatsworddmg
                        time.sleep(1)

                    elif enemyweapon == 2:
                        enemychargechance = randint(0,100)
                        print("The enemy charges at you!")
                        time.sleep(1)

                        if enemychargechance <= 35:
                            health = health - chargedmg
                            print(" ")
                            print("The enemy did 35 damage and you were stunned!")
                            continue

                        else:
                            print(" ")
                            print("The enemy missed the charge!")
                            time.sleep(1)

                    elif enemyweapon == 3:
                        enemyblockchance = randint(0,100)
                        time.sleep(1)
                        if enemyblockchance <=70:
                            enemyhealth = enemyhealth + 10
                            print("The enemy manages to block your next attack and heal 10 health!")
                            time.sleep(1)
                            continue

                        else:
                            print("The enemy attempts to block your next attack but fails!")
                            time.sleep(1)
                    break

            elif (enemyclass == "Ninja") or (enemyclass == "ninja"):

                while True:
                    enemyweapon = randint(1,3)
                    enemyknifehits = randint(1,8)
                    enemybleedchance = randint(0,100)
                    enemyswordhits = randint(1,2)
                    enemysworddmg = 15 * enemyswordhits
                    enemyshurikendmg = 20
                    enemyknifedmg = 5 * enemyknifehits

                    if enemyweapon == 1:
                        print(" ")
                        print("The enemy slices you with a sword",(enemyswordhits),"time(s), and does",(enemysworddmg),"damage!")
                        time.sleep(1)
                        health = health - enemysworddmg

                    elif enemyweapon == 2:
                        print(" ")
                        print("The enemy throws shurikens at you! It does 20 damage!")
                        health = health - enemyshurikendmg
                        time.sleep(1)

                    elif enemyweapon == 3:
                        print(" ")
                        print("The enemy throws",(enemyknifehits),"knives at you! It does",(enemyknifedmg),"damage!")
                        health = health - enemyknifedmg
                        time.sleep(1)

                        if enemybleedchance <= 50:

                            print("The knives caused you to bleed! You will now take 10 damage per turn until death.")
                            playerbleed = playerbleed + 1

                    break
        
        
            time.sleep(1)
            print(" ")

            if playerbleed >= 1:
                print("You're bleeding! You take 10 damage!")
                health = health - 10
            
            print("The enemy's health is",(enemyhealth))
            time.sleep(1)
            print(" ")

            if enemyhealth <= 0:
                print("You won!")
                break
        
            print("Your health is",(health))


            if health <= 0:
                print("You lost!")
                break

        print(" ")
    

        x = input("Do you want to keep playing?: ")
        if (x == "y") or (x == "yes") or (x == "Yes") or (x == "Y") or (x == "yeah") or (x == "yea"):
            continue
        
        else:
            break
        break

    elif (clazz == "warrior") or (clazz == "Warrior"):
        health = 125
        while True:
            greatsworddmg = 20
            enemydagger = randint(1,8)
            daggerrandom = randint(1,8)
            enemydmg = 5 * enemydagger
            bowchance = randint(0,100)
            daggerdmg = 5 * daggerrandom
            blockchance = randint(0,100)
            bleedchance = randint(0,100)
            chargedmg = 35
            chargechance = randint(0,100)
        
            
            print(" ")

        
            weapon = input("Do you want to use your greatsword, block or charge at the enemy? Type help for more info. ")
            print(" ")

            time.sleep(1)

    

            if (weapon == "greatsword") or (weapon == "Greatsword"):
                
                enemyhealth = enemyhealth - greatsworddmg
            
                print(" ")

                print("You attack! You do",(greatsworddmg),"damage!")
                time.sleep(1)

            elif (weapon == "dev"):
                enemyhealth = 0

            elif (weapon == "Block") or (weapon =="block"):
                
                if blockchance <= 70:
                    
                    
                    print("You block! This gives you time to regenerate 10 health!")
                    health = health + 5
                    time.sleep(1)

                    if health >125:
                        print("Your health cannot be more than max.")
                        health = 125
                    
                    
                    continue
                else:
                    print("You couldn't block in time!")
                    


            elif (weapon == "charge") or (weapon == "Charge"):

                if chargechance <= 35:
                    enemyhealth = enemyhealth - chargedmg
                    print("You land the charge! You deal",(chargedmg),"damage and the enemy is unable to move this turn!")

                    print("The enemy's health is",(enemyhealth))
                    time.sleep(1)
                    print(" ")

                    if enemyhealth <= 0:
                        print("You won!")
                        break

                    
                    continue
                else:
                    print("You missed the charge!")
                    time.sleep(1)
        


            elif (weapon == "help") or (weapon == "Help"):
                print("The greatsword does 20 damage, and will always hit.")
                print(" ")
                time.sleep(0.5)
                print("Blocking skips the enemies turn and lets you regenrate 10 health, but only has a 70% chance to work.")
                print(" ")
                time.sleep(0.5)
                print("Charging at the enemy does 35 damage and stuns the enemy! It has a 35% chance to hit.")
                time.sleep(0.5)
                continue

            elif (weapon == "health") or (weapon == "Health"):
                print("Your health is",(health),"!")
                continue


            else:
                print("That isn't a weapon!")
                time.sleep(1)
                continue
            

        
            if (enemyclass == "Knight") or (enemyclass == "knight"):

        
                enemyweapon = randint(1,3)

                print(" ")

                if health <= 20:
                    health = health - sworddmg
                    print("The enemy attacks with a sword! They do",(sworddmg),"damage!")
                    time.sleep(1)

                elif enemyweapon == 1:
                    print("The enemy attacks with a sword! They do",(sworddmg),"damage!")
                    health = health - sworddmg
                    time.sleep(1)

                elif enemyweapon == 2:
                    print("The enemy attacks with a dagger and hits",(enemydagger),"times! They do",(enemydmg),"damage!")
                    health = health - enemydmg
                    time.sleep(1)

                elif enemyweapon == 3:
                    print("The enemy attacks with a bow!")
                    enemybow = randint(0,100)
                    time.sleep(1)
                    if enemybow <=50:
                        health = health - bowdmg
                        print("They do",(bowdmg),"damage!")
                        time.sleep(1)

                    else:
                        print("They miss!")
                        time.sleep(1)


            elif (enemyclass == "mage") or (enemyclass == "Mage"):



                while True:

                    enemyice = randint(1,10)
                    enemyicedmg = 5 * enemyice
                    enemyfirehits = randint(1,2)
                    enemyfire = 20 * enemyfirehits
                    enemyfreezechance = randint(0,100)
                    enemyweapon = randint(1,3)


                    if enemyweapon == 1:
                        print("The enemy attacks with a fireball spell! They do",(enemyfire),"damage!")
                        health = health - enemyfire
                        time.sleep(1)
    
                    elif enemyweapon == 2:
                        print("The enemy attacks with the ice-jab spell! They hit",(enemyice),"times, and deal",(enemyicedmg),"damage!")
                        health = health - enemyicedmg

                        if enemyfreezechance <= 50:
                            print(" ")
                            print("You are frozen for the rest of this turn!")
                            continue
                        
                        time.sleep(1)
    
                    elif enemyweapon == 3:
                        print("The enemy uses a heal spell!")
                        enemyhealchance = randint(0,100)
                        time.sleep(1)
                        if enemyhealchance <=50:
                            enemyhealth = enemyhealth + 40
                            print("They heal 40 damage!")
                            time.sleep(1)
    
                        else:
                            print("Their heal spell fails!")
                            time.sleep(1)
                    break


            elif (enemyclass == "Warrior") or (enemyclass == "warrior"):

                while True:
                    enemyweapon = randint(1,3)
                    chargedmg = 35
                    greatsworddmg = 20

                    if enemyweapon == 1:
                        print("The enemy attacks with their greatsword! They do",(greatsworddmg),"damage!")
                        health = health - greatsworddmg
                        time.sleep(1)

                    elif enemyweapon == 2:
                        enemychargechance = randint(0,100)
                        print("The enemy charges at you!")
                        time.sleep(1)

                        if enemychargechance <= 35:
                            health = health - chargedmg
                            print(" ")
                            print("The enemy did 35 damage and you were stunned!")
                            continue

                        else:
                            print(" ")
                            print("The enemy missed the charge!")
                            time.sleep(1)

                    elif enemyweapon == 3:
                        enemyblockchance = randint(0,100)
                        time.sleep(1)
                        if enemyblockchance <=70:
                            enemyhealth = enemyhealth + 10
                            print("The enemy manages to block your next attack and heal 10 health!")
                            time.sleep(1)
                            continue

                        else:
                            print("The enemy attempts to block your next attack but fails!")
                            time.sleep(1)
                    break

            elif (enemyclass == "Ninja") or (enemyclass == "ninja"):

                while True:
                    enemyweapon = randint(1,3)
                    enemyknifehits = randint(1,8)
                    enemybleedchance = randint(0,100)
                    enemyswordhits = randint(1,2)
                    enemysworddmg = 15 * enemyswordhits
                    enemyshurikendmg = 20
                    enemyknifedmg = 5 * enemyknifehits

                    if enemyweapon == 1:
                        print(" ")
                        print("The enemy slices you with a sword",(enemyswordhits),"time(s), and does",(enemysworddmg),"damage!")
                        time.sleep(1)
                        health = health - enemysworddmg

                    elif enemyweapon == 2:
                        print(" ")
                        print("The enemy throws shurikens at you! It does 20 damage!")
                        health = health - enemyshurikendmg
                        time.sleep(1)

                    elif enemyweapon == 3:
                        print(" ")
                        print("The enemy throws",(enemyknifehits),"knives at you! It does",(enemyknifedmg),"damage!")
                        health = health - enemyknifedmg
                        time.sleep(1)

                        if enemybleedchance <= 50:

                            print("The knives caused you to bleed! You will now take 10 damage per turn until death.")
                            playerbleed = playerbleed + 1

                    break
        
        
            time.sleep(1)
            print(" ")
            
            print("The enemy's health is",(enemyhealth))
            time.sleep(1)
            print(" ")

            if playerbleed >= 1:
                print("You're bleeding! You take 10 damage!")
                health = health - 10

            if enemyhealth <= 0:
                print("You won!")
                break
        
            print("Your health is",(health))


            if health <= 0:
                print("You lost!")
                break

        print(" ")
    

        x = input("Do you want to keep playing?: ")
        if (x == "y") or (x == "yes") or (x == "Yes") or (x == "Y") or (x == "yeah") or (x == "yea"):
            continue
        
        else:
            break
        break

    elif (clazz == "Ninja") or (clazz == "ninja"):

        health = 80
        bleed = 0
        while True:
            knifehits = randint(1,8)
            enemydagger = randint(1,8)
            daggerrandom = randint(1,8)
            enemydmg = 5 * enemydagger
            bowchance = randint(0,100)
            daggerdmg = 5 * daggerrandom
            shurikendmg = 20
            ninjadmg = 15
            knifedmg = 5 * knifehits
            bleedchance = randint(0,100)      
        
            
            print(" ")

        
            weapon = input("Do you want to use your sword, shurikens or throwing knives? Type help for more info. ")
            print(" ")

            time.sleep(1)

            if (weapon == "shuriken") or (weapon == "Shuriken"):
                enemyhealth = enemyhealth - shurikendmg
            
                print(" ")

                print("You attack! You do",(shurikendmg),"damage!")
                time.sleep(1)

            elif (weapon == "dev"):
                enemyhealth = 0

            elif (weapon == "sword") or (weapon =="Sword"):
                critical = randint(1,2)
                enemyhealth = enemyhealth - ninjadmg * critical

                print(" ")
            
                print("You slice with your sword",(critical),"time(s) and deal",(ninjadmg * critical),"damage!")
                time.sleep(1)

            elif (weapon == "knife") or (weapon == "Knife") or (weapon == "Throwing knife") or (weapon == "throwing knife") or (weapon == "Throwing knives") or (weapon == "throwing knives"):
                enemyhealth = enemyhealth - knifedmg
                print("You throw",(knifehits),"times! You do",(knifedmg),"damage!")
                if bleedchance <= 30:
                    bleed = bleed + 1
                    print("The enemy is now bleeding! They will take 10 damage every turn from now on!")
                else:
                    print("The knives did not cause the enemy to bleed!")
                

            elif (weapon == "help") or (weapon == "Help"):
                print("The sword does 15 damage, and has a chance to hit twice.")
                print(" ")
                time.sleep(0.5)
                print("The shurikens do 20 damage.")
                print(" ")
                time.sleep(0.5)
                print("The throwing knives do 5 damage, and have a chance to hit 8 times. They also have a 30% chance to make the enemy bleed, causing them to take 10 damage per turn for the rest of the battle.")
                time.sleep(0.5)
                continue

            elif (weapon == "ligma") or (weapon == "Ligma"): # courtesy of saffron
                print("You got ligma. You dead.")
                break

            elif (weapon == "health") or (weapon == "Health"):
                print("Your health is",(health),"!")
                continue
            
            else:
                print("That isn't a weapon!")
                time.sleep(1)
                continue
            

        
            if (enemyclass == "Knight") or (enemyclass == "knight"):

        
                enemyweapon = randint(1,3)

                print(" ")

                if health <= 20:
                    health = health - sworddmg
                    print("The enemy attacks with a sword! They do",(sworddmg),"damage!")
                    time.sleep(1)

                elif enemyweapon == 1:
                    print("The enemy attacks with a sword! They do",(sworddmg),"damage!")
                    health = health - sworddmg
                    time.sleep(1)

                elif enemyweapon == 2:
                    print("The enemy attacks with a dagger and hits",(enemydagger),"times! They do",(enemydmg),"damage!")
                    health = health - enemydmg
                    time.sleep(1)

                elif enemyweapon == 3:
                    print("The enemy attacks with a bow!")
                    enemybow = randint(0,100)
                    time.sleep(1)
                    if enemybow <=50:
                        health = health - bowdmg
                        print("They do",(bowdmg),"damage!")
                        time.sleep(1)

                    else:
                        print("They miss!")
                        time.sleep(1)


            elif (enemyclass == "mage") or (enemyclass == "Mage"):



                while True:

                    enemyice = randint(1,10)
                    enemyicedmg = 5 * enemyice
                    enemyfirehits = randint(1,2)
                    enemyfire = 20 * enemyfirehits
                    enemyfreezechance = randint(0,100)
                    enemyweapon = randint(1,3)


                    if enemyweapon == 1:
                        print("The enemy attacks with a fireball spell! They do",(enemyfire),"damage!")
                        health = health - enemyfire
                        time.sleep(1)
    
                    elif enemyweapon == 2:
                        print("The enemy attacks with the ice-jab spell! They hit",(enemyice),"times, and deal",(enemyicedmg),"damage!")
                        health = health - enemyicedmg

                        if enemyfreezechance <= 50:
                            print(" ")
                            print("You are frozen for the rest of this turn!")
                            continue
                        
                        time.sleep(1)
    
                    elif enemyweapon == 3:
                        print("The enemy uses a heal spell!")
                        enemyhealchance = randint(0,100)
                        time.sleep(1)
                        if enemyhealchance <=50:
                            enemyhealth = enemyhealth + 40
                            print("They heal 40 damage!")
                            time.sleep(1)
    
                        else:
                            print("Their heal spell fails!")
                            time.sleep(1)
                    break


            elif (enemyclass == "Warrior") or (enemyclass == "warrior"):

                while True:
                    enemyweapon = randint(1,3)
                    chargedmg = 35
                    greatsworddmg = 20

                    if enemyweapon == 1:
                        print("The enemy attacks with their greatsword! They do",(greatsworddmg),"damage!")
                        health = health - greatsworddmg
                        time.sleep(1)

                    elif enemyweapon == 2:
                        enemychargechance = randint(0,100)
                        print("The enemy charges at you!")
                        time.sleep(1)

                        if enemychargechance <= 35:
                            health = health - chargedmg
                            print(" ")
                            print("The enemy did 35 damage and you were stunned!")
                            continue

                        else:
                            print(" ")
                            print("The enemy missed the charge!")
                            time.sleep(1)

                    elif enemyweapon == 3:
                        enemyblockchance = randint(0,100)
                        time.sleep(1)
                        if enemyblockchance <=70:
                            enemyhealth = enemyhealth + 10
                            print("The enemy manages to block your next attack and heal 10 health!")
                            time.sleep(1)
                            continue

                        else:
                            print("The enemy attempts to block your next attack but fails!")
                            time.sleep(1)
                    break

            elif (enemyclass == "Ninja") or (enemyclass == "ninja"):

                while True:
                    enemyweapon = randint(1,3)
                    enemyknifehits = randint(1,8)
                    enemybleedchance = randint(0,100)
                    enemyswordhits = randint(1,2)
                    enemysworddmg = 15 * enemyswordhits
                    enemyshurikendmg = 20
                    enemyknifedmg = 5 * enemyknifehits

                    if enemyweapon == 1:
                        print(" ")
                        print("The enemy slices you with a sword",(enemyswordhits),"time(s), and does",(enemysworddmg),"damage!")
                        time.sleep(1)
                        health = health - enemysworddmg

                    elif enemyweapon == 2:
                        print(" ")
                        print("The enemy throws shurikens at you! It does 20 damage!")
                        health = health - enemyshurikendmg
                        time.sleep(1)

                    elif enemyweapon == 3:
                        print(" ")
                        print("The enemy throws",(enemyknifehits),"knives at you! It does",(enemyknifedmg),"damage!")
                        health = health - enemyknifedmg
                        time.sleep(1)

                        if enemybleedchance <= 50:

                            print("The knives caused you to bleed! You will now take 10 damage per turn until death.")
                            playerbleed = playerbleed + 1

                    break
        
        
            time.sleep(1)
            print(" ")

            if playerbleed >= 1:
                print("You're bleeding! You take 10 damage!")
                health = health - 10
                

            if bleed >= 1:
                enemyhealth = enemyhealth - 10
                print("The enemy is bleeding! They take 10 damage!")

            else:
                lambda x: None
            
            print("The enemy's health is",(enemyhealth))
            time.sleep(1)
            print(" ")

            

            if enemyhealth <= 0:
                print("You won!")
                break
        
            print("Your health is",(health))


            if health <= 0:
                print("You lost!")
                break

        print(" ")
    

        x = input("Do you want to keep playing?: ")
        if (x == "y") or (x == "yes") or (x == "Yes") or (x == "Y") or (x == "yeah") or (x == "yea"):
            continue
        
        elif (x == "n") or (x == "N") or (x == "No") or (x == "no"):
            break


    elif (clazz == "help") or (clazz =="Help"):
        time.sleep(1)
        print("The knight is a class which focuses on dealing damage.")
        print(" ")
        time.sleep(0.5)
        print("The mage is a class which focuses on dealing high amounts of damage while also healing themself to stay alive.")
        print(" ")
        time.sleep(0.5)
        print("The warrior is a class which has high base health, and can stun the enemy and block attacks.")
        print(" ")
        time.sleep(0.5)
        print("The ninja is a class which deals high amounts of damage, relying on chain hits and status effects to win.")
        time.sleep(0.5)

    else:
        print("That isn't a class!")
        
        
        


                

        


        
