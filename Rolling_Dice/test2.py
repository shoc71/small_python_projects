from dataclasses import dataclass, field
import random
from typing import List

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

    def calculate_total_score(self) -> int:
        self.total_score = sum(self.records)
        return self.total_score

    def perform_action(self, dice: Dice, action: str, times: int = 1, value: int = 1) -> None:
        if action == "roll":
            rolled_numbers = dice.roll_dice(times)
            rolled_numbers = [round(x,0) for x in rolled_numbers]
            self.records.extend(rolled_numbers)
            total_score = self.calculate_total_score()
            self.sentence = f"Rolled: {rolled_numbers}. All Rolls: {self.records}. Total Score: {total_score}"
            # print(self.sentence)
        elif action == "zero_ing":
            dice.zero_ing(dice.dice_options)
        elif action == "negative":
            dice.negative_dice_options(dice.dice_options)
        elif action == "set_normal":
            dice.normal_dice_options(dice.get_original_dice_options())
        # elif action == "multiply":
        #     dice.multiply_dice_value(dice.dice_options, value)
        # elif action == "divide":
        #     dice.divide_dice_value(dice.dice_options, value)
        # elif action == "add":
        #     dice.add_dice_value(dice.dice_options, value)
        # elif action == "subtract":
        #     dice.subtract_dice_value(dice.dice_options, value)
        elif (action in self.math_control) and (value >= 10):
            value = 10
            print("this is not allowed, restore to ",value)
            dice.subtract_dice_value(dice.dice_options, value)
        elif (action in self.math_order) and (value >= 100):
            value = 100
            print("this is not allowed, restore to ",value)
            dice.subtract_dice_value(dice.dice_options, value)
        
        print(self.sentence + f" Action_Rolled {action}.") #figure out a way to include previous change


def main() -> None:
    dice_r6_1 = [1, 2, 3, 4, 5, 6]
    dice_r10_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    dice_r100_1 = [num for num in range(1, 101)]  # List containing numbers from 1 to 100
    dice_r100_2 = [num for num in range(2, 101, 2)]  # List containing even numbers from 2 to 100
    prism_r12_3 = [3, 6, 9, 12]
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

    dice.normal_dice_options(prism_r12_3)
    dice_record.perform_action(dice, "set_normal")
    dice_record.perform_action(dice, "roll", times=2)

    dice.normal_dice_options(dice_r6_1)
    dice_record.perform_action(dice, "multiply", value=130)
    dice_record.perform_action(dice, "roll", times=2)

    dice_record.perform_action(dice, "divide", value=7)
    dice_record.perform_action(dice, "roll", times=2)

    # dice.normal_dice_options(dice_r100_1)
    # dice_record.perform_action(dice, "add", value=125)
    # dice_record.perform_action(dice, "roll", times=2)

    # dice_record.perform_action(dice, "subtract", value=315) # cant have it as a negative number
    # dice_record.perform_action(dice, "roll", times=2)


if __name__ == "__main__":
    main()
