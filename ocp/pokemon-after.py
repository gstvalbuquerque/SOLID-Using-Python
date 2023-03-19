
from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Pokemon(ABC):
    name: str

    @abstractmethod
    def attack(self):
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
    def attack(self):
        print(f"{self.name} used earthquake!")


fire_pokemon = FirePokemon("Houndoom")
fire_pokemon.attack()
water_pokemon = WaterPokemon("Blastoise")
water_pokemon.attack()
ground_pokemon = GroundPokemon("Cubone")
ground_pokemon.attack()
