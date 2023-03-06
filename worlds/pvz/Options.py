import typing

from Options import Choice, Range, Option, Toggle, DeathLink, OptionList


class StageRandomizer(Toggle):
    """
    Randomizes the stages in a level.
    """
    display_name = "Stage Randomizer"


class SpeedUpTrap(Toggle):
    """
    Adds Speed Up traps to the item pool
    """
    display_name = "Speed up Trap"


class SpeedDownTrap(Toggle):
    """
    Adds 2x Slow down traps to the item pool
    """
    display_name = "Slow down Trap"


class Goal(Range):
    """
    How many stages you must beat to complete your goal
    """
    display_name = "Goal"
    range_start = 1
    range_end = 50
    default = 25


class NumberOfStartingPlants(Range):
    """
    How many plants you'll begin the game with
    """
    display_name = "Number of Starting Plants"
    range_start = 1
    range_end = 49
    default = 1
    
class Difficultymode (Choice):
    """
    Which difficulty to use
    Easy: Double the normal sun
    Normal: Normal Sun
    Hard: Half the normal Sun
    Extreme: Quarter of the normal Sun
    """
    display_name = "Difficulty"
    option_easy = 0
    option_normal = 1
    option_hard = 2
    option_extreme = 3
    default = 1

class SkipMinigames (Toggle):
    """
    Skip the minigame stages
    """
    display_name = "Skip Minigames?"


pvz_options = {
    "stage_randomizer": StageRandomizer,
    "speedup_trap": SpeedUpTrap,
    "speeddown_trap": SpeedDownTrap,
    "goal": Goal,
    "starting_plant_count": NumberOfStartingPlants,
    "difficulty": Difficultymode,
    "skip_minigames": SkipMinigames,
}