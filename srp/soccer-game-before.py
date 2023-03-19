
from dataclasses import dataclass


@dataclass
class SoccerGame:
    player1_name: str
    player1_team: str

    player2_name: str
    player2_team: str

    team1_name: str
    team2_name: str

    player1_goals: int = 0
    player2_goals: int = 0
    team1_score: int = 0
    team2_score: int = 0

    def score_goal(self, scorer: str) -> None:
        if scorer == self.player1_name:
            self.player1_goals += 1
            self.team1_score += 1
        elif scorer == self.player2_name:
            self.player2_goals += 1
            self.team2_score += 1

    def game_result(self) -> str:
        print(
            f"Result: {self.team1_name} {self.team1_score} x {self.team2_name} {self.team2_score}")


soccer_game = SoccerGame(player1_name="Messi", player1_team="PSG",
                         player2_name="Juba", player2_team="Sport",
                         team1_name="PSG", team2_name="Sport")
soccer_game.score_goal("Juba")
soccer_game.score_goal("Juba")
soccer_game.score_goal("Juba")
soccer_game.score_goal("Messi")
soccer_game.game_result()
