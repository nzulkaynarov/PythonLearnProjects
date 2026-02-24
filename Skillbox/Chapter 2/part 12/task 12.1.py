class Air:
    def __str__(self):
        return 'Воздух'

class Fire:
    def __str__(self):
        return 'Огонь'

class Earth:
    def __str__(self):
        return 'Земля'

class Water:
    def __str__(self):
        return 'Вода'
    def __add__(self, other):
        if isinstance(other, Fire):
            return Vape()
        else:
            return None


class Vape:
    def __str__(self):
        return 'Пар'

water = Water()
fire = Fire()

print(water + earth)