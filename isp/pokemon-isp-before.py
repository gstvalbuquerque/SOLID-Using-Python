from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Pokemon(ABC):
    name: str

    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def fly(self):
        pass

    def flee(self):
        print(f"{self.name} fled from battle!")


class FirePokemon(Pokemon):

    def attack(self):
        print(f"{self.name} used flamethrower!")

    def fly(self):
        print("this pokemon can't fly!")


class WaterPokemon(Pokemon):

    def attack(self):
        print(f"{self.name} used surf!")

    def fly(self):
        print("this pokemon can't fly!")


class GroundPokemon(Pokemon):

    def attack(self):
        print(f"{self.name} used earthquake!")

    def fly(self):
        print("this pokemon can't fly!")


class FlyingPokemon(Pokemon):

    def attack(self):
        print(f"{self.name} used wing attack!")

    def fly(self):
        print(f"{self.name} flew away!")


pokemon_team: list[Pokemon] = [FirePokemon(
    "Houndoom"), WaterPokemon("Blastoise"), GroundPokemon("Cubone"), FlyingPokemon("Pidgey")]
for pokemon in pokemon_team:
    pokemon.attack()
    pokemon.flee()
    pokemon.fly()
