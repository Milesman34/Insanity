from enum import Enum

#Method used for a recipe
class RecipeMethod(Enum):
    SHAPED2_2 = 1
    SHAPED3_3 = 2
    SHAPED9_9 = 3
    ROD = 4

#Recipes are used to write crafting recipes
class Recipe:
    def __init__(self, recipeMethod=RecipeMethod.SHAPED9_9, result=None, items=None):
        self.recipeMethod = recipeMethod
        self.result = result
        self.items = items

    #Writes a recipe to the file
    def write_recipe(self, file):
        #If the recipe is a square recipe
        is_square = self.recipeMethod != RecipeMethod.ROD

        if self.recipeMethod == RecipeMethod.SHAPED2_2 or self.recipeMethod == RecipeMethod.SHAPED3_3:
            file.write("recipes.addShaped({}, [\n".format(self.result))
        elif self.recipeMethod == RecipeMethod.ROD:
            file.write("mods.extendedcrafting.TableCrafting.addShaped({}, [\n".format(self.result))

            for index, row in enumerate(self.items):
                file.write("[{}]".format(row[0]))

                if index < len(self.items) - 1:
                    file.write(",\n")
        else:
            file.write("mods.extendedcrafting.TableCrafting.addShaped({}, [\n".format(self.result))

        #Iterates through both levels of the array, adding each item
        if is_square:
            for index, row in enumerate(self.items):
                file.write("[")

                for index2, item in enumerate(row):
                    file.write(item)

                    #Commas are only required if it isn't the last item
                    if index2 < len(row) - 1:
                        file.write(",")

                file.write("]")

                if index < len(self.items) - 1:
                    file.write(",\n")

        file.write("]);\n")

#Null placeholder value for a recipe
null = "null"

#Recipe with 81 of a certain item
class Recipe81(Recipe):
    def __init__(self, result, item):
        self.recipeMethod = RecipeMethod.SHAPED9_9
        self.result = result

        #This turns it into a 9x9 array
        self.items = [[item] * 9] * 9

#Recipe with 9 of an item in a vertical line
class RecipeRod(Recipe):
    def __init__(self, result, item):
        self.recipeMethod = RecipeMethod.ROD
        self.result = result

        self.items = [[item]] * 9

#Tier 1 Pickaxe Recipe
class RecipePickaxeT1(Recipe):
    def __init__(self, result, material, rod):
        self.recipeMethod = RecipeMethod.SHAPED9_9
        self.result = result

        self.items = [
            [material, material, material, material, material, material, material, material, material],
            [material, null, null, null, rod, null, null, null, material],
            [material, null, null, null, rod, null, null, null, material],
            [material, null, null, null, rod, null, null, null, material],
            [material, null, null, null, rod, null, null, null, material],
            [null, null, null, null, rod, null, null, null, null],
            [null, null, null, null, rod, null, null, null, null],
            [null, null, null, null, rod, null, null, null, null],
            [null, null, null, null, rod, null, null, null, null],
        ]

#Tier 1 Axe Recipe
class RecipeAxeT1(Recipe):
    def __init__(self, result, material, rod):
        self.recipeMethod = RecipeMethod.SHAPED9_9
        self.result = result

        self.items = [
            [null, null, material, null, null, null, material, null, null],
            [null, null, material, material, null, material, material, null, null],
            [null, null, material, material, material, material, material, null, null],
            [null, null, material, material, rod, material, material, null, null],
            [null, null, material, null, rod, null, material, null, null],
            [null, null, null, null, rod, null, null, null, null],
            [null, null, null, null, rod, null, null, null, null],
            [null, null, null, null, rod, null, null, null, null],
            [null, null, null, null, rod, null, null, null, null],
        ]

#Tier 1 Shovel Recipe
class RecipeShovelT1(Recipe):
    def __init__(self, result, material, rod):
        self.recipeMethod = RecipeMethod.SHAPED9_9
        self.result = result

        self.items = [
            [null, null, null, material, material, material, null, null, null],
            [null, null, null, material, material, material, null, null, null],
            [null, null, null, material, material, material, null, null, null],
            [null, null, null, null, rod, null, null, null, null],
            [null, null, null, null, rod, null, null, null, null],
            [null, null, null, null, rod, null, null, null, null],
            [null, null, null, null, rod, null, null, null, null],
            [null, null, null, null, rod, null, null, null, null],
            [null, null, null, null, rod, null, null, null, null]
        ]

#Tier 1 Hoe Recipe
class RecipeHoeT1(Recipe):
    def __init__(self, result, material, rod):
        self.recipeMethod = RecipeMethod.SHAPED9_9
        self.result = result

        self.items = [
            [null, null, null, null, material, material, material, material, material],
            [null, null, null, null, rod, null, null, null, null],
            [null, null, null, null, rod, null, null, null, null],
            [null, null, null, null, rod, null, null, null, null],
            [null, null, null, null, rod, null, null, null, null],
            [null, null, null, null, rod, null, null, null, null],
            [null, null, null, null, rod, null, null, null, null],
            [null, null, null, null, rod, null, null, null, null],
            [null, null, null, null, rod, null, null, null, null]
        ]

#Tier 1 Sword Recipe
class RecipeSwordT1(Recipe):
    def __init__(self, result, material, rod):
        self.recipeMethod = RecipeMethod.SHAPED9_9
        self.result = result

        self.items = [
            [null, null, null, null, material, null, null, null, null],
            [null, null, null, null, material, null, null, null, null],
            [null, null, null, null, material, null, null, null, null],
            [null, null, null, null, material, null, null, null, null],
            [null, null, null, null, material, null, null, null, null],
            [null, null, null, null, rod, null, null, null, null],
            [null, null, null, null, rod, null, null, null, null],
            [null, null, null, null, rod, null, null, null, null],
            [null, null, null, null, rod, null, null, null, null]
        ]

#A recipe with a layer surrounding a 7x7 square
class RecipeSurrounding(Recipe):
    def __init__(self, result, item1, item2):
        self.recipeMethod = RecipeMethod.SHAPED9_9
        self.result = result

        #A row of 9 items
        row1 = [[item1] * 9]

        #A row of 7 items, surrounded by 2 other items
        row2 = [[item1] + [item2] * 7 + [item1]]

        self.items = row1 + row2 * 7 + row1

        self.items = [
            [item1, item1, item1, item1, item1, item1, item1, item1, item1],
            [item1, item2, item2, item2, item2, item2, item2, item2, item1],
            [item1, item2, item2, item2, item2, item2, item2, item2, item1],
            [item1, item2, item2, item2, item2, item2, item2, item2, item1],
            [item1, item2, item2, item2, item2, item2, item2, item2, item1],
            [item1, item2, item2, item2, item2, item2, item2, item2, item1],
            [item1, item2, item2, item2, item2, item2, item2, item2, item1],
            [item1, item2, item2, item2, item2, item2, item2, item2, item1],
            [item1, item1, item1, item1, item1, item1, item1, item1, item1]
        ]

#A recipe with 2 layers surrounding a 5x5 square
class Recipe2xSurrounding(Recipe):
    def __init__(self, result, item1, item2, item3):
        self.recipeMethod = RecipeMethod.SHAPED9_9
        self.result = result

        self.items = [
            [item1, item1, item1, item1, item1, item1, item1, item1, item1],
            [item1, item2, item2, item2, item2, item2, item2, item2, item1],
            [item1, item2, item3, item3, item3, item3, item3, item2, item1],
            [item1, item2, item3, item3, item3, item3, item3, item2, item1],
            [item1, item2, item3, item3, item3, item3, item3, item2, item1],
            [item1, item2, item3, item3, item3, item3, item3, item2, item1],
            [item1, item2, item3, item3, item3, item3, item3, item2, item1],
            [item1, item2, item2, item2, item2, item2, item2, item2, item1],
            [item1, item1, item1, item1, item1, item1, item1, item1, item1]
        ]

#A recipe with 2 layers surrounding a 5x5 checkerboard
class Recipe2xSurroundingCheckerboard(Recipe):
    def __init__(self, result, item1, item2, item3, item4):
        self.recipeMethod = RecipeMethod.SHAPED9_9
        self.result = result

        self.items = [
            [item1, item1, item1, item1, item1, item1, item1, item1, item1],
            [item1, item2, item2, item2, item2, item2, item2, item2, item1],
            [item1, item2, item3, item4, item3, item4, item3, item2, item1],
            [item1, item2, item4, item3, item4, item3, item4, item2, item1],
            [item1, item2, item3, item4, item3, item4, item3, item2, item1],
            [item1, item2, item4, item3, item4, item3, item4, item2, item1],
            [item1, item2, item3, item4, item3, item4, item3, item2, item1],
            [item1, item2, item2, item2, item2, item2, item2, item2, item1],
            [item1, item1, item1, item1, item1, item1, item1, item1, item1]
        ]

#A recipe with a grate pattern, as used for iron bars. Alternating rows of checkerboard and 9 of one item
class RecipeGrate(Recipe):
    def __init__(self, result, item1, item2):
        self.recipeMethod = RecipeMethod.SHAPED9_9
        self.result = result

        #A row of alternating items
        row1 = [[item1, item2, item1, item2, item1, item2, item1, item2, item1]]

        #A row of 9 items
        row2 = [[item2] * 9]

        self.items = row1 + row2 + row1 + row2 + row1 + row2 + row1 + row2 + row1

        self.items = [
            [item1, item2, item1, item2, item1, item2, item1, item2, item1],
            [item2, item2, item2, item2, item2, item2, item2, item2, item2],
            [item1, item2, item1, item2, item1, item2, item1, item2, item1],
            [item2, item2, item2, item2, item2, item2, item2, item2, item2],
            [item1, item2, item1, item2, item1, item2, item1, item2, item1],
            [item2, item2, item2, item2, item2, item2, item2, item2, item2],
            [item1, item2, item1, item2, item1, item2, item1, item2, item1],
            [item2, item2, item2, item2, item2, item2, item2, item2, item2],
            [item1, item2, item1, item2, item1, item2, item1, item2, item1]
        ]

#A recipe in an anvil pattern, with other blocks filled in
class RecipeFilledAnvil(Recipe):
    def __init__(self, result, item1, item2):
        self.recipeMethod = RecipeMethod.SHAPED9_9
        self.result = result

        #A row of 9 items
        row1 = [[item1] * 9]

        #A row with 1 item in the middle surrounded by 4 other items on each side
        row2 = [[item2] * 4 + [item1] + [item2] * 4]

        self.items = row1 + row2 * 7 + row1

        self.items = [
            [item1, item1, item1, item1, item1, item1, item1, item1, item1],
            [item2, item2, item2, item2, item1, item2, item2, item2, item2],
            [item2, item2, item2, item2, item1, item2, item2, item2, item2],
            [item2, item2, item2, item2, item1, item2, item2, item2, item2],
            [item2, item2, item2, item2, item1, item2, item2, item2, item2],
            [item2, item2, item2, item2, item1, item2, item2, item2, item2],
            [item2, item2, item2, item2, item1, item2, item2, item2, item2],
            [item2, item2, item2, item2, item1, item2, item2, item2, item2],
            [item1, item1, item1, item1, item1, item1, item1, item1, item1]
        ]

#Tier 2 Pickaxe Recipe
class RecipePickaxeT2(Recipe):
    def __init__(self, result, material, rod, item):
        self.recipeMethod = RecipeMethod.SHAPED9_9
        self.result = result

        self.items = [
            [material, material, material, material, material, material, material, material, material],
            [material, item, item, item, rod, item, item, item, material],
            [material, item, item, item, rod, item, item, item, material],
            [material, item, item, item, rod, item, item, item, material],
            [material, item, item, item, rod, item, item, item, material],
            [item, item, item, item, rod, item, item, item, item],
            [item, item, item, item, rod, item, item, item, item],
            [item, item, item, item, rod, item, item, item, item],
            [item, item, item, item, rod, item, item, item, item],
        ]

#Tier 2 Axe Recipe
class RecipeAxeT2(Recipe):
    def __init__(self, result, material, rod, item):
        self.recipeMethod = RecipeMethod.SHAPED9_9
        self.result = result

        self.items = [
            [item, item, material, item, item, item, material, item, item],
            [item, item, material, material, item, material, material, item, item],
            [item, item, material, material, material, material, material, item, item],
            [item, item, material, material, rod, material, material, item, item],
            [item, item, material, item, rod, item, material, item, item],
            [item, item, item, item, rod, item, item, item, item],
            [item, item, item, item, rod, item, item, item, item],
            [item, item, item, item, rod, item, item, item, item],
            [item, item, item, item, rod, item, item, item, item],
        ]

#Tier 2 Shovel Recipe
class RecipeShovelT2(Recipe):
    def __init__(self, result, material, rod, item):
        self.recipeMethod = RecipeMethod.SHAPED9_9
        self.result = result

        self.items = [
            [item, item, item, material, material, material, item, item, item],
            [item, item, item, material, material, material, item, item, item],
            [item, item, item, material, material, material, item, item, item],
            [item, item, item, item, rod, item, item, item, item],
            [item, item, item, item, rod, item, item, item, item],
            [item, item, item, item, rod, item, item, item, item],
            [item, item, item, item, rod, item, item, item, item],
            [item, item, item, item, rod, item, item, item, item],
            [item, item, item, item, rod, item, item, item, item]
        ]

#Tier 2 Hoe Recipe
class RecipeHoeT2(Recipe):
    def __init__(self, result, material, rod, item):
        self.recipeMethod = RecipeMethod.SHAPED9_9
        self.result = result

        self.items = [
            [item, item, item, item, material, material, material, material, material],
            [item, item, item, item, rod, item, item, item, item],
            [item, item, item, item, rod, item, item, item, item],
            [item, item, item, item, rod, item, item, item, item],
            [item, item, item, item, rod, item, item, item, item],
            [item, item, item, item, rod, item, item, item, item],
            [item, item, item, item, rod, item, item, item, item],
            [item, item, item, item, rod, item, item, item, item],
            [item, item, item, item, rod, item, item, item, item]
        ]

#Tier 2 Sword Recipe
class RecipeSwordT2(Recipe):
    def __init__(self, result, material, rod, item):
        self.recipeMethod = RecipeMethod.SHAPED9_9
        self.result = result

        self.items = [
            [item, item, item, item, material, item, item, item, item],
            [item, item, item, item, material, item, item, item, item],
            [item, item, item, item, material, item, item, item, item],
            [item, item, item, item, material, item, item, item, item],
            [item, item, item, item, material, item, item, item, item],
            [item, item, item, item, rod, item, item, item, item],
            [item, item, item, item, rod, item, item, item, item],
            [item, item, item, item, rod, item, item, item, item],
            [item, item, item, item, rod, item, item, item, item]
        ]

#Checkerboard Recipe
class RecipeCheckerboard(Recipe):
    def __init__(self, result, item1, item2):
        self.recipeMethod = RecipeMethod.SHAPED9_9
        self.result = result

        self.items = [
            [item1, item2, item1, item2, item1, item2, item1, item2, item1],
            [item2, item1, item2, item1, item2, item1, item2, item1, item2],
            [item1, item2, item1, item2, item1, item2, item1, item2, item1],
            [item2, item1, item2, item1, item2, item1, item2, item1, item2],
            [item1, item2, item1, item2, item1, item2, item1, item2, item1],
            [item2, item1, item2, item1, item2, item1, item2, item1, item2],
            [item1, item2, item1, item2, item1, item2, item1, item2, item1],
            [item2, item1, item2, item1, item2, item1, item2, item1, item2],
            [item1, item2, item1, item2, item1, item2, item1, item2, item1]
        ]

#Bow Recipe
class RecipeBow(Recipe):
    def __init__(self, result, item1, item2, rod, filler):
        self.recipeMethod = RecipeMethod.SHAPED9_9
        self.result = result

        self.items = [
            [filler, filler, filler, rod, rod, rod, rod, rod, item2],
            [filler, filler, rod, filler, filler, filler, filler, filler, item2],
            [filler, rod, filler, filler, filler, filler, filler, filler, item2],
            [item1, filler, filler, filler, filler, filler, filler, filler, item2],
            [item1, filler, filler, filler, filler, filler, filler, filler, item2],
            [item1, filler, filler, filler, filler, filler, filler, filler, item2],
            [filler, rod, filler, filler, filler, filler, filler, filler, item2],
            [filler, filler, rod, filler, filler, filler, filler, filler, item2],
            [filler, filler, filler, rod, rod, rod, rod, rod, item2]
        ]

#Arrow Recipe
class RecipeArrow(Recipe):
    def __init__(self, result, item1, item2, rod, filler):
        self.recipeMethod = RecipeMethod.SHAPED9_9
        self.result = result

        self.items = [
            [filler, filler, filler, filler, item1, filler, filler, filler, filler],
            [filler, filler, filler, filler, item1, filler, filler, filler, filler],
            [filler, filler, filler, filler, item1, filler, filler, filler, filler],
            [filler, filler, filler, filler, rod, filler, filler, filler, filler],
            [filler, filler, filler, filler, rod, filler, filler, filler, filler],
            [filler, filler, filler, filler, rod, filler, filler, filler, filler],
            [filler, filler, filler, filler, item2, filler, filler, filler, filler],
            [filler, filler, filler, filler, item2, filler, filler, filler, filler],
            [filler, filler, filler, filler, item2, filler, filler, filler, filler]
        ]

#Helmet Recipe
class RecipeHelmet(Recipe):
    def __init__(self, result, item, filler):
        self.recipeMethod = RecipeMethod.SHAPED9_9
        self.result = result

        self.items = [
            [item, item, item, item, item, item, item, item, item],
            [item, item, item, item, item, item, item, item, item],
            [item, item, filler, filler, filler, filler, filler, item, item],
            [item, item, filler, filler, filler, filler, filler, item, item],
            [item, item, filler, filler, filler, filler, filler, item, item],
            [item, item, filler, filler, filler, filler, filler, item, item],
            [item, item, filler, filler, filler, filler, filler, item, item],
            [item, item, filler, filler, filler, filler, filler, item, item],
            [item, item, filler, filler, filler, filler, filler, item, item]
        ]

#Chestplate Recipe
class RecipeChestplate(Recipe):
    def __init__(self, result, item, filler):
        self.recipeMethod = RecipeMethod.SHAPED9_9
        self.result = result

        self.items = [
            [item, item, filler, filler, filler, filler, filler, item, item],
            [item, item, item, filler, filler, filler, item, item, item],
            [item, item, item, item, item, item, item, item, item],
            [item, item, item, item, item, item, item, item, item],
            [item, item, item, item, item, item, item, item, item],
            [item, item, item, item, item, item, item, item, item],
            [item, item, item, item, item, item, item, item, item],
            [item, item, item, item, item, item, item, item, item],
            [item, item, item, item, item, item, item, item, item],
        ]

#Leggings Recipe
class RecipeLeggings(Recipe):
    def __init__(self, result, item, filler):
        self.recipeMethod = RecipeMethod.SHAPED9_9
        self.result = result

        self.items = [
            [item, item, item, item, item, item, item, item, item],
            [item, item, item, item, item, item, item, item, item],
            [item, item, item, filler, filler, filler, item, item, item],
            [item, item, item, filler, filler, filler, item, item, item],
            [item, item, item, filler, filler, filler, item, item, item],
            [item, item, item, filler, filler, filler, item, item, item],
            [item, item, item, filler, filler, filler, item, item, item],
            [item, item, item, filler, filler, filler, item, item, item],
            [item, item, item, filler, filler, filler, item, item, item]
        ]

#Boots Recipe
class RecipeBoots(Recipe):
    def __init__(self, result, item, filler):
        self.recipeMethod = RecipeMethod.SHAPED9_9
        self.result = result

        self.items = [
            [item, item, filler, filler, filler, filler, filler, item, item],
            [item, item, filler, filler, filler, filler, filler, item, item],
            [item, item, filler, filler, filler, filler, filler, item, item],
            [item, item, filler, filler, filler, filler, filler, item, item],
            [item, item, filler, filler, filler, filler, filler, item, item],
            [item, item, filler, filler, filler, filler, filler, item, item],
            [item, item, filler, filler, filler, filler, filler, item, item],
            [item, item, filler, filler, filler, filler, filler, item, item],
            [item, item, filler, filler, filler, filler, filler, item, item]
        ]

#Buckets Recipe
class RecipeBucket(Recipe):
    def __init__(self, result, item, filler):
        self.recipeMethod = RecipeMethod.SHAPED9_9
        self.result = result

        self.items = [
            [item, filler, filler, filler, filler, filler, filler, filler, item],
            [filler, item, filler, filler, filler, filler, filler, item, filler],
            [filler, filler, item, filler, filler, filler, item, filler, filler],
            [filler, filler, filler, item, filler, item, filler, filler, filler],
            [filler, filler, filler, filler, item, filler, filler, filler, filler],
            [filler, filler, filler, filler, filler, filler, filler, filler, filler],
            [filler, filler, filler, filler, filler, filler, filler, filler, filler],
            [filler, filler, filler, filler, filler, filler, filler, filler, filler],
            [filler, filler, filler, filler, filler, filler, filler, filler, filler]
        ]

#Fishing Rod Recipe
class RecipeFishingRod(Recipe):
    def __init__(self, result, item, rod, filler):
        self.recipeMethod = RecipeMethod.SHAPED9_9
        self.result = result

        self.items = [
            [filler, filler, filler, filler, filler, filler, filler, filler, rod],
            [filler, filler, filler, filler, filler, filler, filler, rod, item],
            [filler, filler, filler, filler, filler, filler, rod, filler, item],
            [filler, filler, filler, filler, filler, rod, filler, filler, item],
            [filler, filler, filler, filler, rod, filler, filler, filler, item],
            [filler, filler, filler, rod, filler, filler, filler, filler, item],
            [filler, filler, rod, filler, filler, filler, filler, filler, item],
            [filler, rod, filler, filler, filler, filler, filler, filler, item],
            [rod, filler, filler, filler, filler, filler, filler, filler, item]
        ]


#Shears Recipe
class RecipeShears(Recipe):
    def __init__(self, result, item, filler):
        self.recipeMethod = RecipeMethod.SHAPED9_9
        self.result = result

        #First 2 rows
        row1 = [[item] * 7 + [filler] * 2]
        row2 = [[item] + [filler] * 8]

        #7 items, surrounded on both sides by 1 other item
        row3 = [[item] + [filler] * 7 + [item]]

        #Row of 9 items
        row4 = [[item] * 9]

        self.items = row1 + row2 + row3 * 6 + row4

        self.items = [
            [item, item, item, item, item, item, item, filler, filler],
            [item, filler, filler, filler, filler, filler, filler, filler, filler],
            [item, filler, filler, filler, filler, filler, filler, filler, item],
            [item, filler, filler, filler, filler, filler, filler, filler, item],
            [item, filler, filler, filler, filler, filler, filler, filler, item],
            [item, filler, filler, filler, filler, filler, filler, filler, item],
            [item, filler, filler, filler, filler, filler, filler, filler, item],
            [item, filler, filler, filler, filler, filler, filler, filler, item],
            [item, item, item, item, item, item, item, item, item]
        ]

#Lead Recipe
class RecipeLead(Recipe):
    def __init__(self, result, item1, item2, item3, filler):
        self.recipeMethod = RecipeMethod.SHAPED9_9
        self.result = result

        self.items = [
            [filler, filler, filler, filler, filler, filler, filler, filler, filler],
            [filler, item1, item1, item1, item2, item2, item3, item3, filler],
            [filler, item1, item1, item1, item2, item2, item3, item3, filler],
            [filler, item1, item1, item2, item2, item2, item3, item3, filler],
            [filler, item1, item1, item2, item2, filler, item3, item3, filler],
            [filler, item1, item1, item2, item2, item2, item3, item3, filler],
            [filler, item1, item1, item2, item2, item3, item3, item3, filler],
            [filler, item1, item1, item2, item2, item3, item3, item3, filler],
            [filler, filler, filler, filler, filler, filler, filler, filler, filler]
        ]

#Name Tag Recipe
class RecipeNameTag(Recipe):
    def __init__(self, result, item1, item2, item3, item4, filler):
        self.recipeMethod = RecipeMethod.SHAPED9_9
        self.result = result

        self.items = [
            [item1, item1, item1, item1, item1, item1, item1, item1, item1],
            [filler, filler, filler, item2, item3, item2, filler, filler, filler],
            [filler, filler, filler, item2, item3, item2, filler, filler, filler],
            [filler, filler, filler, item2, item3, item2, filler, filler, filler],
            [filler, filler, filler, item2, item3, item2, filler, filler, filler],
            [filler, filler, filler, item2, item3, item2, filler, filler, filler],
            [filler, filler, filler, item2, item3, item2, filler, filler, filler],
            [filler, filler, filler, item2, item3, item2, filler, filler, filler],
            [item4, item4, item4, item4, item4, item4, item4, item4, item4]
        ]

#Toolmaker Recipe
class RecipeToolmaker(Recipe):
    def __init__(self, result, item, tool1, tool2, tool3, tool4, tool5):
        self.recipeMethod = RecipeMethod.SHAPED9_9
        self.result = result

        self.items = [
            [item, item, item, item, item, item, item, item, item],
            [item, item, item, item, item, item, item, item, item],
            [item, item, tool1, tool1, tool1, tool1, tool1, item, item],
            [item, item, tool2, tool2, tool2, tool2, tool2, item, item],
            [item, item, tool3, tool3, tool3, tool3, tool3, item, item],
            [item, item, tool4, tool4, tool4, tool4, tool4, item, item],
            [item, item, tool5, tool5, tool5, tool5, tool5, item, item],
            [item, item, item, item, item, item, item, item, item],
            [item, item, item, item, item, item, item, item, item],
        ]

#Freezer Recipe
class RecipeFreezer(Recipe):
    def __init__(self, result, item1, item2):
        self.recipeMethod = RecipeMethod.SHAPED9_9
        self.result = result

        self.items = [
            [item1, item1, item1, item1, item1, item1, item1, item1, item1],
            [item1, item2, item1, item2, item1, item2, item1, item2, item1],
            [item1, item1, item2, item2, item2, item2, item2, item1, item1],
            [item1, item2, item2, item2, item2, item2, item2, item2, item1],
            [item1, item1, item2, item2, item2, item2, item2, item1, item1],
            [item1, item2, item2, item2, item2, item2, item2, item2, item1],
            [item1, item1, item2, item2, item2, item2, item2, item1, item1],
            [item1, item2, item1, item2, item1, item2, item1, item2, item1],
            [item1, item1, item1, item1, item1, item1, item1, item1, item1],
        ]

#Armormaker Recipe
class RecipeArmormaker(Recipe):
    def __init__(self, result, item, armor1, armor2, armor3, armor4):
        self.recipeMethod = RecipeMethod.SHAPED9_9
        self.result = result

        self.items = [
            [item, item, item, item, item, item, item, item, item],
            [item, item, item, item, item, item, item, item, item],
            [item, item, item, item, item, item, item, item, item],
            [item, item, item, armor1, armor1, armor1, armor1, item, item],
            [item, item, item, armor2, armor2, armor2, armor2, item, item],
            [item, item, item, armor3, armor3, armor3, armor3, item, item],
            [item, item, item, armor4, armor4, armor4, armor4, item, item],
            [item, item, item, item, item, item, item, item, item],
            [item, item, item, item, item, item, item, item, item]
        ]

#Castmaker Recipe
class RecipeCastmaker(Recipe):
    def __init__(self, result, item1, item2):
        self.recipeMethod = RecipeMethod.SHAPED9_9
        self.result = result

        self.items = [
            [item1, item1, item1, item1, item1, item1, item1, item1, item1],
            [item1, item1, item2, item2, item2, item2, item2, item1, item1],
            [item1, item2, item2, item2, item2, item2, item2, item2, item1],
            [item1, item2, item2, item2, item2, item2, item2, item2, item1],
            [item1, item2, item2, item2, item2, item2, item2, item2, item1],
            [item1, item2, item2, item2, item2, item2, item2, item2, item1],
            [item1, item2, item2, item2, item2, item2, item2, item2, item1],
            [item1, item1, item2, item2, item2, item2, item2, item1, item1],
            [item1, item1, item1, item1, item1, item1, item1, item1, item1]
        ]

#Dust Refiner Recipe
class RecipeDustRefiner(Recipe):
    def __init__(self, result, item1, item2, item3, item4, item5):
        self.recipeMethod = RecipeMethod.SHAPED9_9
        self.result = result

        self.items = [
            [item1, item1, item1, item1, item1, item1, item1, item1, item1],
            [item1, item2, item2, item2, item2, item2, item2, item2, item1],
            [item1, item2, item3, item3, item4, item5, item5, item2, item1],
            [item1, item2, item3, item3, item4, item5, item5, item2, item1],
            [item1, item2, item3, item3, item4, item5, item5, item2, item1],
            [item1, item2, item3, item3, item4, item5, item5, item2, item1],
            [item1, item2, item3, item3, item4, item5, item5, item2, item1],
            [item1, item2, item2, item2, item2, item2, item2, item2, item1],
            [item1, item1, item1, item1, item1, item1, item1, item1, item1]
        ]

#Basin Recipe
class RecipeBasin(Recipe):
    def __init__(self, result, item1, item2):
        self.recipeMethod = RecipeMethod.SHAPED9_9
        self.result = result

        self.items = [
            [item1, item2, item2, item2, item2, item2, item2, item2, item1],
            [item1, item2, item2, item2, item2, item2, item2, item2, item1],
            [item1, item2, item2, item2, item2, item2, item2, item2, item1],
            [item1, item2, item2, item2, item2, item2, item2, item2, item1],
            [item1, item2, item2, item2, item2, item2, item2, item2, item1],
            [item1, item2, item2, item2, item2, item2, item2, item2, item1],
            [item1, item2, item2, item2, item2, item2, item2, item2, item1],
            [item1, item2, item2, item2, item2, item2, item2, item2, item1],
            [item1, item1, item1, item1, item1, item1, item1, item1, item1]
        ]

#Nugget Cast Recipe
class RecipeNuggetCast(Recipe):
    def __init__(self, result, item1, item2, item3):
        self.recipeMethod = RecipeMethod.SHAPED9_9
        self.result = result

        self.items = [
            [item1, item1, item1, item1, item1, item1, item1, item1, item1],
            [item1, item2, item3, item3, item3, item2, item2, item2, item1],
            [item1, item3, item3, item3, item3, item2, item2, item2, item1],
            [item1, item3, item3, item3, item3, item3, item3, item2, item1],
            [item1, item3, item3, item3, item3, item3, item3, item2, item1],
            [item1, item2, item3, item3, item3, item3, item2, item2, item1],
            [item1, item2, item3, item3, item3, item3, item2, item2, item1],
            [item1, item2, item2, item3, item3, item2, item2, item2, item1],
            [item1, item1, item1, item1, item1, item1, item1, item1, item1],
        ]

#Molten Steel Recipe
class RecipeMoltenSteel(Recipe):
    def __init__(self, result, item1, item2, item3, item4, item5, item6):
        self.recipeMethod = RecipeMethod.SHAPED9_9
        self.result = result

        self.items = [
            [item1, item1, item1, item1, item1, item1, item1, item1, item1],
            [item1, item2, item2, item2, item2, item2, item2, item2, item1],
            [item1, item2, item3, item3, item4, item4, item6, item2, item1],
            [item1, item2, item3, item3, item4, item4, item6, item2, item1],
            [item1, item2, item3, item3, item5, item6, item6, item2, item1],
            [item1, item2, item3, item4, item4, item6, item6, item2, item1],
            [item1, item2, item3, item4, item4, item6, item6, item2, item1],
            [item1, item2, item2, item2, item2, item2, item2, item2, item1],
            [item1, item1, item1, item1, item1, item1, item1, item1, item1]
        ]

#Cutter Recipe
class RecipeCutter(Recipe):
    def __init__(self, result, item1, item2):
        self.recipeMethod = RecipeMethod.SHAPED9_9
        self.result = result

        self.items = [
            [item1, item1, item1, item1, item1, item1, item1, item1, item1],
            [item2, item2, item2, item2, item2, item2, item2, item2, item2],
            [item2, item2, item2, item2, item2, item2, item2, item2, item2],
            [item2, item2, item2, item2, item2, item2, item2, item2, item2],
            [item2, item2, item2, item2, item2, item2, item2, item2, item2],
            [item2, item2, item2, item2, item2, item2, item2, item2, item2],
            [item2, item2, item2, item2, item2, item2, item2, item2, item2],
            [item2, item2, item2, item2, item2, item2, item2, item2, item2],
            [item2, item2, item2, item2, item2, item2, item2, item2, item2]        ]

#Chemistry Station Crafting Recipe
class RecipeChemistryStationCrafting(Recipe):
    def __init__(self, result, item1, item2, item3, item4, item5, item6):
        self.recipeMethod = RecipeMethod.SHAPED9_9
        self.result = result

        self.items = [
            [item1, item1, item1, item1, item1, item1, item1, item1, item1],
            [item1, item3, item3, item3, item2, item4, item4, item4, item1],
            [item1, item3, item3, item3, item2, item4, item4, item4, item1],
            [item1, item3, item3, item3, item2, item4, item4, item4, item1],
            [item1, item2, item2, item2, item2, item2, item2, item2, item1],
            [item1, item5, item5, item5, item2, item6, item6, item6, item1],
            [item1, item5, item5, item5, item2, item6, item6, item6, item1],
            [item1, item5, item5, item5, item2, item6, item6, item6, item1],
            [item1, item1, item1, item1, item1, item1, item1, item1, item1]
        ]

#Alloying Recipe
class RecipeAlloying(Recipe):
    def __init__(self, result, item1, item2, item3, item4):
        self.recipeMethod = RecipeMethod.SHAPED9_9
        self.result = result

        self.items = [
            [item1, item1, item1, item1, item1, item1, item1, item1, item1],
            [item1, item2, item2, item2, item3, item4, item4, item4, item1],
            [item1, item2, item2, item2, item3, item4, item4, item4, item1],
            [item1, item2, item2, item2, item3, item4, item4, item4, item1],
            [item1, item2, item2, item2, item3, item4, item4, item4, item1],
            [item1, item2, item2, item2, item3, item4, item4, item4, item1],
            [item1, item2, item2, item2, item3, item4, item4, item4, item1],
            [item1, item2, item2, item2, item3, item4, item4, item4, item1],
            [item1, item1, item1, item1, item1, item1, item1, item1, item1]
        ]
