class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def __init__(self, speed):
        self.speed = speed
        self._cords = [0, 0, 0]

    def move(self, x, y, z):
        d = self.speed
        dx = d*x
        dy = d*y
        dz = d*z
        if dz < 0:
            print("It's too deep, i can't dive :(")
        else:
            self._cords = [dx, dy, dz]
            return

    def get_cords(self, dx,dy,dz):
        print(f"X: {self._cords[dx]}, Y: {self._cords[dy]} , Z: {self._cords[dz]}")

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        elif self._DEGREE_OF_DANGER >= 5:
            print("Be careful, i'm attacking you 0_0")
        return

class  Bird(Animal):
    beak = True

    def lay_eggs(self, eggs):
        print(f"Here are(is) {self.eggs} eggs for you")
class AquaticAnimal(Animal):
    def dive_in(self, dz):
        self._cords[2] = abs(dz)*(self.speed/2)

class PoisonousAnimal(Animal):

    _DEGREE_OF_DANGER = 8


class Duckbill(Bird, AquaticAnimal, PoisonousAnimal):
    sound = "Click-click-click"
    def __init__(self, speed):
        super().__init__(speed)

    def speak(self):
        print(self.sound)


db = Duckbill(10)

print(db.live)
print(db.beak)

db.speak()
db.attack()

# db.move(1, 2, 3)
# db.get_cords()
# db.dive_in(6)
# db.get_cords()
#
# db.lay_eggs()


print(Duckbill.mro())

