from Recipe import *
from Object import Item

#List of every item in the game
items = [
    Item("molten_iron", recipe=Recipe2xSurroundingCheckerboard("<contenttweaker:molten_iron>", "<contenttweaker:forge>", "<minecraft:iron_ore>", "<contenttweaker:blaze_block>", "<minecraft:coal_block>")),
    Item("raw_nugget_cast", recipe=RecipeNuggetCast("<contenttweaker:raw_nugget_cast>", "<contenttweaker:castmaker>", "<contenttweaker:placeholder_clay_block>", "<minecraft:clay>")),
    Item("placeholder_clay", recipe=RecipeCheckerboard("<contenttweaker:placeholder_clay>", "<minecraft:hardened_clay>", "<minecraft:clay>")),
    Item("nugget_cast", recipe=Recipe2xSurroundingCheckerboard("<contenttweaker:nugget_cast>", "<minecraft:furnace>", "<contenttweaker:raw_nugget_cast>", "<contenttweaker:blaze_block>", "<minecraft:coal_block>")),
    Item("steel_nugget", recipe=Recipe2xSurroundingCheckerboard("<contenttweaker:steel_nugget>", "<contenttweaker:metal_former>", "<contenttweaker:molten_steel>", "<contenttweaker:nugget_cast>", "<contenttweaker:blue_ice>")),
    Item("steel_ingot", recipe=Recipe81("<contenttweaker:steel_ingot>", "<contenttweaker:steel_nugget>")),
    Item("blast_furnace_brick", recipe=RecipeCheckerboard("<contenttweaker:blast_furnace_brick>", "<minecraft:nether_brick>", "<contenttweaker:compressed_soulsand>")),
    Item("molten_steel", recipe=RecipeMoltenSteel("<contenttweaker:molten_steel>", "<contenttweaker:blast_furnace>", "<minecraft:iron_block>", "<contenttweaker:coal_coke_block>", "<contenttweaker:gunpowder_block>", "<contenttweaker:blaze_block>", "<minecraft:glowstone>")),
    Item("coke_oven_brick", recipe=RecipeCheckerboard("<contenttweaker:coke_oven_brick>", "<minecraft:brick_block>", "<contenttweaker:compressed_sandstone>")),
    Item("coal_coke", recipe=RecipeSurrounding("<contenttweaker:coal_coke>", "<contenttweaker:coke_oven>", "<contenttweaker:charcoal_block>")),
    Item("reinforced_leather", recipe=Recipe81("<contenttweaker:reinforced_leather>", "<contenttweaker:leather_block>")),
    Item("molten_glass", recipe=Recipe2xSurroundingCheckerboard("<contenttweaker:molten_glass>", "<contenttweaker:glass_production_oven>", "<contenttweaker:compressed_sandstone>", "<contenttweaker:blaze_block>", "<contenttweaker:coal_coke_block>")),
    Item("glass_shard", recipe=RecipeSurrounding("<contenttweaker:glass_shard>", "<contenttweaker:breaking_chamber>", "<minecraft:glass>")),
    Item("glass_crystal", recipe=RecipeSurrounding("<contenttweaker:glass_crystal>", "<contenttweaker:breaking_chamber>", "<contenttweaker:glass_shard>")),
    Item("glass_blade", recipe=RecipeSurrounding("<contenttweaker:glass_blade>", "<contenttweaker:breaking_chamber>", "<contenttweaker:glass_crystal>")),
    Item("glass_cutter", recipe=RecipeCutter("<contenttweaker:glass_cutter>", "<minecraft:stick>", "<contenttweaker:glass_blade>")),
    Item("steel_shard", recipe=RecipeSurrounding("<contenttweaker:steel_shard>", "<contenttweaker:breaking_chamber>", "<contenttweaker:steel_block>")),
    Item("steel_crystal", recipe=RecipeSurrounding("<contenttweaker:steel_crystal>", "<contenttweaker:breaking_chamber>", "<contenttweaker:steel_shard>")),
    Item("steel_blade", recipe=RecipeSurrounding("<contenttweaker:steel_blade>", "<contenttweaker:breaking_chamber>", "<contenttweaker:steel_crystal>")),
    Item("steel_cutter", recipe=RecipeCutter("<contenttweaker:steel_cutter>", "<minecraft:iron_sword>", "<contenttweaker:steel_blade>")),
    Item("iron_bar", recipe=RecipeSurrounding("<contenttweaker:iron_bar>", "<contenttweaker:steel_cutter>", "<contenttweaker:steel_block>")),
    Item("chain", recipe=Recipe81("<contenttweaker:chain>", "<minecraft:iron_bars>")),
    Item("reinforced_string", recipe=RecipeCheckerboard("<contenttweaker:reinforced_string>", "<minecraft:string>", "<contenttweaker:steel_block>")),
    Item("reinforced_feather", recipe=RecipeCheckerboard("<contenttweaker:reinforced_feather>", "<minecraft:feather>", "<contenttweaker:steel_block>")),
    Item("steel_forge_brick", recipe=RecipeCheckerboard("<contenttweaker:steel_forge_brick>", "<contenttweaker:steel_block>", "<contenttweaker:blast_furnace>")),
    Item("molten_gold", recipe=Recipe2xSurroundingCheckerboard("<contenttweaker:molten_gold>", "<contenttweaker:pyrothite_forge>", "<minecraft:gold_ore>", "<contenttweaker:pyrothite_block>", "<contenttweaker:refined_coke_block>")),
    Item("sulfur", recipe=Recipe81("<contenttweaker:sulfur>", "<contenttweaker:tiny_sulfur_pile>")),
    Item("sulfur_gas", recipe=Recipe2xSurrounding("<contenttweaker:sulfur_gas>", "<contenttweaker:dust_refiner>", "<contenttweaker:blaze_block>", "<contenttweaker:gunpowder_block>")),
    Item("steel_turbine", recipe=Recipe81("<contenttweaker:steel_turbine>", "<contenttweaker:steel_blade>")),
    Item("water_vapor", recipe=Recipe2xSurrounding("<contenttweaker:water_vapor>", "<contenttweaker:evaporator>", "<minecraft:water_bucket>", "<contenttweaker:blaze_block>")),
    Item("oxygen"),
    Item("hydrogen"),
    Item("flask", recipe=Recipe81("<contenttweaker:flask>", "<minecraft:glass_bottle>")),
    Item("beaker", recipe=Recipe81("<contenttweaker:beaker>", "<contenttweaker:flask>")),
    Item("sulfuric_acid"),
    Item("tiny_sulfur_pile", recipe=Recipe81("<contenttweaker:tiny_sulfur_pile>", "<contenttweaker:very_tiny_sulfur_pile>")),
    Item("very_tiny_sulfur_pile", recipe=Recipe2xSurrounding("<contenttweaker:very_tiny_sulfur_pile>", "<contenttweaker:depositor>", "<contenttweaker:sulfuric_acid>", "<contenttweaker:purple_ice>")),
    Item("pyrotheum_dust", recipe=Recipe81("<contenttweaker:pyrotheum_dust>", "<contenttweaker:tiny_pyrotheum_dust_pile>")),
    Item("tiny_pyrotheum_dust_pile", recipe=Recipe81("<contenttweaker:tiny_pyrotheum_dust_pile>", "<contenttweaker:very_tiny_pyrotheum_dust_pile>")),
    Item("very_tiny_pyrotheum_dust_pile", recipe=Recipe2xSurrounding("<contenttweaker:very_tiny_pyrotheum_dust_pile>", "<contenttweaker:depositor>", "<contenttweaker:pyrotheum_gas>", "<contenttweaker:purple_ice>")),
    Item("pyrotheum_gas", recipe=RecipeChemistryStationCrafting("<contenttweaker:pyrotheum_gas>", "<contenttweaker:dust_mixer>", "<contenttweaker:chemistry_station>", "<contenttweaker:blaze_block>", "<contenttweaker:blaze_block>", "<minecraft:redstone_block>", "<contenttweaker:sulfur_block>")),
    Item("molten_pyrothite", recipe=RecipeSurrounding("<contenttweaker:molten_pyrothite>", "<contenttweaker:steel_forge>", "<contenttweaker:pyrotheum_dust_block>")),
    Item("pyrothite_nugget", recipe=Recipe2xSurroundingCheckerboard("<contenttweaker:pyrothite_nugget>", "<contenttweaker:steel_metal_former>", "<contenttweaker:molten_pyrothite>", "<contenttweaker:nugget_cast>", "<contenttweaker:purple_ice>")),
    Item("pyrothite_ingot", recipe=Recipe81("<contenttweaker:pyrothite_ingot>", "<contenttweaker:pyrothite_nugget>")),
    Item("pyrothite_forge_brick", recipe=RecipeCheckerboard("<contenttweaker:pyrothite_forge_brick>", "<contenttweaker:pyrothite_block>", "<contenttweaker:steel_forge>")),
    Item("environmental_destroyer"),
    Item("oil", recipe=RecipeSurrounding("<contenttweaker:oil>", "<contenttweaker:environmental_destroyer>", "<minecraft:water_bucket>")),
    Item("heavy_oil", recipe=Recipe2xSurrounding("<contenttweaker:heavy_oil>", "<contenttweaker:refinery>", "<contenttweaker:oil>", "<contenttweaker:pyrothite_block>")),
    Item("medium_oil", recipe=Recipe2xSurrounding("<contenttweaker:medium_oil>", "<contenttweaker:refinery>", "<contenttweaker:heavy_oil>", "<contenttweaker:pyrothite_block>")),
    Item("diesel_oil", recipe=Recipe2xSurrounding("<contenttweaker:diesel_oil>", "<contenttweaker:refinery>", "<contenttweaker:medium_oil>", "<contenttweaker:pyrothite_block>")),
    Item("kerosene", recipe=Recipe2xSurrounding("<contenttweaker:kerosene>", "<contenttweaker:refinery>", "<contenttweaker:diesel_oil>", "<contenttweaker:pyrothite_block>")),
    Item("naphtha", recipe=Recipe2xSurrounding("<contenttweaker:naphtha>", "<contenttweaker:refinery>", "<contenttweaker:kerosene>", "<contenttweaker:pyrothite_block>")),
    Item("gasoline_oil", recipe=Recipe2xSurrounding("<contenttweaker:gasoline_oil>", "<contenttweaker:refinery>", "<contenttweaker:naphtha>", "<contenttweaker:pyrothite_block>")),
    Item("refined_fuel", recipe=Recipe2xSurrounding("<contenttweaker:refined_fuel>", "<contenttweaker:refinery>", "<contenttweaker:gasoline_oil>", "<contenttweaker:pyrothite_block>")),
    Item("refined_coke", recipe=RecipeCheckerboard("<contenttweaker:refined_coke>", "<contenttweaker:refined_fuel>", "<contenttweaker:coal_coke_block>")),
    Item("blizz_rod", recipe=Recipe2xSurrounding("<contenttweaker:blizz_rod>", "<contenttweaker:steel_freezer>", "<contenttweaker:blaze_block>", "<contenttweaker:purple_ice>")),
    Item("cryotheum_gas", recipe=RecipeChemistryStationCrafting("<contenttweaker:cryotheum_gas>", "<contenttweaker:pyrothite_dust_mixer>", "<contenttweaker:pyrothite_chemistry_station>", "<contenttweaker:blizz_block>", "<contenttweaker:blizz_block>", "<minecraft:redstone_block>", "<contenttweaker:purple_ice>")),
    Item("molten_platinum", recipe=Recipe2xSurroundingCheckerboard("<contenttweaker:molten_platinum>", "<contenttweaker:pyrothite_forge>", "<minecraft:diamond_block>", "<contenttweaker:pyrothite_block>", "<contenttweaker:refined_coke_block>")),
    Item("platinum_nugget", recipe=Recipe2xSurroundingCheckerboard("<contenttweaker:platinum_nugget>", "<contenttweaker:steel_metal_former>", "<contenttweaker:molten_platinum>", "<contenttweaker:nugget_cast>", "<contenttweaker:purple_ice>")),
    Item("platinum_ingot", recipe=Recipe81("<contenttweaker:platinum_ingot>", "<contenttweaker:platinum_nugget>")),
    Item("molten_platinum_infused_glass", recipe=Recipe2xSurroundingCheckerboard("<contenttweaker:molten_platinum_infused_glass>", "<contenttweaker:pyrothite_glass_production_oven>", "<minecraft:glass>", "<contenttweaker:pyrothite_block>", "<contenttweaker:refined_coke_block>")),
    Item("cryotheum_dust", recipe=Recipe81("<contenttweaker:cryotheum_dust>", "<contenttweaker:tiny_cryotheum_dust_pile>")),
    Item("tiny_cryotheum_dust_pile", recipe=Recipe81("<contenttweaker:tiny_cryotheum_dust_pile>", "<contenttweaker:very_tiny_cryotheum_dust_pile>")),
    Item("very_tiny_cryotheum_dust_pile", recipe=Recipe2xSurrounding("<contenttweaker:very_tiny_cryotheum_dust_pile>", "<contenttweaker:depositor>", "<contenttweaker:cryotheum_gas>", "<contenttweaker:purple_ice>")),
    Item("molten_cryothite", recipe=Recipe2xSurrounding("<contenttweaker:molten_cryothite>", "<contenttweaker:pyrothite_forge>", "<contenttweaker:cryotheum_dust_block>", "<contenttweaker:refined_coke_block>")),
    Item("cryothite_nugget", recipe=Recipe2xSurroundingCheckerboard("<contenttweaker:cryothite_nugget>", "<contenttweaker:steel_metal_former>", "<contenttweaker:molten_cryothite>", "<contenttweaker:nugget_cast>", "<contenttweaker:purple_ice>")),
    Item("cryothite_ingot", recipe=Recipe81("<contenttweaker:cryothite_ingot>", "<contenttweaker:cryothite_nugget>")),
    Item("blitz_rod", recipe=Recipe2xSurrounding("<contenttweaker:blitz_rod>", "<contenttweaker:air_altar>", "<contenttweaker:blizz_block>", "<extendedcrafting:storage:2>")),
    Item("molten_infernium", recipe=RecipeAlloying("<contenttweaker:molten_infernium>", "<contenttweaker:pyrothite_forge>", "<contenttweaker:platinum_block>", "<contenttweaker:refined_coke_block>", "<extendedcrafting:storage:2>")),
    Item("infernium_nugget", recipe=Recipe2xSurroundingCheckerboard("<contenttweaker:infernium_nugget>", "<contenttweaker:cryothite_metal_former>", "<contenttweaker:molten_infernium>", "<contenttweaker:nugget_cast>", "<contenttweaker:pink_ice>")),
    Item("infernium_ingot", recipe=Recipe81("<contenttweaker:infernium_ingot>", "<contenttweaker:infernium_nugget>")),
    Item("infernium_forge_brick", recipe=RecipeCheckerboard("<contenttweaker:infernium_forge_brick>", "<contenttweaker:infernium_block>", "<contenttweaker:pyrothite_forge>")),
    Item("molten_mithril", recipe=RecipeAlloying("<contenttweaker:molten_mithril>", "<contenttweaker:infernium_forge>", "<contenttweaker:cryothite_block>", "<contenttweaker:infernal_coke_block>", "<contenttweaker:infernium_block>")),
    Item("mithril_nugget", recipe=Recipe2xSurroundingCheckerboard("<contenttweaker:mithril_nugget>", "<contenttweaker:cryothite_metal_former>", "<contenttweaker:molten_mithril>", "<contenttweaker:nugget_cast>", "<contenttweaker:pink_ice>")),
    Item("mithril_ingot", recipe=Recipe81("<contenttweaker:mithril_ingot>", "<contenttweaker:mithril_nugget>")),
    Item("infernal_coke", recipe=Recipe2xSurroundingCheckerboard("<contenttweaker:infernal_coke>", "<contenttweaker:infernium_refinery>", "<contenttweaker:environmental_destroyer_v2>", "<contenttweaker:refined_coke_block>", "<extendedcrafting:storage:2>")),
    Item("environmental_destroyer_v2", "Environmental Destroyer v2"),
    Item("molten_adamantium", recipe=RecipeAlloying("<contenttweaker:molten_adamantium>", "<contenttweaker:mithril_forge>", "<contenttweaker:pyrothite_block>", "<contenttweaker:infernal_coke_block>", "<contenttweaker:mithril_block>")),
    Item("adamantium_nugget", recipe=Recipe2xSurroundingCheckerboard("<contenttweaker:adamantium_nugget>", "<contenttweaker:cryothite_metal_former>", "<contenttweaker:molten_adamantium>", "<contenttweaker:nugget_cast>", "<contenttweaker:pink_ice>")),
    Item("adamantium_ingot", recipe=Recipe81("<contenttweaker:adamantium_ingot>", "<contenttweaker:adamantium_nugget>")),
    Item("mithril_forge_brick", recipe=RecipeCheckerboard("<contenttweaker:mithril_forge_brick>", "<contenttweaker:mithril_block>", "<contenttweaker:infernium_forge>")),
    Item("adamantium_forge_brick", recipe=RecipeCheckerboard("<contenttweaker:adamantium_forge_brick>", "<contenttweaker:adamantium_block>", "<contenttweaker:mithril_forge>")),
    Item("molten_reinforced_steel", recipe=RecipeAlloying("<contenttweaker:molten_reinforced_steel>", "<contenttweaker:adamantium_forge>", "<contenttweaker:reinforced_obsidian>", "<contenttweaker:infernal_coke_block>", "<contenttweaker:adamantium_block>")),
    Item("reinforced_steel_nugget", recipe=Recipe2xSurroundingCheckerboard("<contenttweaker:reinforced_steel_nugget>", "<contenttweaker:cryothite_metal_former>", "<contenttweaker:molten_reinforced_steel>", "<contenttweaker:nugget_cast>", "<contenttweaker:pink_ice>")),
    Item("reinforced_steel_ingot", recipe=Recipe81("<contenttweaker:reinforced_steel_ingot>", "<contenttweaker:reinforced_steel_nugget>")),
    Item("reinforced_steel_forge_brick", recipe=RecipeCheckerboard("<contenttweaker:reinforced_steel_forge_brick>", "<contenttweaker:reinforced_steel_block>", "<contenttweaker:adamantium_forge>")),
    Item("molten_reinforced_glass", recipe=Recipe2xSurroundingCheckerboard("<contenttweaker:molten_reinforced_glass>", "<contenttweaker:reinforced_steel_glass_production_oven>", "<contenttweaker:platinum_infused_glass>", "<contenttweaker:reinforced_steel_block>", "<contenttweaker:infernal_coke_block>")),
    Item("wood_gear", recipe=RecipeSurrounding("<contenttweaker:wood_gear>", "<contenttweaker:compressed_cobblestone>", "<minecraft:stick>")),
    Item("stone_gear", recipe=RecipeSurrounding("<contenttweaker:stone_gear>", "<contenttweaker:compressed_cobblestone>", "<contenttweaker:wood_gear>")),
    Item("weird_food"),
    Item("banana", recipe=Recipe2xSurrounding("<contenttweaker:banana>", "<contenttweaker:greenhouse>", "<contenttweaker:life_altar>", "<contenttweaker:apple_block>")),
    Item("potassium", recipe=Recipe2xSurrounding("<contenttweaker:potassium>", "<contenttweaker:reinforced_steel_dust_refiner>", "<contenttweaker:infernal_coke_block>", "<contenttweaker:banana_block>")),
    Item("nitrogen", recipe=Recipe2xSurrounding("<contenttweaker:nitrogen>", "<contenttweaker:reinforced_steel_dust_refiner>", "<contenttweaker:infernal_coke_block>", "<contenttweaker:egg_block>")),
    Item("nitrate"),
    Item("potassium_nitrate"),
    Item("very_tiny_niter_pile", recipe=Recipe2xSurrounding("<contenttweaker:very_tiny_niter_pile>", "<contenttweaker:reinforced_steel_depositor>", "<contenttweaker:potassium_nitrate>", "<contenttweaker:pink_ice>")),
    Item("tiny_niter_pile", recipe=Recipe81("<contenttweaker:tiny_niter_pile>", "<contenttweaker:very_tiny_niter_pile>")),
    Item("niter", recipe=Recipe81("<contenttweaker:niter>", "<contenttweaker:tiny_niter_pile>")),
    Item("aerotheum_gas", recipe=RecipeChemistryStationCrafting("<contenttweaker:aerotheum_gas>", "<contenttweaker:reinforced_steel_dust_mixer>", "<contenttweaker:reinforced_steel_chemistry_station>", "<contenttweaker:blitz_block>", "<contenttweaker:blitz_block>", "<minecraft:redstone_block>", "<contenttweaker:niter_block>")),
    Item("very_tiny_aerotheum_dust_pile", recipe=Recipe2xSurrounding("<contenttweaker:very_tiny_aerotheum_dust_pile>", "<contenttweaker:reinforced_steel_depositor>", "<contenttweaker:aerotheum_gas>", "<contenttweaker:pink_ice>")),
    Item("tiny_aerotheum_dust_pile", recipe=Recipe81("<contenttweaker:tiny_aerotheum_dust_pile>", "<contenttweaker:very_tiny_aerotheum_dust_pile>")),
    Item("aerotheum_dust", recipe=Recipe81("<contenttweaker:aerotheum_dust>", "<contenttweaker:tiny_aerotheum_dust_pile>")),
    Item("molten_aerothite", recipe=Recipe2xSurrounding("<contenttweaker:molten_aerothite>", "<contenttweaker:reinforced_steel_forge>", "<contenttweaker:aerotheum_dust_block>", "<contenttweaker:infernal_coke_block>")),
    Item("aerothite_nugget", recipe=Recipe2xSurroundingCheckerboard("<contenttweaker:aerothite_nugget>", "<contenttweaker:cryothite_metal_former>", "<contenttweaker:molten_aerothite>", "<contenttweaker:nugget_cast>", "<contenttweaker:pink_ice>")),
    Item("aerothite_ingot", recipe=Recipe81("<contenttweaker:aerothite_ingot>", "<contenttweaker:aerothite_nugget>")),
    Item("environmental_destroyer_v3", "Environmental Destroyer v3"),
    Item("life_infused_coke", recipe=Recipe2xSurroundingCheckerboard("<contenttweaker:life_infused_coke>", "<contenttweaker:reinforced_steel_refinery>", "<contenttweaker:environmental_destroyer_v3>", "<contenttweaker:infernal_coke_block>", "<contenttweaker:aerothite_block>")),
    Item("molten_altarus", recipe=RecipeAlloying("<contenttweaker:molten_altarus>", "<contenttweaker:reinforced_steel_forge>", "<contenttweaker:reinforced_steel_block>", "<contenttweaker:life_infused_coke_block>", "<contenttweaker:aerothite_block>")),
    Item("altarus_nugget", recipe=Recipe2xSurroundingCheckerboard("<contenttweaker:altarus_nugget>", "<contenttweaker:aerothite_metal_former>", "<contenttweaker:molten_altarus>", "<contenttweaker:nugget_cast>", "<contenttweaker:rose_gold_ice>")),
    Item("altarus_ingot", recipe=Recipe81("<contenttweaker:altarus_ingot>", "<contenttweaker:altarus_nugget>")),
    Item("altarus_forge_brick", recipe=RecipeCheckerboard("<contenttweaker:altarus_forge_brick>", "<contenttweaker:altarus_block>", "<contenttweaker:reinforced_steel_forge>")),
    Item("molten_tartarite", recipe=RecipeAlloying("<contenttweaker:molten_tartarite>", "<contenttweaker:altarus_forge>", "<contenttweaker:altarus_block>", "<contenttweaker:life_infused_coke_block>", "<contenttweaker:adamantium_block>")),
    Item("tartarite_nugget", recipe=Recipe2xSurroundingCheckerboard("<contenttweaker:tartarite_nugget>", "<contenttweaker:aerothite_metal_former>", "<contenttweaker:molten_tartarite>", "<contenttweaker:nugget_cast>", "<contenttweaker:rose_gold_ice>")),
    Item("tartarite_ingot", recipe=Recipe81("<contenttweaker:tartarite_ingot>", "<contenttweaker:tartarite_nugget>")),
    Item("basalz_rod", recipe=Recipe2xSurrounding("<contenttweaker:basalz_rod>", "<contenttweaker:earth_altar>", "<contenttweaker:blitz_block>", "<contenttweaker:quadruply_compressed_cobblestone>")),
    Item("molten_altarus_glass", recipe=Recipe2xSurroundingCheckerboard("<contenttweaker:molten_altarus_glass>", "<contenttweaker:altarus_glass_production_oven>", "<contenttweaker:reinforced_glass>", "<contenttweaker:altarus_block>", "<contenttweaker:life_infused_coke_block>")),
    Item("tartarite_forge_brick", recipe=RecipeCheckerboard("<contenttweaker:tartarite_forge_brick>", "<contenttweaker:tartarite_block>", "<contenttweaker:altarus_forge>")),
    Item("molten_tartarite_glass", recipe=Recipe2xSurroundingCheckerboard("<contenttweaker:molten_tartarite_glass>", "<contenttweaker:tartarite_glass_production_oven>", "<contenttweaker:altarus_glass>", "<contenttweaker:tartarite_block>", "<contenttweaker:life_infused_coke_block>")),
    Item("petrotheum_gas", recipe=RecipeChemistryStationCrafting("<contenttweaker:petrotheum_gas>", "<contenttweaker:tartarite_dust_mixer>", "<contenttweaker:tartarite_chemistry_station>", "<contenttweaker:basalz_block>", "<contenttweaker:basalz_block>", "<minecraft:redstone_block>", "<contenttweaker:quadruply_compressed_cobblestone>")),
    Item("very_tiny_petrotheum_dust_pile", recipe=Recipe2xSurrounding("<contenttweaker:very_tiny_petrotheum_dust_pile>", "<contenttweaker:tartarite_depositor>", "<contenttweaker:petrotheum_gas>", "<contenttweaker:rose_gold_ice>")),
    Item("tiny_petrotheum_dust_pile", recipe=Recipe81("<contenttweaker:tiny_petrotheum_dust_pile>", "<contenttweaker:very_tiny_petrotheum_dust_pile>")),
    Item("petrotheum_dust", recipe=Recipe81("<contenttweaker:petrotheum_dust>", "<contenttweaker:tiny_petrotheum_dust_pile>")),
    Item("molten_petrothite", recipe=Recipe2xSurrounding("<contenttweaker:molten_petrothite>", "<contenttweaker:tartarite_forge>", "<contenttweaker:petrotheum_dust_block>", "<contenttweaker:life_infused_coke_block>")),
    Item("petrothite_nugget", recipe=Recipe2xSurroundingCheckerboard("<contenttweaker:petrothite_nugget>", "<contenttweaker:aerothite_metal_former>", "<contenttweaker:molten_petrothite>", "<contenttweaker:nugget_cast>", "<contenttweaker:rose_gold_ice>")),
    Item("petrothite_ingot", recipe=Recipe81("<contenttweaker:petrothite_ingot>", "<contenttweaker:petrothite_nugget>")),
    Item("petrothite_forge_brick", recipe=RecipeCheckerboard("<contenttweaker:petrothite_forge_brick>", "<contenttweaker:petrothite_block>", "<contenttweaker:tartarite_forge>")),
    Item("molten_petrothite_glass", recipe=Recipe2xSurroundingCheckerboard("<contenttweaker:molten_petrothite_glass>", "<contenttweaker:petrothite_glass_production_oven>", "<contenttweaker:tartarite_glass>", "<contenttweaker:petrothite_block>", "<contenttweaker:life_infused_coke_block>")),
    Item("mana_gas"),
    Item("very_tiny_mana_dust_pile", recipe=Recipe2xSurrounding("<contenttweaker:very_tiny_mana_dust_pile>", "<contenttweaker:petrothite_depositor>", "<contenttweaker:mana_gas>", "<contenttweaker:rose_gold_ice>")),
    Item("tiny_mana_dust_pile", recipe=Recipe81("<contenttweaker:tiny_mana_dust_pile>", "<contenttweaker:very_tiny_mana_dust_pile>")),
    Item("mana_dust", recipe=Recipe81("<contenttweaker:mana_dust>", "<contenttweaker:tiny_mana_dust_pile>")),
    Item("molten_manalite", recipe=Recipe2xSurrounding("<contenttweaker:molten_manalite>", "<contenttweaker:petrothite_forge>", "<contenttweaker:mana_dust_block>", "<contenttweaker:life_infused_coke_block>")),
    Item("manalite_nugget", recipe=Recipe2xSurroundingCheckerboard("<contenttweaker:manalite_nugget>", "<contenttweaker:aerothite_metal_former>", "<contenttweaker:molten_manalite>", "<contenttweaker:nugget_cast>", "<contenttweaker:rose_gold_ice>")),
    Item("manalite_ingot", recipe=Recipe81("<contenttweaker:manalite_ingot>", "<contenttweaker:manalite_nugget>")),
    Item("manalite_forge_brick", recipe=RecipeCheckerboard("<contenttweaker:manalite_forge_brick>", "<contenttweaker:manalite_block>", "<contenttweaker:petrothite_forge>"))
]
