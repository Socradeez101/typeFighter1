print("Hello welcome to Type Fighter , this is an exciting game that test your typing speed")
import random
import threading
import time

words_for_goblin = ["crab", "grow", "screw"]
words_for_minion_and_giant = ["abroad", "accept", "access", "agenda", "almost", "copper", "corner", "costly"]

class Player():
    def __init__(self, health, damage):
        self.health = health
        self.damage = damage

    def health_dec(self):
        self.health = (self.health - 20)

player = Player(100, 20)

stats = input("do you want to see your stats : ")
if stats == "yes":
    print(player.__dict__)


enemy_choice = input("choose your enemy \ngoblin(easy) - 2 seconds\word \nminion(medium) - 1.5 seconds\word \ngiant(hard) - 1 second\word \n: ")
if enemy_choice == "goblin":
    t = 10
    def countdown_for_goblin(t):
        for i in range(t):
            tts = str(t - i) + "seconds remain"
            time.sleep(1)
            if tts == "1seconds remain":
                print("game over")
    t1 = threading.Thread(countdown_for_goblin(t), t)
    t1.start()

class enemy():
    def __init__(self, health, damage):
        self.damage = damage
        self.health = health

    def health_dec(self):
        self.health = (self.health - 20)


if enemy_choice == "goblin":
    goblin = enemy(100, 20)
    print(goblin.__dict__)
elif enemy_choice == "giant":
    giant = enemy(140, 25)
    print(giant.__dict__)
elif enemy_choice == "minion":
    minion = enemy(100, 20)
    print(minion.__dict__)
else:
    print("choose appropriate enemy")

# part 3 fight
approval = input("the game is about to begin, are you ready : ")
if approval == "yes":
    if enemy_choice == "goblin":
        t = 6
        t1.start()
        t1.join()
        while player.health != 0 or goblin.health != 0:
            on_screen = random.choice(words_for_goblin)
            print(on_screen)
            ans = input("type the word on screen :")
            if ans == on_screen:
                goblin.health_dec()
                print(goblin.health)
            elif ans != on_screen:
                print("wrong word")
                player.health_dec()
                print(player.health)
            if player.health == 0:
                print("you died")
                break
            if goblin.health == 0:
                print("enemy defeated")
                break
