import typing
from BaseClasses import Item, ItemClassification


class ItemData(typing.NamedTuple):
    code: typing.Optional[int]
    classification: ItemClassification
    quantity: int = 1


class PVZItem(Item):
    game: str = "Plants vs Zombies"


day_plants_table = {
    "Pea shooter":       ItemData(0, True),
    "Sun Flower":        ItemData(1, True),
    "Cherry bomb":       ItemData(2, True),
    "Wall-nut":          ItemData(3, True),
    "Potato Mine":       ItemData(4, True),
    "Snow Pea":          ItemData(5, True),
    "Chomper":           ItemData(6, True),
    "Repeater":          ItemData(7, True),
}

night_plants_table = {
    "Puff-Shroom":       ItemData(8, True),
    "Sun-Shroom":        ItemData(9, True),
    "Fume-Shroom":       ItemData(10, True),
    "Grave Buster":      ItemData(11, True),
    "Hypno-Shroom":      ItemData(12, True),
    "Scaredy-Shroom":    ItemData(13, True),
    "Ice-Shroom":        ItemData(14, True),
    "Doom-Shroom":       ItemData(15, True),
}

pool_plants_table = {
    "Lily Pad":          ItemData(16, True),
    "Squash":            ItemData(17, True),
    "Threepeater":       ItemData(18, True),
    "Tangle Kelp":       ItemData(19, True),
    "Jalapeno":          ItemData(20, True),
    "Spikeweed":         ItemData(21, True),
    "Torchwood":         ItemData(22, True),
    "Tall-nut":          ItemData(23, True),
}

fog_plants_table = {
    "Sea-Shroom":        ItemData(24, True),
    "Plantern":          ItemData(25, True),
    "Cactus":            ItemData(26, True),
    "Blover":            ItemData(27, True),
    "Split Pea":         ItemData(28, True),
    "Starfruit":         ItemData(29, True),
    "Pumpkin":           ItemData(30, True),
    "Magnet-Shroom":     ItemData(31, True),
}

roof_plants_table = {
    "Cabbage-pult":      ItemData(32, True),
    "Flower Pot":        ItemData(33, True),
    "Kernel-pult":       ItemData(34, True),
    "Coffee Bean":       ItemData(35, True),
    "Garlic":            ItemData(36, True),
    "Umbrella Leaf":     ItemData(37, True),
    "Marigold":          ItemData(38, True),
    "Melon-pult":        ItemData(39, True),
}

upgrade_plants_table = {
    "Gatling Pea":       ItemData(40, True),
    "Twin Sunflower":    ItemData(41, True),
    "Gloom-shroom":      ItemData(42, True),
    "Cattail":           ItemData(43, True),
    "Winter Melon":      ItemData(44, True),
    "Gold Magnet":       ItemData(45, True),
    "Spikerock":         ItemData(46, True),
    "Cob Cannon":        ItemData(47, True),
}

other_plants_table = {
    "Imitator":          ItemData(48, True)
}


item_table = {
    **day_plants_table
    **night_plants_table
    **pool_plants_table
    **fog_plants_table
    **roof_plants_table
    **upgrade_plants_table
    **other_plants_table
}