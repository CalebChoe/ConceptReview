class bullet:
    def __init__(self, x, y, width, height, speed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed

    def move(self, time):
        self.x += time * self.speed

class enemy:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

projectile = bullet(10, 10, 1, 1, 5)
monster = enemy(30, 10, 5, 5)

print(f"Position: ({projectile.x}, {projectile.y})")
timeinp = int(input("How long do you want the projectile to move for(seconds): "))

projectile.move(timeinp)

print(f"Position: ({projectile.x}, {projectile.y})")

a = (monster.x + 0-monster.width/2, monster.y)
b = (monster.x, monster.height/2 + monster.y)
c = (monster.x + monster.width/2, monster.y)
d = (monster.x, 0-monster.height/2 + monster.y)

print(a, b, c, d)

xcheck = (monster.x + 0-monster.width/2 <= projectile.x <= monster.x + monster.width/2)
ycheck = (0-monster.height/2 + monster.y <= projectile.y <= monster.height/2 + monster.y)

if xcheck and ycheck:
    print("Hit target!")
else:
    print("Missed!")
