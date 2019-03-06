from blocks import *
from items import *
from block_recipes import *
from item_recipes import *

"""File Creation"""
#Creates the content file
with open("content2.zs", "w+") as file:
    print("Started writing content2.zs")

    #File header
    file.write("#loader contenttweaker\n")

    #Imports
    file.write("import crafttweaker.item.IItemStack;\n")
    file.write("import mods.contenttweaker.VanillaFactory;\n")
    file.write("import mods.contenttweaker.Block;\n")
    file.write("import mods.contenttweaker.Item;\n")

    print("Wrote header to content2.zs")

    #Create the items
    for item in items:
        item.write_item(file)

    print("Finished writing items to content2.zs")

    #Creates the blocks
    for block in blocks:
        block.write_block(file)

    print("Finished writing blocks to content2.zs")

file.close()

counter = 2

#Creates the lang file
with open("../resources/contenttweaker/lang/en_us.lang", "w+") as file:
    print("Started writing en_us.lang")

    #Writes the lines
    for gameObject in blocks + items:
        gameObject.write_name(file)

    print("Wrote all items to en_us.lang")

file.close()

#Creates the recipes file
with open("recipes1.zs", "w+") as file:
    print("Started writing recipes.zs")

    #Imports
    file.write("import crafttweaker.item.IItemStack;\n")

    #Removes Vanilla recipes
    file.write("recipes.removeAll();\n")
    file.write("furnace.removeAll();\n")

    #Removes ExtendedCrafting recipes
    file.write("mods.extendedcrafting.TableCrafting.remove(<extendedcrafting:material:24>);\n")
    file.write("mods.extendedcrafting.TableCrafting.remove(<extendedcrafting:singularity_ultimate>);\n")

    file.write("mods.extendedcrafting.EnderCrafting.remove(<extendedcrafting:material:40>);\n")
    file.write("mods.extendedcrafting.EnderCrafting.remove(<extendedcrafting:material:48>);\n")

    file.write("mods.extendedcrafting.CompressionCrafting.remove(<extendedcrafting:singularity:0>);\n")
    file.write("mods.extendedcrafting.CompressionCrafting.remove(<extendedcrafting:singularity:1>);\n")
    file.write("mods.extendedcrafting.CompressionCrafting.remove(<extendedcrafting:singularity:2>);\n")
    file.write("mods.extendedcrafting.CompressionCrafting.remove(<extendedcrafting:singularity:3>);\n")
    file.write("mods.extendedcrafting.CompressionCrafting.remove(<extendedcrafting:singularity:4>);\n")
    file.write("mods.extendedcrafting.CompressionCrafting.remove(<extendedcrafting:singularity:5>);\n")
    file.write("mods.extendedcrafting.CompressionCrafting.remove(<extendedcrafting:singularity:6>);\n")
    file.write("mods.extendedcrafting.CompressionCrafting.remove(<extendedcrafting:singularity:7>);\n")

    print("Finished removing old recipes")

file.close()

#Writes every new recipe for Vanilla objects
for recipe in block_recipes + item_recipes:
     recipe.write_recipe(open("recipes{}.zs".format(counter), "w+"))
     counter += 1

print("Finished writing Vanilla recipes")

#Writes every new recipe for non-Vanilla objects
for gameObject in blocks + items:
    gameObject.write_recipe(open("recipes{}.zs".format(counter), "w+"))
    counter += 1

print("Finished writing all recipes")
