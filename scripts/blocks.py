from Recipe import *
from Tiers import tiers
from Object import Block

#List of every block in the game
blocks = [
    Block("compressed_cobblestone", tier=tiers["stone"], recipe=Recipe81("<contenttweaker:compressed_cobblestone>", "<minecraft:cobblestone>")),
    Block("stone_toolmaker", tier=tiers["stone"], recipe=RecipeToolmaker("<contenttweaker:stone_toolmaker>", "<contenttweaker:compressed_cobblestone>", "<minecraft:wooden_pickaxe>", "<minecraft:wooden_axe>", "<minecraft:wooden_shovel>", "<minecraft:wooden_hoe>", "<minecraft:wooden_sword>")),
    Block("blaze_block", tier=tiers["terracotta"], recipe=Recipe81("<contenttweaker:blaze_block>", "<minecraft:blaze_rod>")),
    Block("forge", tier=tiers["stone"], recipe=Recipe2xSurrounding("<contenttweaker:forge>", "<minecraft:furnace>", "<minecraft:coal_block>", "<contenttweaker:blaze_block>")),
    Block("metal_former", tier=tiers["stone"], recipe=RecipeSurrounding("<contenttweaker:metal_former>", "<minecraft:hardened_clay>", "<contenttweaker:blue_ice>")),
    Block("freezer", tier=tiers["terracotta"], recipe=RecipeFreezer("<contenttweaker:freezer>", "<minecraft:hardened_clay>", "<minecraft:snow>")),
    Block("blue_ice", tier=tiers["blue_ice"], recipe=RecipeSurrounding("<contenttweaker:blue_ice>", "<contenttweaker:freezer>", "<minecraft:packed_ice>")),
    Block("castmaker", tier=tiers["terracotta"], recipe=RecipeCastmaker("<contenttweaker:castmaker>", "<minecraft:hardened_clay>", "<contenttweaker:compressed_cobblestone>")),
    Block("compressed_netherrack", tier=tiers["stone"], recipe=Recipe81("<contenttweaker:compressed_netherrack>", "<minecraft:netherrack>")),
    Block("compressed_soulsand", "Compressed Soul Sand", tiers["stone"], Recipe81("<contenttweaker:compressed_soulsand>", "<minecraft:soul_sand>")),
    Block("blast_furnace_bricks", tier=tiers["blast_furnace"], recipe=Recipe81("<contenttweaker:blast_furnace_bricks>", "<contenttweaker:blast_furnace_brick>")),
    Block("blast_furnace_controller", tier=tiers["blast_furnace"], recipe=RecipeSurrounding("<contenttweaker:blast_furnace_controller>", "<contenttweaker:blast_furnace_bricks>", "<minecraft:iron_block>")),
    Block("blast_furnace", tier=tiers["blast_furnace"], recipe=RecipeSurrounding("<contenttweaker:blast_furnace>", "<contenttweaker:blast_furnace_bricks>", "<contenttweaker:blast_furnace_controller>")),
    Block("charcoal_block", tier=tiers["terracotta"], recipe=Recipe81("<contenttweaker:charcoal_block>", "<minecraft:coal:1>")),
    Block("gunpowder_block", tier=tiers["terracotta"], recipe=Recipe81("<contenttweaker:gunpowder_block>", "<minecraft:gunpowder>")),
    Block("steel_block", tier=tiers["steel"], recipe=Recipe81("<contenttweaker:steel_block>", "<contenttweaker:steel_ingot>")),
    Block("compressed_sandstone", tier=tiers["stone"], recipe=Recipe81("<contenttweaker:compressed_sandstone>", "<minecraft:sandstone:0>")),
    Block("placeholder_clay_block", tier=tiers["terracotta"], recipe=Recipe81("<contenttweaker:placeholder_clay_block>", "<contenttweaker:placeholder_clay>")),
    Block("coke_oven_bricks", tier=tiers["coke_oven"], recipe=Recipe81("<contenttweaker:coke_oven_bricks>", "<contenttweaker:coke_oven_brick>")),
    Block("coke_oven_controller", tier=tiers["coke_oven"], recipe=RecipeSurrounding("<contenttweaker:coke_oven_controller>", "<contenttweaker:coke_oven_bricks>", "<contenttweaker:charcoal_block>")),
    Block("coke_oven", tier=tiers["coke_oven"], recipe=RecipeSurrounding("<contenttweaker:coke_oven>", "<contenttweaker:coke_oven_bricks>", "<contenttweaker:coke_oven_controller>")),
    Block("coal_coke_block", tier=tiers["terracotta"], recipe=Recipe81("<contenttweaker:coal_coke_block>", "<contenttweaker:coal_coke>")),
    Block("steel_toolmaker", tier=tiers["steel"], recipe=RecipeToolmaker("<contenttweaker:steel_toolmaker>", "<contenttweaker:steel_block>", "<minecraft:stone_pickaxe>", "<minecraft:stone_axe>", "<minecraft:stone_shovel>", "<minecraft:stone_hoe>", "<minecraft:stone_sword>")),
    Block("leather_block", tier=tiers["terracotta"], recipe=Recipe81("<contenttweaker:leather_block>", "<minecraft:leather>")),
    Block("reinforced_leather_block", tier=tiers["reinforced_leather"], recipe=Recipe81("<contenttweaker:reinforced_leather_block>", "<contenttweaker:reinforced_leather>")),
    Block("leather_armormaker", tier=tiers["reinforced_leather"], recipe=RecipeCheckerboard("<contenttweaker:leather_armormaker>", "<contenttweaker:reinforced_leather_block>", "<contenttweaker:stone_toolmaker>")),
    Block("glass_production_oven", tier=tiers["steel"], recipe=RecipeCheckerboard("<contenttweaker:glass_production_oven>", "<contenttweaker:blast_furnace>", "<contenttweaker:steel_block>")),
    Block("block_basin", tier=tiers["steel"], recipe=RecipeBasin("<contenttweaker:block_basin>", "<contenttweaker:steel_block>", "<contenttweaker:blue_ice>")),
    Block("breaking_chamber", tier=tiers["steel"], recipe=RecipeSurrounding("<contenttweaker:breaking_chamber>", "<contenttweaker:steel_block>", "<minecraft:iron_pickaxe>")),
    Block("chains", tier=tiers["steel"], recipe=Recipe81("<contenttweaker:chains>", "<contenttweaker:chain>")),
    Block("chainmail_armormaker", tier=tiers["steel"], recipe=RecipeArmormaker("<contenttweaker:chainmail_armormaker>", "<contenttweaker:chains>", "<minecraft:leather_helmet>", "<minecraft:leather_chestplate>", "<minecraft:leather_leggings>", "<minecraft:leather_boots>")),
    Block("steel_armormaker", tier=tiers["steel"], recipe=RecipeArmormaker("<contenttweaker:steel_armormaker>", "<contenttweaker:steel_block>", "<minecraft:chainmail_helmet>", "<minecraft:chainmail_chestplate>", "<minecraft:chainmail_leggings>", "<minecraft:chainmail_boots>")),
    Block("reinforced_wool", tier=tiers["steel"], recipe=Recipe81("<contenttweaker:reinforced_wool>", "<contenttweaker:reinforced_string>")),
    Block("flint_block", tier=tiers["terracotta"], recipe=Recipe81("<contenttweaker:flint_block>", "<minecraft:flint>")),
    Block("reinforced_featherwool", tier=tiers["steel"], recipe=Recipe81("<contenttweaker:reinforced_featherwool>", "<contenttweaker:reinforced_feather>")),
    Block("steel_forge_bricks", tier=tiers["steel"], recipe=Recipe81("<contenttweaker:steel_forge_bricks>", "<contenttweaker:steel_forge_brick>")),
    Block("steel_forge_controller", tier=tiers["steel"], recipe=RecipeSurrounding("<contenttweaker:steel_forge_controller>", "<contenttweaker:steel_forge_bricks>", "<contenttweaker:steel_block>")),
    Block("steel_forge", tier=tiers["steel"], recipe=RecipeSurrounding("<contenttweaker:steel_forge>", "<contenttweaker:steel_forge_bricks>", "<contenttweaker:steel_forge_controller>")),
    Block("steel_tank", tier=tiers["steel"], recipe=RecipeSurrounding("<contenttweaker:steel_tank>", "<contenttweaker:steel_block>", "<minecraft:glass>")),
    Block("dust_refiner", tier=tiers["steel"], recipe=RecipeDustRefiner("<contenttweaker:dust_refiner>", "<contenttweaker:steel_block>", "<contenttweaker:steel_tank>", "<contenttweaker:gunpowder_block>", "<minecraft:redstone_block>", "<minecraft:glowstone>")),
    Block("condensator", tier=tiers["steel"], recipe=Recipe2xSurrounding("<contenttweaker:condensator>", "<contenttweaker:steel_block>", "<contenttweaker:steel_tank>", "<contenttweaker:freezer>")),
    Block("steel_freezer", tier=tiers["steel"], recipe=Recipe2xSurrounding("<contenttweaker:steel_freezer>", "<contenttweaker:steel_block>", "<contenttweaker:freezer>", "<contenttweaker:condensator>")),
    Block("depositor", tier=tiers["steel"], recipe=Recipe2xSurrounding("<contenttweaker:depositor>", "<contenttweaker:steel_block>", "<contenttweaker:condensator>", "<contenttweaker:steel_freezer>")),
    Block("evaporator", tier=tiers["steel"], recipe=Recipe2xSurrounding("<contenttweaker:evaporator>", "<contenttweaker:steel_block>", "<contenttweaker:steel_tank>", "<contenttweaker:blaze_block>")),
    Block("gas_separator", tier=tiers["steel"], recipe=RecipeSurrounding("<contenttweaker:gas_separator>", "<contenttweaker:steel_block>", "<contenttweaker:steel_turbine>")),
    Block("chemistry_station", tier=tiers["steel"], recipe=Recipe2xSurrounding("<contenttweaker:chemistry_station>", "<contenttweaker:steel_block>", "<contenttweaker:beaker>", "<contenttweaker:steel_tank>")),
    Block("sulfur_block", tier=tiers["steel"], recipe=Recipe81("<contenttweaker:sulfur_block>", "<contenttweaker:sulfur>")),
    Block("dust_mixer", tier=tiers["steel"], recipe=Recipe2xSurrounding("<contenttweaker:dust_mixer>", "<contenttweaker:steel_block>", "<contenttweaker:dust_refiner>", "<contenttweaker:chemistry_station>")),
    Block("pyrotheum_dust_block", tier=tiers["steel"], recipe=Recipe81("<contenttweaker:pyrotheum_dust_block>", "<contenttweaker:pyrotheum_dust>")),
    Block("purple_ice", tier=tiers["steel"], recipe=RecipeSurrounding("<contenttweaker:purple_ice>", "<contenttweaker:steel_freezer>", "<contenttweaker:blue_ice>")),
    Block("steel_metal_former", tier=tiers["steel"], recipe=Recipe2xSurrounding("<contenttweaker:steel_metal_former>", "<contenttweaker:steel_freezer>", "<contenttweaker:metal_former>", "<contenttweaker:purple_ice>")),
    Block("pyrothite_block", tier=tiers["pyrothite"], recipe=Recipe81("<contenttweaker:pyrothite_block>", "<contenttweaker:pyrothite_ingot>")),
    Block("pyrothite_forge_bricks", tier=tiers["pyrothite"], recipe=Recipe81("<contenttweaker:pyrothite_forge_bricks>", "<contenttweaker:pyrothite_forge_brick>")),
    Block("pyrothite_forge_controller", tier=tiers["pyrothite"], recipe=RecipeSurrounding("<contenttweaker:pyrothite_forge_controller>", "<contenttweaker:pyrothite_forge_bricks>", "<contenttweaker:pyrothite_block>")),
    Block("pyrothite_forge", tier=tiers["pyrothite"], recipe=RecipeSurrounding("<contenttweaker:pyrothite_forge>", "<contenttweaker:pyrothite_forge_bricks>", "<contenttweaker:pyrothite_forge_controller>")),
    Block("refinery", tier=tiers["pyrothite"], recipe=Recipe2xSurrounding("<contenttweaker:refinery>", "<contenttweaker:steel_block>", "<contenttweaker:environmental_destroyer>", "<contenttweaker:pyrothite_forge>")),
    Block("refined_coke_block", tier=tiers["terracotta"], recipe=Recipe81("<contenttweaker:refined_coke_block>", "<contenttweaker:refined_coke>")),
    Block("blizz_block", tier=tiers["terracotta"], recipe=Recipe81("<contenttweaker:blizz_block>", "<contenttweaker:blizz_rod>")),
    Block("pyrothite_chemistry_station", tier=tiers["pyrothite"], recipe=Recipe2xSurrounding("<contenttweaker:pyrothite_chemistry_station>", "<contenttweaker:pyrothite_block>", "<contenttweaker:chemistry_station>", "<contenttweaker:pyrothite_tank>")),
    Block("pyrothite_dust_mixer", tier=tiers["pyrothite"], recipe=Recipe2xSurrounding("<contenttweaker:pyrothite_dust_mixer>", "<contenttweaker:pyrothite_block>", "<contenttweaker:pyrothite_dust_refiner>", "<contenttweaker:pyrothite_chemistry_station>")),
    Block("pyrothite_dust_refiner", tier=tiers["pyrothite"], recipe=Recipe2xSurrounding("<contenttweaker:pyrothite_dust_refiner>", "<contenttweaker:pyrothite_block>", "<contenttweaker:dust_refiner>", "<contenttweaker:pyrothite_tank>")),
    Block("pyrothite_tank", tier=tiers["pyrothite"], recipe=RecipeSurrounding("<contenttweaker:pyrothite_tank>", "<contenttweaker:pyrothite_tank_wall>", "<contenttweaker:pyrothite_tank_controller>")),
    Block("pyrothite_tank_wall", tier=tiers["pyrothite"], recipe=RecipeSurrounding("<contenttweaker:pyrothite_tank_wall>", "<contenttweaker:pyrothite_block>", "<contenttweaker:platinum_infused_glass>")),
    Block("pyrothite_tank_glass", tier=tiers["pyrothite"], recipe=RecipeSurrounding("<contenttweaker:pyrothite_tank_glass>", "<contenttweaker:pyrothite_tank_wall>", "<contenttweaker:platinum_infused_glass>")),
    Block("pyrothite_tank_controller", tier=tiers["pyrothite"], recipe=RecipeSurrounding("<contenttweaker:pyrothite_tank_controller>", "<contenttweaker:pyrothite_tank_wall>", "<contenttweaker:pyrothite_tank_glass>")),
    Block("platinum_block", tier=tiers["platinum"], recipe=Recipe81("<contenttweaker:platinum_block>", "<contenttweaker:platinum_ingot>")),
    Block("platinum_infused_glass", tier=tiers["platinum"], recipe=Recipe2xSurrounding("<contenttweaker:platinum_infused_glass>", "<contenttweaker:block_basin_mk2>", "<contenttweaker:molten_platinum_infused_glass>", "<contenttweaker:purple_ice>")),
    Block("block_basin_mk2", "Block Basin v2", tiers["pyrothite"], Recipe2xSurrounding("<contenttweaker:block_basin_mk2>", "<contenttweaker:platinum_block>", "<contenttweaker:block_basin>", "<contenttweaker:purple_ice>")),
    Block("pyrothite_glass_production_oven", tier=tiers["pyrothite"], recipe=RecipeCheckerboard("<contenttweaker:pyrothite_glass_production_oven>", "<contenttweaker:pyrothite_forge>", "<contenttweaker:platinum_block>")),
    Block("cryotheum_dust_block", tier=tiers["pyrothite"], recipe=Recipe81("<contenttweaker:cryotheum_dust_block>", "<contenttweaker:cryotheum_dust>")),
    Block("cryothite_block", tier=tiers["cryothite"], recipe=Recipe81("<contenttweaker:cryothite_block>", "<contenttweaker:cryothite_ingot>")),
    Block("cryothite_freezer", tier=tiers["cryothite"], recipe=Recipe2xSurrounding("<contenttweaker:cryothite_freezer>", "<contenttweaker:cryothite_block>", "<contenttweaker:steel_freezer>", "<contenttweaker:purple_ice>")),
    Block("pink_ice", tier=tiers["pink_ice"], recipe=RecipeSurrounding("<contenttweaker:pink_ice>", "<contenttweaker:cryothite_freezer>", "<contenttweaker:purple_ice>")),
    Block("reinforced_obsidian", tier=tiers["reinforced_obsidian"], recipe=Recipe2xSurrounding("<contenttweaker:reinforced_obsidian>", "<minecraft:obsidian>", "<extendedcrafting:storage:2>", "<contenttweaker:cryothite_block>")),
    Block("air_altar", tier=tiers["cryothite"], recipe=Recipe2xSurrounding("<contenttweaker:air_altar>", "<minecraft:beacon>", "<contenttweaker:pink_ice>", "<extendedcrafting:storage:2>")),
    Block("blitz_block", tier=tiers["cryothite"], recipe=Recipe81("<contenttweaker:blitz_block>", "<contenttweaker:blitz_rod>")),
    Block("infernium_block", tier=tiers["infernium"], recipe=Recipe81("<contenttweaker:infernium_block>", "<contenttweaker:infernium_ingot>")),
    Block("cryothite_metal_former", tier=tiers["cryothite"], recipe=Recipe2xSurrounding("<contenttweaker:cryothite_metal_former>", "<contenttweaker:cryothite_freezer>", "<contenttweaker:steel_metal_former>", "<contenttweaker:pink_ice>")),
    Block("infernium_forge_bricks", tier=tiers["infernium"], recipe=Recipe81("<contenttweaker:infernium_forge_bricks>", "<contenttweaker:infernium_forge_brick>")),
    Block("infernium_forge_controller", tier=tiers["infernium"], recipe=RecipeSurrounding("<contenttweaker:infernium_forge_controller>", "<contenttweaker:infernium_forge_bricks>", "<contenttweaker:infernium_block>")),
    Block("infernium_forge", tier=tiers["infernium"], recipe=RecipeSurrounding("<contenttweaker:infernium_forge>", "<contenttweaker:infernium_forge_bricks>", "<contenttweaker:infernium_forge_controller>")),
    Block("mithril_block", tier=tiers["mithril"], recipe=Recipe81("<contenttweaker:mithril_block>", "<contenttweaker:mithril_ingot>")),
    Block("infernal_coke_block", tier=tiers["infernal_coke"], recipe=Recipe81("<contenttweaker:infernal_coke_block>", "<contenttweaker:infernal_coke>")),
    Block("infernium_refinery", tier=tiers["infernium"], recipe=Recipe2xSurrounding("<contenttweaker:infernium_refinery>", "<contenttweaker:refinery>", "<contenttweaker:environmental_destroyer_v2>", "<contenttweaker:infernium_forge>")),
    Block("adamantium_block", tier=tiers["adamantium"], recipe=Recipe81("<contenttweaker:adamantium_block>", "<contenttweaker:adamantium_ingot>")),
    Block("mithril_forge_bricks", tier=tiers["mithril"], recipe=Recipe81("<contenttweaker:mithril_forge_bricks>", "<contenttweaker:mithril_forge_brick>")),
    Block("mithril_forge_controller", tier=tiers["mithril"], recipe=RecipeSurrounding("<contenttweaker:mithril_forge_controller>", "<contenttweaker:mithril_forge_bricks>", "<contenttweaker:mithril_block>")),
    Block("mithril_forge", tier=tiers["mithril"], recipe=RecipeSurrounding("<contenttweaker:mithril_forge>", "<contenttweaker:mithril_forge_bricks>", "<contenttweaker:mithril_forge_controller>")),
    Block("adamantium_forge_bricks", tier=tiers["adamantium"], recipe=Recipe81("<contenttweaker:adamantium_forge_bricks>", "<contenttweaker:adamantium_forge_brick>")),
    Block("adamantium_forge_controller", tier=tiers["adamantium"], recipe=RecipeSurrounding("<contenttweaker:adamantium_forge_controller>", "<contenttweaker:adamantium_forge_bricks>", "<contenttweaker:adamantium_block>")),
    Block("adamantium_forge", tier=tiers["adamantium"], recipe=RecipeSurrounding("<contenttweaker:adamantium_forge>", "<contenttweaker:adamantium_forge_bricks>", "<contenttweaker:adamantium_forge_controller>")),
    Block("reinforced_steel_block", tier=tiers["reinforced steel"], recipe=Recipe81("<contenttweaker:reinforced_steel_block>", "<contenttweaker:reinforced_steel_ingot>")),
    Block("block_basin_mk3", "Block Basin v3", tiers["reinforced steel"], Recipe2xSurrounding("<contenttweaker:block_basin_mk3>", "<contenttweaker:reinforced_steel_block>", "<contenttweaker:block_basin_mk2>", "<contenttweaker:pink_ice>")),
    Block("reinforced_steel_glass_production_oven", tier=tiers["reinforced steel"], recipe=Recipe2xSurrounding("<contenttweaker:reinforced_steel_glass_production_oven>", "<contenttweaker:reinforced_steel_forge>", "<contenttweaker:pyrothite_glass_production_oven>", "<contenttweaker:platinum_infused_glass>")),
    Block("reinforced_steel_forge_bricks", tier=tiers["reinforced steel"], recipe=Recipe81("<contenttweaker:reinforced_steel_forge_bricks>", "<contenttweaker:reinforced_steel_forge_brick>")),
    Block("reinforced_steel_forge_controller", tier=tiers["reinforced steel"], recipe=RecipeSurrounding("<contenttweaker:reinforced_steel_forge_controller>", "<contenttweaker:reinforced_steel_forge_bricks>", "<contenttweaker:reinforced_steel_block>")),
    Block("reinforced_steel_forge", tier=tiers["reinforced steel"], recipe=RecipeSurrounding("<contenttweaker:reinforced_steel_forge>", "<contenttweaker:reinforced_steel_forge_bricks>", "<contenttweaker:reinforced_steel_forge_controller>")),
    Block("reinforced_glass", tier=tiers["reinforced steel"], recipe=Recipe2xSurrounding("<contenttweaker:reinforced_glass>", "<contenttweaker:block_basin_mk3>", "<contenttweaker:molten_reinforced_glass>", "<contenttweaker:pink_ice>")),
    Block("reinforced_steel_tank_wall", tier=tiers["reinforced steel"], recipe=RecipeSurrounding("<contenttweaker:reinforced_steel_tank_wall>", "<contenttweaker:reinforced_steel_block>", "<contenttweaker:reinforced_glass>")),
    Block("reinforced_steel_tank_glass", tier=tiers["reinforced steel"], recipe=RecipeSurrounding("<contenttweaker:reinforced_steel_tank_glass>", "<contenttweaker:reinforced_steel_tank_wall>", "<contenttweaker:reinforced_glass>")),
    Block("reinforced_steel_tank_controller", tier=tiers["reinforced steel"], recipe=RecipeSurrounding("<contenttweaker:reinforced_steel_tank_controller>", "<contenttweaker:reinforced_steel_tank_wall>", "<contenttweaker:reinforced_steel_tank_glass>")),
    Block("reinforced_steel_tank", tier=tiers["reinforced steel"], recipe=RecipeSurrounding("<contenttweaker:reinforced_steel_tank>", "<contenttweaker:reinforced_steel_tank_wall>", "<contenttweaker:reinforced_steel_tank_controller>")),
    Block("reinforced_steel_chemistry_station", tier=tiers["reinforced steel"], recipe=Recipe2xSurrounding("<contenttweaker:reinforced_steel_chemistry_station>", "<contenttweaker:reinforced_steel_block>", "<contenttweaker:pyrothite_chemistry_station>", "<contenttweaker:reinforced_steel_tank>")),
    Block("reinforced_steel_dust_mixer", tier=tiers["reinforced steel"], recipe=Recipe2xSurrounding("<contenttweaker:reinforced_steel_dust_mixer>", "<contenttweaker:reinforced_steel_block>", "<contenttweaker:reinforced_steel_dust_refiner>", "<contenttweaker:reinforced_steel_chemistry_station>")),
    Block("reinforced_steel_dust_refiner", tier=tiers["reinforced steel"], recipe=Recipe2xSurrounding("<contenttweaker:reinforced_steel_dust_refiner>", "<contenttweaker:reinforced_steel_block>", "<contenttweaker:pyrothite_dust_refiner>", "<contenttweaker:reinforced_steel_tank>")),
    Block("beetroot_block", tier=tiers["terracotta"], recipe=Recipe81("<contenttweaker:beetroot_block>", "<minecraft:beetroot>")),
    Block("grindstone", tier=tiers["stone"], recipe=RecipeSurrounding("<contenttweaker:grindstone>", "<contenttweaker:compressed_cobblestone>", "<contenttweaker:stone_gear>")),
    Block("steel_oven", tier=tiers["steel"], recipe=Recipe2xSurrounding("<contenttweaker:steel_oven>", "<contenttweaker:steel_block>", "<minecraft:hardened_clay>", "<contenttweaker:steel_forge>")),
    Block("apple_block", tier=tiers["terracotta"], recipe=Recipe81("<contenttweaker:apple_block>", "<minecraft:apple>")),
    Block("sugar_cane_block", tier=tiers["blue_ice"], recipe=Recipe81("<contenttweaker:sugar_cane_block>", "<minecraft:reeds>")),
    Block("paper_block", tier=tiers["blue_ice"], recipe=Recipe81("<contenttweaker:paper_block>", "<minecraft:paper>")),
    Block("egg_block", tier=tiers["terracotta"], recipe=Recipe81("<contenttweaker:egg_block>", "<minecraft:egg>")),
    Block("sugar_block", tier=tiers["blue_ice"], recipe=Recipe81("<contenttweaker:sugar_block>", "<minecraft:sugar>")),
    Block("cocoa_block", tier=tiers["blue_ice"], recipe=Recipe81("<contenttweaker:cocoa_block>", "<minecraft:dye:3>")),
    Block("flesh_block", tier=tiers["terracotta"], recipe=Recipe81("<contenttweaker:flesh_block>", "<minecraft:rotten_flesh>")),
    Block("spider_eye_block", tier=tiers["terracotta"], recipe=Recipe81("<contenttweaker:spider_eye_block>", "<minecraft:spider_eye>")),
    Block("carrot_block", tier=tiers["blue_ice"], recipe=Recipe81("<contenttweaker:carrot_block>", "<minecraft:carrot>")),
    Block("potato_block", tier=tiers["blue_ice"], recipe=Recipe81("<contenttweaker:potato_block>", "<minecraft:potato>")),
    Block("poisonous_potato_block", tier=tiers["blue_ice"], recipe=Recipe81("<contenttweaker:poisonous_potato_block>", "<minecraft:poisonous_potato>")),
    Block("life_altar", tier=tiers["cryothite"], recipe=RecipeSurrounding("<contenttweaker:life_altar>", "<contenttweaker:air_altar>", "<contenttweaker:weird_food>")),
    Block("greenhouse", tier=tiers["reinforced steel"], recipe=RecipeSurrounding("<contenttweaker:greenhouse>", "<contenttweaker:reinforced_steel_block>", "<contenttweaker:life_altar>")),
    Block("banana_block", tier=tiers["terracotta"], recipe=Recipe81("<contenttweaker:banana_block>", "<contenttweaker:banana>")),
    Block("reinforced_steel_condensator", tier=tiers["reinforced steel"], recipe=Recipe2xSurrounding("<contenttweaker:reinforced_steel_condensator>", "<contenttweaker:reinforced_steel_block>", "<contenttweaker:reinforced_steel_tank>", "<contenttweaker:cryothite_freezer>")),
    Block("reinforced_steel_depositor", tier=tiers["reinforced steel"], recipe=Recipe2xSurrounding("<contenttweaker:reinforced_steel_depositor>", "<contenttweaker:reinforced_steel_block>", "<contenttweaker:reinforced_steel_condensator>", "<contenttweaker:cryothite_freezer>")),
    Block("niter_block", tier=tiers["steel"], recipe=Recipe81("<contenttweaker:niter_block>", "<contenttweaker:niter>")),
    Block("aerotheum_dust_block", tier=tiers["reinforced steel"], recipe=Recipe81("<contenttweaker:aerotheum_dust_block>", "<contenttweaker:aerotheum_dust>")),
    Block("aerothite_block", tier=tiers["aerothite"], recipe=Recipe81("<contenttweaker:aerothite_block>", "<contenttweaker:aerothite_ingot>")),
    Block("aerothite_freezer", tier=tiers["aerothite"], recipe=Recipe2xSurrounding("<contenttweaker:aerothite_freezer>", "<contenttweaker:aerothite_block>", "<contenttweaker:cryothite_freezer>", "<contenttweaker:pink_ice>")),
    Block("reinforced_steel_refinery", tier=tiers["reinforced steel"], recipe=Recipe2xSurrounding("<contenttweaker:reinforced_steel_refinery>", "<contenttweaker:infernium_refinery>", "<contenttweaker:environmental_destroyer_v3>", "<contenttweaker:reinforced_steel_forge>")),
    Block("life_infused_coke_block", tier=tiers["life infused coke"], recipe=Recipe81("<contenttweaker:life_infused_coke_block>", "<contenttweaker:life_infused_coke>")),
    Block("rose_gold_ice", tier=tiers["aerothite"], recipe=RecipeSurrounding("<contenttweaker:rose_gold_ice>", "<contenttweaker:aerothite_freezer>", "<contenttweaker:pink_ice>")),
    Block("aerothite_metal_former", tier=tiers["aerothite"], recipe=Recipe2xSurrounding("<contenttweaker:aerothite_metal_former>", "<contenttweaker:aerothite_freezer>", "<contenttweaker:cryothite_metal_former>", "<contenttweaker:rose_gold_ice>")),
    Block("altarus_block", tier=tiers["altarus"], recipe=Recipe81("<contenttweaker:altarus_block>", "<contenttweaker:altarus_ingot>")),
    Block("altarus_forge_bricks", tier=tiers["altarus"], recipe=Recipe81("<contenttweaker:altarus_forge_bricks>", "<contenttweaker:altarus_forge_brick>")),
    Block("altarus_forge_controller", tier=tiers["altarus"], recipe=RecipeSurrounding("<contenttweaker:altarus_forge_controller>", "<contenttweaker:altarus_forge_bricks>", "<contenttweaker:altarus_block>")),
    Block("altarus_forge", tier=tiers["altarus"], recipe=RecipeSurrounding("<contenttweaker:altarus_forge>", "<contenttweaker:altarus_forge_bricks>", "<contenttweaker:altarus_forge_controller>")),
    Block("tartarite_block", tier=tiers["tartarite"], recipe=Recipe81("<contenttweaker:tartarite_block>", "<contenttweaker:tartarite_ingot>")),
    Block("compression_chamber", tier=tiers["tartarite"], recipe=RecipeSurrounding("<contenttweaker:compression_chamber>", "<contenttweaker:tartarite_block>", "<contenttweaker:reinforced_obsidian>")),
    Block("doubly_compressed_cobblestone", tier=tiers["cobble2x"]),
    Block("triply_compressed_cobblestone", tier=tiers["cobble2x"]),
    Block("quadruply_compressed_cobblestone", tier=tiers["cobble2x"]),
    Block("earth_altar", tier=tiers["cobble2x"], recipe=RecipeSurrounding("<contenttweaker:earth_altar>", "<contenttweaker:life_altar>", "<contenttweaker:quadruply_compressed_cobblestone>")),
    Block("basalz_block", tier=tiers["aerothite"], recipe=Recipe81("<contenttweaker:basalz_block>", "<contenttweaker:basalz_rod>")),
    Block("block_basin_mk4", "Block Basin v4", tiers["tartarite"], recipe=Recipe2xSurrounding("<contenttweaker:block_basin_mk4>", "<contenttweaker:tartarite_block>", "<contenttweaker:block_basin_mk3>", "<contenttweaker:rose_gold_ice>")),
    Block("altarus_glass_production_oven", tier=tiers["altarus"], recipe=Recipe2xSurrounding("<contenttweaker:altarus_glass_production_oven>", "<contenttweaker:altarus_forge>", "<contenttweaker:reinforced_steel_glass_production_oven>", "<contenttweaker:reinforced_glass>")),
    Block("altarus_glass", tier=tiers["altarus"], recipe=Recipe2xSurrounding("<contenttweaker:altarus_glass>", "<contenttweaker:block_basin_mk4>", "<contenttweaker:molten_altarus_glass>", "<contenttweaker:rose_gold_ice>")),
    Block("altarus_tank_wall", tier=tiers["altarus"], recipe=RecipeSurrounding("<contenttweaker:altarus_tank_wall>", "<contenttweaker:altarus_block>", "<contenttweaker:altarus_glass>")),
    Block("altarus_tank_glass", tier=tiers["altarus"], recipe=RecipeSurrounding("<contenttweaker:altarus_tank_glass>", "<contenttweaker:altarus_tank_wall>", "<contenttweaker:altarus_glass>")),
    Block("altarus_tank_controller", tier=tiers["altarus"], recipe=RecipeSurrounding("<contenttweaker:altarus_tank_controller>", "<contenttweaker:altarus_tank_wall>", "<contenttweaker:altarus_tank_glass>")),
    Block("altarus_tank", tier=tiers["altarus"], recipe=RecipeSurrounding("<contenttweaker:altarus_tank>", "<contenttweaker:altarus_tank_wall>", "<contenttweaker:altarus_tank_controller>")),
    Block("altarus_chemistry_station", tier=tiers["altarus"], recipe=Recipe2xSurrounding("<contenttweaker:altarus_chemistry_station>", "<contenttweaker:altarus_block>", "<contenttweaker:reinforced_steel_chemistry_station>", "<contenttweaker:altarus_tank>")),
    Block("altarus_dust_refiner", tier=tiers["altarus"], recipe=Recipe2xSurrounding("<contenttweaker:altarus_dust_refiner>", "<contenttweaker:altarus_block>", "<contenttweaker:reinforced_steel_dust_refiner>", "<contenttweaker:altarus_tank>")),
    Block("altarus_dust_mixer", tier=tiers["altarus"], recipe=Recipe2xSurrounding("<contenttweaker:altarus_dust_mixer>", "<contenttweaker:altarus_block>", "<contenttweaker:altarus_dust_refiner>", "<contenttweaker:altarus_chemistry_station>")),
    Block("tartarite_glass_production_oven", tier=tiers["tartarite"], recipe=Recipe2xSurrounding("<contenttweaker:tartarite_glass_production_oven>", "<contenttweaker:tartarite_forge>", "<contenttweaker:altarus_glass_production_oven>", "<contenttweaker:altarus_glass>")),
    Block("tartarite_forge_bricks", tier=tiers["tartarite"], recipe=Recipe81("<contenttweaker:tartarite_forge_bricks>", "<contenttweaker:tartarite_forge_brick>")),
    Block("tartarite_forge_controller", tier=tiers["tartarite"], recipe=RecipeSurrounding("<contenttweaker:tartarite_forge_controller>", "<contenttweaker:tartarite_forge_bricks>", "<contenttweaker:tartarite_block>")),
    Block("tartarite_forge", tier=tiers["tartarite"], recipe=RecipeSurrounding("<contenttweaker:tartarite_forge>", "<contenttweaker:tartarite_forge_bricks>", "<contenttweaker:tartarite_forge_controller>")),
    Block("tartarite_glass", tier=tiers["tartarite"], recipe=Recipe2xSurrounding("<contenttweaker:tartarite_glass>", "<contenttweaker:block_basin_mk4>", "<contenttweaker:molten_tartarite_glass>", "<contenttweaker:rose_gold_ice>")),
    Block("tartarite_tank_wall", tier=tiers["tartarite"], recipe=RecipeSurrounding("<contenttweaker:tartarite_tank_wall>", "<contenttweaker:tartarite_block>", "<contenttweaker:tartarite_glass>")),
    Block("tartarite_tank_glass", tier=tiers["tartarite"], recipe=RecipeSurrounding("<contenttweaker:tartarite_tank_glass>", "<contenttweaker:tartarite_tank_wall>", "<contenttweaker:tartarite_glass>")),
    Block("tartarite_tank_controller", tier=tiers["tartarite"], recipe=RecipeSurrounding("<contenttweaker:tartarite_tank_controller>", "<contenttweaker:tartarite_tank_wall>", "<contenttweaker:tartarite_tank_glass>")),
    Block("tartarite_tank", tier=tiers["tartarite"], recipe=RecipeSurrounding("<contenttweaker:tartarite_tank>", "<contenttweaker:tartarite_tank_wall>", "<contenttweaker:tartarite_tank_controller>")),
    Block("tartarite_chemistry_station", tier=tiers["tartarite"], recipe=Recipe2xSurrounding("<contenttweaker:tartarite_chemistry_station>", "<contenttweaker:tartarite_block>", "<contenttweaker:altarus_chemistry_station>", "<contenttweaker:tartarite_tank>")),
    Block("tartarite_dust_refiner", tier=tiers["tartarite"], recipe=Recipe2xSurrounding("<contenttweaker:tartarite_dust_refiner>", "<contenttweaker:tartarite_block>", "<contenttweaker:altarus_dust_refiner>", "<contenttweaker:tartarite_tank>")),
    Block("tartarite_dust_mixer", tier=tiers["tartarite"], recipe=Recipe2xSurrounding("<contenttweaker:tartarite_dust_mixer>", "<contenttweaker:tartarite_block>", "<contenttweaker:tartarite_dust_refiner>", "<contenttweaker:tartarite_chemistry_station>")),
    Block("altarus_condensator", tier=tiers["altarus"], recipe=Recipe2xSurroundingCheckerboard("<contenttweaker:altarus_condensator>", "<contenttweaker:altarus_block>", "<contenttweaker:altarus_tank>", "<contenttweaker:aerothite_freezer>", "<contenttweaker:reinforced_steel_condensator>")),
    Block("altarus_depositor", tier=tiers["altarus"], recipe=Recipe2xSurrounding("<contenttweaker:altarus_depositor>", "<contenttweaker:altarus_block>", "<contenttweaker:altarus_condensator>", "<contenttweaker:reinforced_steel_depositor>")),
    Block("tartarite_condensator", tier=tiers["tartarite"], recipe=Recipe2xSurroundingCheckerboard("<contenttweaker:tartarite_condensator>", "<contenttweaker:tartarite_block>", "<contenttweaker:tartarite_tank>", "<contenttweaker:aerothite_freezer>", "<contenttweaker:altarus_condensator>")),
    Block("tartarite_depositor", tier=tiers["tartarite"], recipe=Recipe2xSurrounding("<contenttweaker:tartarite_depositor>", "<contenttweaker:tartarite_block>", "<contenttweaker:tartarite_condensator>", "<contenttweaker:altarus_depositor>")),
    Block("petrotheum_dust_block", tier=tiers["tartarite"], recipe=Recipe81("<contenttweaker:petrotheum_dust_block>", "<contenttweaker:petrotheum_dust>")),
    Block("petrothite_block", tier=tiers["petrothite"], recipe=Recipe81("<contenttweaker:petrothite_block>", "<contenttweaker:petrothite_ingot>")),
    Block("petrothite_forge_bricks", tier=tiers["petrothite"], recipe=Recipe81("<contenttweaker:petrothite_forge_bricks>", "<contenttweaker:petrothite_forge_brick>")),
    Block("petrothite_forge_controller", tier=tiers["petrothite"], recipe=RecipeSurrounding("<contenttweaker:petrothite_forge_controller>", "<contenttweaker:petrothite_forge_bricks>", "<contenttweaker:petrothite_block>")),
    Block("petrothite_forge", tier=tiers["petrothite"], recipe=RecipeSurrounding("<contenttweaker:petrothite_forge>", "<contenttweaker:petrothite_forge_bricks>", "<contenttweaker:petrothite_forge_controller>")),
    Block("petrothite_glass_production_oven", tier=tiers["petrothite"], recipe=Recipe2xSurrounding("<contenttweaker:petrothite_glass_production_oven>", "<contenttweaker:petrothite_forge>", "<contenttweaker:tartarite_glass_production_oven>", "<contenttweaker:tartarite_glass>")),
    Block("petrothite_glass", tier=tiers["petrothite"], recipe=Recipe2xSurrounding("<contenttweaker:petrothite_glass>", "<contenttweaker:block_basin_mk4>", "<contenttweaker:molten_petrothite_glass>", "<contenttweaker:rose_gold_ice>")),
    Block("petrothite_tank_wall", tier=tiers["petrothite"], recipe=RecipeSurrounding("<contenttweaker:petrothite_tank_wall>", "<contenttweaker:petrothite_block>", "<contenttweaker:petrothite_glass>")),
    Block("petrothite_tank_glass", tier=tiers["petrothite"], recipe=RecipeSurrounding("<contenttweaker:petrothite_tank_glass>", "<contenttweaker:petrothite_tank_wall>", "<contenttweaker:petrothite_glass>")),
    Block("petrothite_tank_controller", tier=tiers["petrothite"], recipe=RecipeSurrounding("<contenttweaker:petrothite_tank_controller>", "<contenttweaker:petrothite_tank_wall>", "<contenttweaker:petrothite_tank_glass>")),
    Block("petrothite_tank", tier=tiers["petrothite"], recipe=RecipeSurrounding("<contenttweaker:petrothite_tank>", "<contenttweaker:petrothite_tank_wall>", "<contenttweaker:petrothite_tank_controller>")),
    Block("petrothite_chemistry_station", tier=tiers["petrothite"], recipe=Recipe2xSurrounding("<contenttweaker:petrothite_chemistry_station>", "<contenttweaker:petrothite_block>", "<contenttweaker:tartarite_chemistry_station>", "<contenttweaker:petrothite_tank>")),
    Block("petrothite_dust_refiner", tier=tiers["petrothite"], recipe=Recipe2xSurrounding("<contenttweaker:petrothite_dust_refiner>", "<contenttweaker:petrothite_block>", "<contenttweaker:tartarite_dust_refiner>", "<contenttweaker:petrothite_tank>")),
    Block("petrothite_dust_mixer", tier=tiers["petrothite"], recipe=Recipe2xSurrounding("<contenttweaker:petrothite_dust_mixer>", "<contenttweaker:petrothite_block>", "<contenttweaker:petrothite_dust_refiner>", "<contenttweaker:petrothite_chemistry_station>")),
    Block("petrothite_condensator", tier=tiers["petrothite"], recipe=Recipe2xSurroundingCheckerboard("<contenttweaker:petrothite_condensator>", "<contenttweaker:petrothite_block>", "<contenttweaker:petrothite_tank>", "<contenttweaker:aerothite_freezer>", "<contenttweaker:tartarite_condensator>")),
    Block("petrothite_depositor", tier=tiers["petrothite"], recipe=Recipe2xSurrounding("<contenttweaker:petrothite_depositor>", "<contenttweaker:petrothite_block>", "<contenttweaker:petrothite_condensator>", "<contenttweaker:tartarite_depositor>")),
    Block("mana_dust_block", tier=tiers["petrothite"], recipe=Recipe81("<contenttweaker:mana_dust_block>", "<contenttweaker:mana_dust>")),
    Block("manalite_block", tier=tiers["manalite"], recipe=Recipe81("<contenttweaker:manalite_block>", "<contenttweaker:manalite_ingot>")),
    Block("manalite_forge_bricks", tier=tiers["manalite"], recipe=Recipe81("<contenttweaker:manalite_forge_bricks>", "<contenttweaker:manalite_forge_brick>")),
    Block("manalite_forge_controller", tier=tiers["manalite"], recipe=RecipeSurrounding("<contenttweaker:manalite_forge_controller>", "<contenttweaker:manalite_forge_bricks>", "<contenttweaker:manalite_block>")),
    Block("manalite_forge", tier=tiers["manalite"], recipe=RecipeSurrounding("<contenttweaker:manalite_forge>", "<contenttweaker:manalite_forge_bricks>", "<contenttweaker:manalite_forge_controller>")),
    Block("altarus_refinery", tier=tiers["altarus"], recipe=Recipe2xSurrounding("<contenttweaker:altarus_refinery>", "<contenttweaker:altarus_block>", "<contenttweaker:reinforced_steel_refinery>", "<contenttweaker:altarus_forge>")),
    Block("tartarite_refinery", tier=tiers["tartarite"], recipe=Recipe2xSurrounding("<contenttweaker:tartarite_refinery>", "<contenttweaker:tartarite_block>", "<contenttweaker:altarus_refinery>", "<contenttweaker:tartarite_forge>")),
    Block("petrothite_refinery", tier=tiers["petrothite"], recipe=Recipe2xSurrounding("<contenttweaker:petrothite_refinery>", "<contenttweaker:petrothite_block>", "<contenttweaker:tartarite_refinery>", "<contenttweaker:petrothite_forge>")),
    Block("manalite_refinery", tier=tiers["manalite"], recipe=Recipe2xSurrounding("<contenttweaker:manalite_refinery>", "<contenttweaker:manalite_block>", "<contenttweaker:petrothite_refinery>", "<contenttweaker:manalite_forge>")),
    Block("mana_coke_block", tier=tiers["manalite"], recipe=Recipe81("<contenttweaker:mana_coke_block>", "<contenttweaker:mana_coke>")),
    Block("manalite_freezer", tier=tiers["manalite"], recipe=Recipe2xSurrounding("<contenttweaker:manalite_freezer>", "<contenttweaker:manalite_block>", "<contenttweaker:aerothite_freezer>", "<contenttweaker:rose_gold_ice>")),
    Block("green_ice", tier=tiers["manalite"], recipe=RecipeSurrounding("<contenttweaker:green_ice>", "<contenttweaker:manalite_freezer>", "<contenttweaker:rose_gold_ice>")),
    Block("manalite_metal_former", tier=tiers["manalite"], recipe=Recipe2xSurrounding("<contenttweaker:manalite_metal_former>", "<contenttweaker:manalite_freezer>", "<contenttweaker:aerothite_metal_former>", "<contenttweaker:green_ice>")),
    Block("angmallen_block", tier=tiers["angmallen"], recipe=Recipe81("<contenttweaker:angmallen_block>", "<contenttweaker:angmallen_ingot>")),
    Block("angmallen_toolmaker", tier=tiers["angmallen"], recipe=RecipeToolmaker("<contenttweaker:angmallen_toolmaker>", "<contenttweaker:angmallen_block>", "<minecraft:iron_pickaxe>", "<minecraft:iron_axe>", "<minecraft:iron_shovel>", "<minecraft:iron_hoe>", "<minecraft:iron_sword>")),
    Block("angmallen_armormaker", tier=tiers["angmallen"], recipe=RecipeArmormaker("<contenttweaker:angmallen_armormaker>", "<contenttweaker:angmallen_block>", "<minecraft:iron_helmet>", "<minecraft:iron_chestplate>", "<minecraft:iron_leggings>", "<minecraft:iron_boots>"))
]
