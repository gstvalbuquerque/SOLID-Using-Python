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


class IPokemonFactory(ABC):
    @abstractmethod
    def create_fire_pokemon(self, name: str) -> Pokemon:
        pass

    @abstractmethod
    def create_water_pokemon(self, name: str) -> Pokemon:
        pass

    @abstractmethod
    def create_ground_pokemon(self, name: str) -> Pokemon:
        pass

    @abstractmethod
    def create_flying_pokemon(self, name: str) -> Pokemon:
        pass


class PokemonFactory(IPokemonFactory):
    def create_fire_pokemon(self, name: str) -> Pokemon:
        return FirePokemon(name)

    def create_water_pokemon(self, name: str) -> Pokemon:
        return WaterPokemon(name)

    def create_ground_pokemon(self, name: str) -> Pokemon:
        return GroundPokemon(name)

    def create_flying_pokemon(self, name: str) -> Pokemon:
        return FlyingPokemon(name)


pokemon_factory = PokemonFactory()
pokemon_team: list[Pokemon] = [
    pokemon_factory.create_fire_pokemon("Charmander"),
    pokemon_factory.create_water_pokemon("Squirtle"),
    pokemon_factory.create_ground_pokemon("Cubone"),
    pokemon_factory.create_flying_pokemon("Pidgey")
]

for pokemon in pokemon_team:
    pokemon.attack()
    pokemon.flee()

    if isinstance(pokemon, FlyingType):
        pokemon.fly()
