from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Pokemon(ABC):
    name: str

    @abstractmethod
    def attack(self):
        pass

    def flee(self):
        print(f"{self.name} fled from battle!")


@dataclass
class FirePokemon(Pokemon):

    def attack(self):
        print(f"{self.name} used flamethrower!")


@dataclass
class WaterPokemon(Pokemon):

    def attack(self):
        print(f"{self.name} used surf!")


@dataclass
class GroundPokemon(Pokemon):

    def attack(self):
        print(f"{self.name} used earthquake!")


pokemon_team: list[Pokemon] = [FirePokemon(
    "Houndoom"), WaterPokemon("Blastoise"), GroundPokemon("Cubone")]
for pokemon in pokemon_team:
    pokemon.attack()
    pokemon.flee()
