from dataclasses import dataclass, field
import random
from typing import List

@dataclass
class Dice:
    original_dice_options: List[int] = field(default_factory=list)
    dice_options: List[int] = field(default_factory=list)
    
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

    def calculate_total_score(self) -> int:
        self.total_score = sum(self.records)
        return self.total_score

    def perform_action(self, dice: Dice, action: str, times: int = 1) -> None:
        if action == "roll":
            rolled_numbers = dice.roll_dice(times)
            self.records.extend(rolled_numbers)
            total_score = self.calculate_total_score()
            print(f"Rolled: {rolled_numbers}. All Rolls: {self.records}. Total Score: {total_score}")
        elif action == "zero_ing":
            dice.zero_ing(dice.dice_options)
        elif action == "negative":
            dice.negative_dice_options(dice.dice_options)
        elif action == "set_normal":
            dice.normal_dice_options(dice.get_original_dice_options())

def main() -> None:
    dice_r6_1 = [1, 2, 3, 4, 5, 6]
    dice_r10_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    dice_r100_1 = [num for num in range(1, 101)]  # List containing numbers from 1 to 100
    dice_r100_2 = [num for num in range(2, 101, 2)]  # List containing even numbers from 2 to 100
    coin = [0, 1]

    dice = Dice(dice_options=dice_r6_1)
    dice_printer = DicePrinter()
    dice_record = DiceRecord()

    dice_record.perform_action(dice, "roll", times=5)

    dice.normal_dice_options(dice_r10_1)
    dice_record.perform_action(dice, "negative")
    dice_record.perform_action(dice, "roll", times=5)

    dice.normal_dice_options(coin)
    dice_record.perform_action(dice, "roll", times=3)

    dice.normal_dice_options(dice_r100_1)
    dice_record.perform_action(dice, "roll", times=3)

    dice.normal_dice_options(dice_r100_2)
    dice_record.perform_action(dice, "negative")
    dice_record.perform_action(dice, "roll", times=3)

if __name__ == "__main__":
    main()
