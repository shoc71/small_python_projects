from dataclasses import dataclass, field
import random
from typing import List, Dict

@dataclass
class Player:
    name : str 
    score : int
    position : int

@dataclass
class Dice:
    original_dice_options: List[int] = field(default_factory=list)
    dice_options: List[int] = field(default_factory=list)
    # value: int
    
    def normal_dice_options(self, options: List[int]) -> None:
        self.dice_options = options
        self.original_dice_options = options

    def negative_dice_options(self, options: List[int]) -> None:
        self.dice_options = [-x for x in options]

    def zero_ing(self, options: List[int]) -> None:
        self.dice_options = [0 for _ in options]

    def roll_dice(self, times: int) -> List[int]:
        return [random.choice(self.dice_options) for _ in range(times)]

    def get_original_dice_options(self) -> List[int]:
        return self.original_dice_options
    
    def multiply_dice_value(self, options : List[int], value:int) -> None:
        self.dice_options = [(x * value) for x in options]

    def divide_dice_value(self, options : List[int], value:int) -> None:
        self.dice_options = [(x / value) for x in options]

    def add_dice_value(self, options : List[int], value:int) -> None:
        self.dice_options = [(x + value) for x in options]

    def subtract_dice_value(self, options : List[int], value:int) -> None:
        self.dice_options = [(x - value) for x in options]

    # def bonus_calculation(self, list):
    #     if list.count(list[0]) == len(list):
    #             print('bonus dickkkkkkkkkkkkkkkkkkkkkkkkkkkkk')
    #             pass

class DicePrinter:
    @staticmethod
    def print_options(options: List[int]) -> None:
        print("Dice options:", options)

    @staticmethod
    def print_records(records: List[int]) -> None:
        print("Rolling results:", records)

class DiceRecord:
    def __init__(self):
        self.records = []
        self.total_score = 0
        self.math_order = ["subtract", "add"]
        self.math_control = ["multiply","divide"]
        self.rolled_numbers = 0

    def calculate_total_score(self) -> int:
        self.total_score = sum(self.records)
        return self.total_score

    def perform_action(self, dice: Dice, action: str, times: int = 1, value: int = 1) -> None:
        if action == "roll":
            self.rolled_numbers = dice.roll_dice(times)
            self.rolled_numbers = [round(x,0) for x in self.rolled_numbers]
            self.records.extend(self.rolled_numbers)
            # bonus for same number rolling
            if self.rolled_numbers.count(self.rolled_numbers[0]) == len(self.rolled_numbers):
                bonus_value = int(sum(self.rolled_numbers) / (2 * len(self.rolled_numbers)))
                print('bonus point(s) - ',bonus_value)
                self.records.append(bonus_value)
            total_score = self.calculate_total_score()
            self.sentence = f"Rolled: {self.rolled_numbers}. All Rolls: {self.records}. Total Score: {total_score}"
        elif action == "zero_ing":
            dice.zero_ing(dice.dice_options)
        elif action == "negative":
            dice.negative_dice_options(dice.dice_options)
        elif action == "set_normal":
            dice.normal_dice_options(dice.get_original_dice_options())
        elif (action in self.math_control) and (value >= 10):
            value = 10
            print("this is not allowed, restore to ",value)
            dice.subtract_dice_value(dice.dice_options, value)
        elif (action in self.math_order) and (value >= 100):
            value = 100
            print("this is not allowed, restore to ",value)
            dice.subtract_dice_value(dice.dice_options, value)
        
        # if action != 'roll':
        print(self.sentence + f" \nAction_Rolled {action}.") #figure out a way to include previous change

class Card(DiceRecord): #idea of this is use to the functions defined in the dice class above and manipulate them as seen fit
    def __init__(self) -> None:
        pass

    def switch_player(self) -> None:
        pass

    # def 

def final_result(*player: Player, dice: Dice) -> None:
    if player < 0:
        player *= -1
        negative_check = True
    pass


def calculate_results(players: Dict[str, Player]) -> None:

    def sort_players(player):
        return player.score

    ranking_players = sorted(players.values(), key=sort_players, reverse=True)
    for i, player in enumerate(ranking_players):
        player.position = i + 1

def main() -> None:
    dice_r6_1 = [1, 2, 3, 4, 5, 6]
    dice_r10_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    dice_r100_1 = [num for num in range(1, 101)]  # List containing numbers from 1 to 100
    dice_r100_2 = [num for num in range(2, 101, 2)]  # List containing even numbers from 2 to 100
    prism_r12_3 = [3, 6, 9, 12]
    coin = [0, 1]

    players = {
        "Duece": Player(name="Duece", score=0, position=0),
        "Shakers": Player(name="Shakers", score=0, position=0),
        # "Player3": Player(name="Player3", score=0, position=0),
        # ...
    }

    # Assign specific dice options to Shakers and Duece
    players["Duece"].dice_options = dice_r6_1
    players["Shakers"].dice_options = dice_r6_1

    # Simulate the game for each player
    for player_name, player in players.items():
        dice = Dice(dice_options=player.dice_options)
        dice_record = DiceRecord()

        # Simulate the game for the current player
        dice_record.perform_action(dice, "roll", times=5)  # Roll the dice 5 times (you can adjust this as needed)
        player.score = dice_record.total_score

    # Calculate positions based on scores
    calculate_results(players)

    # Print player info
    for player_name, player in players.items():
        print(f"Player: {player_name}, Score: {player.score}, Position: {player.position}")

    # print(player_1, player_2)
    # print("Remember the winner is the furtherest away from spawn : 0")

if __name__ == "__main__":
    main()
