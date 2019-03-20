from Recipe import *

#Items with new crafting recipes
item_recipes = [
    Recipe81("<minecraft:iron_ingot>", "<minecraft:iron_nugget>"),
    Recipe81("<minecraft:gold_ingot>", "<minecraft:gold_nugget>"),
    Recipe81("<minecraft:paper>", "<contenttweaker:sugar_cane_block>"),

    RecipeSurrounding("<minecraft:glass_pane>", "<contenttweaker:glass_cutter>", "<minecraft:glass>"),
    RecipeSurrounding("<minecraft:shield>", "<contenttweaker:steel_block>", "<minecraft:stick>"),
    RecipeSurrounding("<minecraft:bread>", "<contenttweaker:grindstone>", "<minecraft:hay_block>"),
    RecipeSurrounding("<minecraft:sugar>", "<contenttweaker:grindstone>", "<contenttweaker:sugar_cane_block>"),
    RecipeSurrounding("<minecraft:beetroot_soup>", "<minecraft:bowl>", "<contenttweaker:beetroot_block>"),

    RecipeCheckerboard("<minecraft:flint_and_steel>", "<contenttweaker:steel_block>", "<contenttweaker:flint_block>"),
    RecipeCheckerboard("<minecraft:book>", "<contenttweaker:paper_block>", "<contenttweaker:reinforced_leather_block>"),

    Recipe2xSurrounding("<minecraft:golden_apple:0>", "<minecraft:enchanting_table>", "<minecraft:gold_block>", "<contenttweaker:apple_block>"),
    Recipe2xSurrounding("<minecraft:golden_apple:1>", "<minecraft:enchanting_table>", "<extendedcrafting:storage:2>", "<minecraft:golden_apple:0>"),

    Recipe2xSurroundingCheckerboard("<minecraft:coal:1>", "<minecraft:furnace>", "<minecraft:log:0>", "<contenttweaker:blaze_block>", "<minecraft:coal_block>"),
    Recipe2xSurroundingCheckerboard("<minecraft:coal:1>", "<minecraft:furnace>", "<minecraft:log:1>", "<contenttweaker:blaze_block>", "<minecraft:coal_block>"),
    Recipe2xSurroundingCheckerboard("<minecraft:coal:1>", "<minecraft:furnace>", "<minecraft:log:2>", "<contenttweaker:blaze_block>", "<minecraft:coal_block>"),
    Recipe2xSurroundingCheckerboard("<minecraft:coal:1>", "<minecraft:furnace>", "<minecraft:log:3>", "<contenttweaker:blaze_block>", "<minecraft:coal_block>"),
    Recipe2xSurroundingCheckerboard("<minecraft:coal:1>", "<minecraft:furnace>", "<minecraft:log2:0>", "<contenttweaker:blaze_block>", "<minecraft:coal_block>"),
    Recipe2xSurroundingCheckerboard("<minecraft:coal:1>", "<minecraft:furnace>", "<minecraft:log2:1>", "<contenttweaker:blaze_block>", "<minecraft:coal_block>"),
    Recipe2xSurroundingCheckerboard("<minecraft:brick>", "<minecraft:furnace>", "<contenttweaker:placeholder_clay_block>", "<contenttweaker:blaze_block>", "<minecraft:coal_block>"),
    Recipe2xSurroundingCheckerboard("<minecraft:gold_nugget>", "<contenttweaker:steel_metal_former>", "<contenttweaker:molten_gold>", "<contenttweaker:nugget_cast>", "<contenttweaker:purple_ice>"),
    Recipe2xSurroundingCheckerboard("<minecraft:netherbrick>", "<minecraft:furnace>", "<contenttweaker:compressed_netherrack>", "<contenttweaker:blaze_block>", "<minecraft:coal_block>"),
    Recipe2xSurroundingCheckerboard("<minecraft:iron_nugget>", "<contenttweaker:metal_former>", "<contenttweaker:molten_iron>", "<contenttweaker:nugget_cast>", "<contenttweaker:blue_ice>"),
    Recipe2xSurroundingCheckerboard("<minecraft:cooked_porkchop>", "<contenttweaker:steel_oven>", "<minecraft:porkchop>", "<contenttweaker:blaze_block>", "<minecraft:coal_block>"),
    Recipe2xSurroundingCheckerboard("<minecraft:cooked_fish:0>", "<contenttweaker:steel_oven>", "<minecraft:fish:0>", "<contenttweaker:blaze_block>", "<minecraft:coal_block>"),
    Recipe2xSurroundingCheckerboard("<minecraft:cooked_fish:1>", "<contenttweaker:steel_oven>", "<minecraft:fish:1>", "<contenttweaker:blaze_block>", "<minecraft:coal_block>"),
    Recipe2xSurroundingCheckerboard("<minecraft:cooked_beef>", "<contenttweaker:steel_oven>", "<minecraft:beef>", "<contenttweaker:blaze_block>", "<minecraft:coal_block>"),
    Recipe2xSurroundingCheckerboard("<minecraft:cooked_chicken>", "<contenttweaker:steel_oven>", "<minecraft:chicken>", "<contenttweaker:blaze_block>", "<minecraft:coal_block>"),
    Recipe2xSurroundingCheckerboard("<minecraft:baked_potato>", "<contenttweaker:steel_oven>", "<contenttweaker:potato_block>", "<contenttweaker:blaze_block>", "<minecraft:coal_block>"),
    Recipe2xSurroundingCheckerboard("<minecraft:cooked_rabbit>", "<contenttweaker:steel_oven>", "<minecraft:rabbit>", "<contenttweaker:blaze_block>", "<minecraft:coal_block>"),
    Recipe2xSurroundingCheckerboard("<minecraft:cooked_mutton>", "<contenttweaker:steel_oven>", "<minecraft:mutton>", "<contenttweaker:blaze_block>", "<minecraft:coal_block>"),
    Recipe2xSurroundingCheckerboard("<minecraft:cookie>", "<contenttweaker:steel_oven>", "<minecraft:hay_block>", "<contenttweaker:sugar_block>", "<contenttweaker:cocoa_block>"),
    Recipe2xSurroundingCheckerboard("<minecraft:pumpkin_pie>", "<contenttweaker:steel_oven>", "<minecraft:pumpkin>", "<contenttweaker:sugar_block>", "<contenttweaker:egg_block>"),

    RecipeRod("<minecraft:stick>", "<minecraft:planks:0>"),
    RecipeRod("<minecraft:stick>", "<minecraft:planks:1>"),
    RecipeRod("<minecraft:stick>", "<minecraft:planks:2>"),
    RecipeRod("<minecraft:stick>", "<minecraft:planks:3>"),
    RecipeRod("<minecraft:stick>", "<minecraft:planks:4>"),
    RecipeRod("<minecraft:stick>", "<minecraft:planks:5>"),

    RecipePickaxeT1("<minecraft:wooden_pickaxe>", "<minecraft:planks:0>", "<minecraft:stick>"),
    RecipePickaxeT1("<minecraft:wooden_pickaxe>", "<minecraft:planks:1>", "<minecraft:stick>"),
    RecipePickaxeT1("<minecraft:wooden_pickaxe>", "<minecraft:planks:2>", "<minecraft:stick>"),
    RecipePickaxeT1("<minecraft:wooden_pickaxe>", "<minecraft:planks:3>", "<minecraft:stick>"),
    RecipePickaxeT1("<minecraft:wooden_pickaxe>", "<minecraft:planks:4>", "<minecraft:stick>"),
    RecipePickaxeT1("<minecraft:wooden_pickaxe>", "<minecraft:planks:5>", "<minecraft:stick>"),

    RecipeAxeT1("<minecraft:wooden_axe>", "<minecraft:planks:0>", "<minecraft:stick>"),
    RecipeAxeT1("<minecraft:wooden_axe>", "<minecraft:planks:1>", "<minecraft:stick>"),
    RecipeAxeT1("<minecraft:wooden_axe>", "<minecraft:planks:2>", "<minecraft:stick>"),
    RecipeAxeT1("<minecraft:wooden_axe>", "<minecraft:planks:3>", "<minecraft:stick>"),
    RecipeAxeT1("<minecraft:wooden_axe>", "<minecraft:planks:4>", "<minecraft:stick>"),
    RecipeAxeT1("<minecraft:wooden_axe>", "<minecraft:planks:5>", "<minecraft:stick>"),

    RecipeShovelT1("<minecraft:wooden_shovel>", "<minecraft:planks:0>", "<minecraft:stick>"),
    RecipeShovelT1("<minecraft:wooden_shovel>", "<minecraft:planks:1>", "<minecraft:stick>"),
    RecipeShovelT1("<minecraft:wooden_shovel>", "<minecraft:planks:2>", "<minecraft:stick>"),
    RecipeShovelT1("<minecraft:wooden_shovel>", "<minecraft:planks:3>", "<minecraft:stick>"),
    RecipeShovelT1("<minecraft:wooden_shovel>", "<minecraft:planks:4>", "<minecraft:stick>"),
    RecipeShovelT1("<minecraft:wooden_shovel>", "<minecraft:planks:5>", "<minecraft:stick>"),

    RecipeHoeT1("<minecraft:wooden_hoe>", "<minecraft:planks:0>", "<minecraft:stick>"),
    RecipeHoeT1("<minecraft:wooden_hoe>", "<minecraft:planks:1>", "<minecraft:stick>"),
    RecipeHoeT1("<minecraft:wooden_hoe>", "<minecraft:planks:2>", "<minecraft:stick>"),
    RecipeHoeT1("<minecraft:wooden_hoe>", "<minecraft:planks:3>", "<minecraft:stick>"),
    RecipeHoeT1("<minecraft:wooden_hoe>", "<minecraft:planks:4>", "<minecraft:stick>"),
    RecipeHoeT1("<minecraft:wooden_hoe>", "<minecraft:planks:5>", "<minecraft:stick>"),

    RecipeSwordT1("<minecraft:wooden_sword>", "<minecraft:planks:0>", "<minecraft:stick>"),
    RecipeSwordT1("<minecraft:wooden_sword>", "<minecraft:planks:1>", "<minecraft:stick>"),
    RecipeSwordT1("<minecraft:wooden_sword>", "<minecraft:planks:2>", "<minecraft:stick>"),
    RecipeSwordT1("<minecraft:wooden_sword>", "<minecraft:planks:3>", "<minecraft:stick>"),
    RecipeSwordT1("<minecraft:wooden_sword>", "<minecraft:planks:4>", "<minecraft:stick>"),
    RecipeSwordT1("<minecraft:wooden_sword>", "<minecraft:planks:5>", "<minecraft:stick>"),

    RecipePickaxeT2("<minecraft:golden_pickaxe>", "<contenttweaker:angmallen_block>", "<minecraft:iron_pickaxe>", "<contenttweaker:angmallen_toolmaker>"),
    RecipePickaxeT2("<minecraft:iron_pickaxe>", "<contenttweaker:steel_block>", "<minecraft:stone_pickaxe>", "<contenttweaker:steel_toolmaker>"),
    RecipePickaxeT2("<minecraft:stone_pickaxe>", "<contenttweaker:compressed_cobblestone>", "<minecraft:wooden_pickaxe>", "<contenttweaker:stone_toolmaker>"),

    RecipeAxeT2("<minecraft:golden_axe>", "<contenttweaker:angmallen_block>", "<minecraft:iron_axe>", "<contenttweaker:angmallen_toolmaker>"),
    RecipeAxeT2("<minecraft:iron_axe>", "<contenttweaker:steel_block>", "<minecraft:stone_axe>", "<contenttweaker:steel_toolmaker>"),
    RecipeAxeT2("<minecraft:stone_axe>", "<contenttweaker:compressed_cobblestone>", "<minecraft:wooden_axe>", "<contenttweaker:stone_toolmaker>"),

    RecipeShovelT2("<minecraft:golden_shovel>", "<contenttweaker:angmallen_block>", "<minecraft:iron_shovel>", "<contenttweaker:angmallen_toolmaker>"),
    RecipeShovelT2("<minecraft:iron_shovel>", "<contenttweaker:steel_block>", "<minecraft:stone_shovel>", "<contenttweaker:steel_toolmaker>"),
    RecipeShovelT2("<minecraft:stone_shovel>", "<contenttweaker:compressed_cobblestone>", "<minecraft:wooden_shovel>", "<contenttweaker:stone_toolmaker>"),

    RecipeHoeT2("<minecraft:golden_hoe>", "<contenttweaker:angmallen_block>", "<minecraft:iron_hoe>", "<contenttweaker:angmallen_toolmaker>"),
    RecipeHoeT2("<minecraft:iron_hoe>", "<contenttweaker:steel_block>", "<minecraft:stone_hoe>", "<contenttweaker:steel_toolmaker>"),
    RecipeHoeT2("<minecraft:stone_hoe>", "<contenttweaker:compressed_cobblestone>", "<minecraft:wooden_hoe>", "<contenttweaker:stone_toolmaker>"),

    RecipeSwordT2("<minecraft:golden_sword>", "<contenttweaker:angmallen_block>", "<minecraft:iron_sword>", "<contenttweaker:angmallen_toolmaker>"),
    RecipeSwordT2("<minecraft:iron_sword>", "<contenttweaker:steel_block>", "<minecraft:stone_sword>", "<contenttweaker:steel_toolmaker>"),
    RecipeSwordT2("<minecraft:stone_sword>", "<contenttweaker:compressed_cobblestone>", "<minecraft:wooden_sword>", "<contenttweaker:stone_toolmaker>"),

    RecipeBow("<minecraft:bow>", "<contenttweaker:steel_block>", "<contenttweaker:reinforced_wool>", "<minecraft:stick>", "<contenttweaker:steel_toolmaker>"),

    RecipeArrow("<minecraft:arrow>", "<contenttweaker:flint_block>", "<contenttweaker:reinforced_featherwool>", "<minecraft:stick>", "<contenttweaker:steel_toolmaker>"),

    RecipeHelmet("<minecraft:golden_helmet>", "<contenttweaker:angmallen_block>", "<contenttweaker:angmallen_armormaker>"),
    RecipeHelmet("<minecraft:leather_helmet>", "<contenttweaker:reinforced_leather_block>", "<contenttweaker:leather_armormaker>"),
    RecipeHelmet("<minecraft:chainmail_helmet>", "<contenttweaker:chains>", "<contenttweaker:chainmail_armormaker>"),
    RecipeHelmet("<minecraft:iron_helmet>", "<contenttweaker:steel_block>", "<contenttweaker:steel_armormaker>"),

    RecipeChestplate("<minecraft:golden_chestplate>", "<contenttweaker:angmallen_block>", "<contenttweaker:angmallen_armormaker>"),
    RecipeChestplate("<minecraft:leather_chestplate>", "<contenttweaker:reinforced_leather_block>", "<contenttweaker:leather_armormaker>"),
    RecipeChestplate("<minecraft:chainmail_chestplate>", "<contenttweaker:chains>", "<contenttweaker:chainmail_armormaker>"),
    RecipeChestplate("<minecraft:iron_chestplate>", "<contenttweaker:steel_block>", "<contenttweaker:steel_armormaker>"),

    RecipeLeggings("<minecraft:golden_leggings>", "<contenttweaker:angmallen_block>", "<contenttweaker:angmallen_armormaker>"),
    RecipeLeggings("<minecraft:leather_leggings>", "<contenttweaker:reinforced_leather_block>", "<contenttweaker:leather_armormaker>"),
    RecipeLeggings("<minecraft:chainmail_leggings>", "<contenttweaker:chains>", "<contenttweaker:chainmail_armormaker>"),
    RecipeLeggings("<minecraft:iron_leggings>", "<contenttweaker:steel_block>", "<contenttweaker:steel_armormaker>"),

    RecipeBoots("<minecraft:golden_boots>", "<contenttweaker:angmallen_block>", "<contenttweaker:angmallen_armormaker>"),
    RecipeBoots("<minecraft:leather_boots>", "<contenttweaker:reinforced_leather_block>", "<contenttweaker:leather_armormaker>"),
    RecipeBoots("<minecraft:chainmail_boots>", "<contenttweaker:chains>", "<contenttweaker:chainmail_armormaker>"),
    RecipeBoots("<minecraft:iron_boots>", "<contenttweaker:steel_block>", "<contenttweaker:steel_armormaker>"),

    RecipeGrate("<minecraft:iron_bars>", "<minecraft:glass_pane>", "<contenttweaker:iron_bar>"),

    RecipeBucket("<minecraft:bucket>", "<contenttweaker:steel_block>", "<contenttweaker:steel_toolmaker>"),
    RecipeBucket("<minecraft:glass_bottle>", "<minecraft:glass>", "<minecraft:bucket>"),
    RecipeBucket("<minecraft:bowl>", "<minecraft:planks:0>", "<minecraft:stick>"),
    RecipeBucket("<minecraft:bowl>", "<minecraft:planks:1>", "<minecraft:stick>"),
    RecipeBucket("<minecraft:bowl>", "<minecraft:planks:2>", "<minecraft:stick>"),
    RecipeBucket("<minecraft:bowl>", "<minecraft:planks:3>", "<minecraft:stick>"),
    RecipeBucket("<minecraft:bowl>", "<minecraft:planks:4>", "<minecraft:stick>"),
    RecipeBucket("<minecraft:bowl>", "<minecraft:planks:5>", "<minecraft:stick>"),

    RecipeFishingRod("<minecraft:fishing_rod>", "<contenttweaker:reinforced_wool>", "<minecraft:stick>", "<contenttweaker:steel_toolmaker>"),

    RecipeShears("<minecraft:shears>", "<contenttweaker:steel_block>", "<contenttweaker:steel_toolmaker>"),

    RecipeLead("<minecraft:lead>", "<contenttweaker:reinforced_wool>", "<contenttweaker:steel_block>", "<minecraft:slime>", "<contenttweaker:steel_toolmaker>"),

    RecipeNameTag("<minecraft:name_tag>", "<minecraft:anvil>", "<minecraft:slime>", "<contenttweaker:reinforced_wool>", "<contenttweaker:steel_block>", "<contenttweaker:steel_toolmaker>")
]
