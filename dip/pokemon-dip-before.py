from abc import ABC, abstractmethod
from dataclasses import dataclass


class FlyingType(ABC):
    @abstractmethod
    def fly(self):
        pass


@dataclass
class Pokemon(ABC):
    name: str

    @abstractmethod
    def attack(self):
        pass

    def flee(self):
        print(f"{self.name} fled from battle!")


class FirePokemon(Pokemon):

    def attack(self):
        print(f"{self.name} used flamethrower!")


class WaterPokemon(Pokemon):

    def attack(self):
        print(f"{self.name} used surf!")


class GroundPokemon(Pokemon):

    def attack(self):
        print(f"{self.name} used earthquake!")


class FlyingPokemon(Pokemon, FlyingType):

    def attack(self):
        print(f"{self.name} used wing attack!")

    def fly(self):
        print(f"{self.name} flew away!")


pokemon_team: list[Pokemon] = [FirePokemon(
    "Houndoom"), WaterPokemon("Blastoise"), GroundPokemon("Cubone"), FlyingPokemon("Pidgey")]
for pokemon in pokemon_team:
    pokemon.attack()
    pokemon.flee()

    if isinstance(pokemon, FlyingType):
        pokemon.fly()
