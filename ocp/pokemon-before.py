
from dataclasses import dataclass


@dataclass
class Pokemon:
    name: str

    def fire_attack(self):
        print(f"{self.name} used flamethrower!")

    def water_attack(self):
        print(f"{self.name} used surf!")

    def ground_attack(self):
        print(f"{self.name} used earthquake!")


fire_pokemon = Pokemon("Houndoom")
fire_pokemon.fire_attack()
water_pokemon = Pokemon("Blastoise")
water_pokemon.water_attack()
ground_pokemon = Pokemon("Cubone")
ground_pokemon.ground_attack()
