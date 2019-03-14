#A Tier is used for blocks, to determine the hardness, resistance, and tool requirements
class Tier:
    def __init__(self, hardness, resistance):
        self.hardness = hardness
        self.resistance = resistance

#List of all tiers
tiers = {
    "stone": Tier(18.0, 30.0),
    "terracotta": Tier(5.0, 30.0),
    "blue_ice": Tier(1.0, 10.0),
    "soul_sand": Tier(18.0, 30.0),
    "blast_furnace": Tier(18.0, 120.0),
    "steel": Tier(10.0, 120.0),
    "coke_oven": Tier(8.0, 60.0),
    "reinforced_leather": Tier(10.0, 60.0),
    "pyrothite": Tier(40.0, 480.0),
    "platinum": Tier(80.0, 960.0),
    "cryothite": Tier(80.0, 1337.0),
    "pink_ice": Tier(8.0, 137.0),
    "reinforced_obsidian": Tier(9001.0, 34567.0),
    "infernium": Tier(137.0, 2468.0),
    "mithril": Tier(333.0, 12345.0),
    "infernal_coke": Tier(666.0, 666.0),
    "adamantium": Tier(567.0, 24242.0),
    "reinforced steel": Tier(777.0, 77777.0),
    "aerothite": Tier(1000.0, 100000.0),
    "life infused coke": Tier(864.0, 46840.0),
    "altarus": Tier(5040.0, 362880.0),
    "tartarite": Tier(6666.0, 666666.0),
    "cobble2x": Tier(2147483646.0, 2147483646.0),
    "petrothite": Tier(12345.0, 1234567.0),
    "manalite": Tier(32768.0, 2097152.0)
}
