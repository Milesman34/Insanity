from enum import Enum
from string_fns import capitalize

#Enumeration for a type of object (block or item)
class ObjectType(Enum):
    BLOCK = 1
    ITEM = 2

#Class for an object (block or item), which will be inherited from by Block and Item
class Object:
    def __init__(self, official_name, ingame_name=None, object_type=ObjectType.ITEM, recipe=None):
        self.official_name = official_name
        self.object_type = object_type
        self.recipe = recipe

        #If there is no assigned ingame name, it removes the underscores from the official, and capitalizes every word
        self.ingame_name = ingame_name if ingame_name != None else " ".join(list(map(capitalize, official_name.split("_"))))

    #Writes a line to the given file that sets the ingame name of the object
    def write_name(self, file):
        #The string that starts the line
        starting_string = "tile" if self.object_type == ObjectType.BLOCK else "item"

        #Writes the line
        file.write("{}.contenttweaker.{}.name={}\n".format(starting_string, self.official_name, self.ingame_name))

    #Writes the recipe to the given file
    def write_recipe(self, file):
        if self.recipe != None:
            self.recipe.write_recipe(file)

#Class for an item
class Item(Object):
    def __init__(self, official_name, ingame_name=None, recipe=None):
        Object.__init__(self, official_name, ingame_name, ObjectType.ITEM, recipe)

    #Creates the item in the content file
    def write_item(self, file):
        file.write("VanillaFactory.createItem(\"{}\").register();\n".format(self.official_name))

#Class for a block
class Block(Object):
    def __init__(self, official_name, ingame_name=None, tier=None, recipe=None):
        Object.__init__(self, official_name, ingame_name, ObjectType.BLOCK, recipe)

        self.tier = tier

    #Creates the block in the content file
    def write_block(self, file):
        file.write("var {name} = VanillaFactory.createBlock(\"{name}\", <blockmaterial:rock>);\n".format(name=self.official_name))
        file.write("{}.setCreativeTab(<creativetab:buildingBlocks>);\n".format(self.official_name))
        file.write("{}.setBlockHardness({});\n".format(self.official_name, self.tier.hardness))
        file.write("{}.setBlockResistance({});\n".format(self.official_name, self.tier.resistance))
        file.write("{}.setToolClass(\"pickaxe\");\n".format(self.official_name))
        file.write("{}.setToolLevel(0);\n".format(self.official_name))
        file.write("{}.register();\n".format(self.official_name))
