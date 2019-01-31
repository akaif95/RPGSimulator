'''
Description:
<Program consists of OOP used to design a game where two
players fight each other, and the first one to lost all their 
health points loses! >
'''
import random

class Fighter:

    def __init__(self, name):
        self.name = name
        self.hit_points = 10

    def __repr__(self):
        return (self.name + " (HP: " + str(self.hit_points) + ")")

    def take_damage(self, damage_amount):
        self.hit_points -= damage_amount

        if self.hit_points <= 0:
            print("\tAlas, " + self.name + " has fallen!")
        else:
            print("\t" + self.name + " has " + str(self.hit_points) + " hit points remaining.")

    def attack(self, other):
        print(self.name + " attacks " + other.name + "!")

        attack_chance = random.randrange(1, 20)

        if attack_chance >= 12:
            damage_inflicted = random.randrange(1, 7)
            print("\tHits for " + str(damage_inflicted) + " hit points!")
            other.take_damage(damage_inflicted)
        else:
            print("\tMisses!")

    def is_alive(self):
        if self.hit_points > 0:
            return True
        else:
            return False

def combat_round(instance_one, instance_two):
    strike_first = random.randrange(1, 7)
    strike_second = random.randrange(1, 7)

    if strike_first == strike_second:
        print("Simultaneous!")

        instance_one.attack(instance_two)
        instance_two.attack(instance_one)

    else:
        if strike_first > strike_second:
            instance_one.attack(instance_two)

            if instance_two.is_alive() == True:
                instance_two.attack(instance_one)

        else:
            instance_two.attack(instance_one)
            if instance_one.is_alive() == True:
                instance_one.attack(instance_two)



        

#==========================================================
def main():
    '''
    '''

    Death_Mongrel = Fighter("Death_Mongrel")
    Hurt_then_Pain = Fighter("Hurt_then_Pain")

    rounds = 1

    pause = input("Enter to Fight!")

    while Death_Mongrel.is_alive() and Hurt_then_Pain.is_alive():
        print("=" * 19 + " ROUND " + str(rounds) + " " + "=" * 19)
        print(Death_Mongrel)
        print(Hurt_then_Pain)

        combat_round(Death_Mongrel, Hurt_then_Pain)
    

        rounds += 1

    print("The battle is over!")

    print(Death_Mongrel)
    print(Hurt_then_Pain)



    