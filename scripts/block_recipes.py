from Recipe import *

#Blocks with new crafting recipes
block_recipes = [
    Recipe(RecipeMethod.SHAPED2_2, "<minecraft:crafting_table>", [
        ["<minecraft:dirt:1>", "<minecraft:sand:1>"],
        ["<minecraft:clay_ball>", "<minecraft:flint>"]
    ]),

    Recipe(RecipeMethod.SHAPED3_3, "<extendedcrafting:table_ultimate>", [
        ["<minecraft:nether_star>", "<minecraft:spider_eye>", "<minecraft:record_chirp>"],
        ["<minecraft:ender_pearl>", "<minecraft:diamond>", "<minecraft:blaze_rod>"],
        ["<minecraft:prismarine_shard>", "<minecraft:quartz>", "<minecraft:totem_of_undying>"]
    ]),

    Recipe81("<minecraft:planks:0>", "<minecraft:log:0>"),
    Recipe81("<minecraft:planks:1>", "<minecraft:log:1>"),
    Recipe81("<minecraft:planks:2>", "<minecraft:log:2>"),
    Recipe81("<minecraft:planks:3>", "<minecraft:log:3>"),
    Recipe81("<minecraft:planks:4>", "<minecraft:log2:0>"),
    Recipe81("<minecraft:planks:5>", "<minecraft:log2:1>"),
    Recipe81("<minecraft:sandstone:0>", "<minecraft:sand>"),
    Recipe81("<minecraft:gold_block>", "<minecraft:gold_ingot>"),
    Recipe81("<minecraft:iron_block>", "<minecraft:iron_ingot>"),
    Recipe81("<minecraft:brick_block>", "<minecraft:brick>"),
    Recipe81("<minecraft:diamond_block>", "<minecraft:diamond>"),
    Recipe81("<minecraft:snow>", "<minecraft:snowball>"),
    Recipe81("<minecraft:clay>", "<minecraft:clay_ball>"),
    Recipe81("<minecraft:glowstone>", "<minecraft:glowstone_dust>"),
    Recipe81("<minecraft:nether_brick>", "<minecraft:netherbrick>"),
    Recipe81("<minecraft:coal_block>", "<minecraft:coal>"),
    Recipe81("<minecraft:slime>", "<minecraft:slime_ball>"),
    Recipe81("<minecraft:redstone_block>", "<minecraft:redstone>"),
    Recipe81("<extendedcrafting:storage:2>", "<minecraft:nether_star>"),
    Recipe81("<minecraft:brown_mushroom_block>", "<minecraft:brown_mushroom>"),
    Recipe81("<minecraft:red_mushroom_block>", "<minecraft:red_mushroom>"),
    Recipe81("<minecraft:hay_block>", "<minecraft:wheat>"),
    Recipe81("<minecraft:melon_block>", "<minecraft:melon>"),

    RecipeSurrounding("<minecraft:ice>", "<contenttweaker:freezer>", "<minecraft:snow>"),
    RecipeSurrounding("<minecraft:packed_ice>", "<contenttweaker:freezer>", "<minecraft:ice>"),
    RecipeSurrounding("<minecraft:bookshelf>", "<minecraft:planks:0>", "<minecraft:book>"),
    RecipeSurrounding("<minecraft:bookshelf>", "<minecraft:planks:1>", "<minecraft:book>"),
    RecipeSurrounding("<minecraft:bookshelf>", "<minecraft:planks:2>", "<minecraft:book>"),
    RecipeSurrounding("<minecraft:bookshelf>", "<minecraft:planks:3>", "<minecraft:book>"),
    RecipeSurrounding("<minecraft:bookshelf>", "<minecraft:planks:4>", "<minecraft:book>"),
    RecipeSurrounding("<minecraft:bookshelf>", "<minecraft:planks:5>", "<minecraft:book>"),

    Recipe2xSurrounding("<minecraft:glass>", "<contenttweaker:block_basin>", "<contenttweaker:molten_glass>", "<contenttweaker:blue_ice>"),
    Recipe2xSurrounding("<minecraft:furnace>", "<contenttweaker:compressed_cobblestone>", "<minecraft:coal_block>", "<contenttweaker:blaze_block>"),
    Recipe2xSurrounding("<minecraft:beacon>", "<contenttweaker:reinforced_obsidian>", "<contenttweaker:platinum_infused_glass>", "<extendedcrafting:storage:2>"),
    Recipe2xSurrounding("<minecraft:enchanting_table>", "<contenttweaker:reinforced_obsidian>", "<contenttweaker:air_altar>", "<minecraft:bookshelf>"),

    Recipe2xSurroundingCheckerboard("<minecraft:hardened_clay>", "<minecraft:furnace>", "<minecraft:clay>", "<contenttweaker:blaze_block>", "<minecraft:coal_block>"),

    RecipeFilledAnvil("<minecraft:anvil>", "<contenttweaker:steel_block>", "<contenttweaker:steel_toolmaker>")
]
