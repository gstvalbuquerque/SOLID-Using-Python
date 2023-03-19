from dataclasses import dataclass


@dataclass
class Player:
    name: str
    team: str
    goals: int = 0


@dataclass
class Team:
    name: str
    score: int = 0


@dataclass
class Scoreboard:
    team1: str
    team2: str

    def update_score(self, team: Team, goals: int = 1) -> None:
        team.score += goals


@dataclass
class SoccerGame:
    player1: Player
    player2: Player
    team1: Team
    team2: Team

    def __post_init__(self) -> None:
        self.scoreboard: Scoreboard = Scoreboard(self.team1, self.team2)

    def score_goal(self, scorer: str) -> None:
        if scorer == self.player1.name:
            self.player1.goals += 1
            self.scoreboard.update_score(self.team1)
        elif scorer == self.player2.name:
            self.player2.goals += 1
            self.scoreboard.update_score(self.team2)

    def game_result(self) -> str:
        print(
            f"Result: {self.team1.name} {self.team1.score} x {self.team2.name} {self.team2.score}")


team1 = Team("PSG")
team2 = Team("Sport")
player1 = Player("Messi", team1.name)
player2 = Player("Juba", team2.name)

soccer_game = SoccerGame(player1, player2, team1, team2)
soccer_game.score_goal("Juba")
soccer_game.score_goal("Juba")
soccer_game.score_goal("Juba")
soccer_game.score_goal("Messi")
soccer_game.game_result()
