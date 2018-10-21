
from Important import max_x,max_y


class Map:
    def __init__(self):
        "nothing"

    def draw_spot(self, x, y, objects):
        """Decide what should be drawn on a given spot"""

        "verify singular objects"
        for i in objects.non_lists:
            j = objects.lists.get(i)
            if (x == j.x and y == j.y):
                return j.mark

        "verify lists"
        for i in objects.list_keys:
            for j in objects.lists.get(i):
                if (x == j.x and y == j.y):
                    return j.mark

        return ' '

    def draw(self, objects):
        y = 0
        hero = objects.lists.get('hero')
        print("")
        print("/--------------------\\")
        while (y < max_y):
            x = 0
            print("|",end='', flush=True)
            while (x < max_x):
                print(self.draw_spot(x, y, objects), end='', flush=True)
                x = x + 1
            if (y == 1):
                print("|   HP", hero.hp)
            elif (y == 2):
                print("|   XP", hero.experience)
            elif (y == 3):
                print("|   G", hero.gold)
            else:
                print("|")
            y = y + 1

        print("\\--------------------/")
        print(">", end='', flush=True)

    def look_at(self, objects, direction):
        look_x = objects.lists.get('hero').x
        look_y = objects.lists.get('hero').y

        if direction == 'w':
            look_y -= 1
        if direction == 's':
            look_y += 1
        if direction == 'a':
            look_x -= 1
        if direction == 'd':
            look_x += 1
        for i in objects.list_keys:
            for j in objects.lists.get(i):
                if (look_x == j.x and look_y == j.y):
                    j.response()

    def attack(self, objects, direction):
        attack_x = objects.lists.get('hero').x
        attack_y = objects.lists.get('hero').y

        if direction == 'i':
            attack_y -= 1
        if direction == 'k':
            attack_y += 1
        if direction == 'j':
            attack_x -= 1
        if direction == 'l':
            attack_x += 1
        for i in objects.list_keys:
            for j in objects.lists.get(i):
                if (attack_x == j.x and attack_y == j.y):
                    result = j.defeat_result()
                    if (result.remove == True):
                        objects.lists.get(i).remove(j)
                    return result
        return 0

    def collision(self, objects):
        for i in objects.list_keys:
            for j in objects.lists.get(i):
                if (objects.lists.get('hero').x == j.x and objects.lists.get('hero').y == j.y):
                    result = j.collision_result()
                    if (result.remove == True):
                        objects.lists.get(i).remove(j)
                    return result
        return 0
