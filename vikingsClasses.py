
# Soldier


import random


class Soldier:

    def __init__(self, health, strength):
        self.health=health
        self.strength=strength

    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.health-=damage

# Viking

class Viking(Soldier):

    def __init__(self, name, health, strength):
        self.name=name
        Soldier.__init__(self, health, strength)

    def receiveDamage(self, damage):
        self.health-=damage  
        if self.health>0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat" 
    
    def battleCry(self):
        return "Odin Owns You All!"



# Saxon


class Saxon(Soldier):
    def __init__(self, health, strength):
        Soldier.__init__(self, health, strength)
    
    def receiveDamage(self, damage):
        self.health-=damage
        if self.health>0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return "A Saxon has died in combat"


# War


class War:
    def __init__(self):
        self.vikingArmy=[]
        self.saxonArmy=[]

    def addViking(self, Viking):
        self.vikingArmy.append(Viking)
    
    def addSaxon(self, Saxon):
        self.saxonArmy.append(Saxon)
        

    def vikingAttack(self):
        saxon_s=random.choice(self.saxonArmy)
        viking_s=random.choice(self.vikingArmy)
        v=saxon_s.receiveDamage(viking_s.strength)
        if saxon_s.health<=0:
            self.saxonArmy.remove(saxon_s)
        return v
    
    def saxonAttack(self):
        saxon_s=random.choice(self.saxonArmy)
        viking_s=random.choice(self.vikingArmy)
        v=viking_s.receiveDamage(saxon_s.strength)
        if viking_s.health<=0:
            self.vikingArmy.remove(viking_s)      
        return v
    
    def showStatus(self):
        if len(self.saxonArmy)==0:
            return "Vikings have won the war of the century!"
        if len(self.vikingArmy)==0:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."