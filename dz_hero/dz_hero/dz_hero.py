import random

class Hero:
    def __init__(self,name,min_damage,max_damage,hp,min_satiety,max_satiety,min_energy,max_energy):
        self.name = name
        self.min_damage = min_damage
        self.max_damage = max_damage
        self.hp = hp
        self.min_satiety = min_satiety #мин.сытость
        self.max_satiety = max_satiety
        self.min_energy = min_energy 
        self.max_energy = max_energy      
    def run(self):
        print(self.name + "в пути")
    def food(self,satiety):
        if satiety <= 5:
           print(self.name + "Нужно поспать!!!")
        elif satiety > 5 or self.satiety == max.satiety:
             print(self.name + "не голоден")
    def power(self,energy):
        if energy <= 5:
           print(self.name + "вымотан!!!")
        elif energy > 5 or self.energy == max.energy:
           print(self.name + "бодр")

    def down_health(self,damage,satiety,energy):
        if self.hp == 0:
           print(self.name + "убит")
        else: 
           self.hp - damage - satiety - energy
           print("у {} осталось {} очков здоровья".format(self.name,self.hp))
    def fight(self,enemy):
     energy = random.randint(self.min_energy,self.max_energy)
     damage = random.randint(self.min_damage,self.max_damage)
     satiety = random.randint(self.min_satiety,self.max_satiety)     
     enemy.down_health(damage,satiety,energy)
     print("{} наносит удар {}".format(self.name,enemy.name))
     if self.hp > enemy.hp:
         print(self.name + "победил")
     else:
         print(enemy.name + "победил")
    def __str__(self):
        return "{} имеет урон в диапазоне {}-{} очков , {} хп,шкалу сытости в {}-{} и шкалу бодрости {}-{} ".format(
            self.name,
            self.min_damage,
            self.max_damage,
            self.hp,
            self.min_satiety, 
            self.max_satiety,
            self.min_energy, 
            self.max_energy,)

hero1 = Hero("Rk800",20,80,500,1,20,0,20)
hero2 = Hero("Rk900",25,60,100,2,30,0,10)
hero1.run()
hero1.fight(hero2)

for bullet in range(20):
    hero1.fight(hero2)

