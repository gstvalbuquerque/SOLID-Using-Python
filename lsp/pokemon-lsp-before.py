
from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Pokemon(ABC):
    name: str

    @abstractmethod
    def attack(self, move: str):
        pass


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

    def flee(self):
        print(f"{self.name} fled from battle!")


pokemon_team: list[Pokemon] = [FirePokemon(
    "Houndoom"), WaterPokemon("Blastoise"), GroundPokemon("Cubone")]
for pokemon in pokemon_team:
    pokemon.attack()
