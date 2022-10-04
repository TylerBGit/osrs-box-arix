import json

from osrsbox import monsters_api

if __name__ == "__main__":
    # Load the database
    all_db_monsters = monsters_api.load()

    # Setup output dictionary
    monsters_list = list()

    # Loop through all monsters in the database
    for monster in all_db_monsters:
        monster_dict = dict()
        monster_stats = dict()
        monster_drops = dict()
        # Convert stats if monster has stats
        if not monster.combat_level == 0:
            levels = [
                monster.attack_level,
                monster.strength_level,
                monster.defence_level,
                monster.magic_level,
                monster.ranged_level]
            bonuses = [
                monster.attack_bonus,
                monster.strength_bonus,
                monster.magic_bonus,
                monster.ranged_bonus,]
            attack = [
                monster.attack_magic,
                monster.attack_ranged]
            defence = [
                monster.defence_crush,
                monster.defence_slash,
                monster.defence_stab,
                monster.defence_magic,
                monster.defence_ranged]

            # Append extracted data to a dictionary
            monster_stats["levels"] = levels
            monster_stats["bonuses"] = bonuses
            monster_stats["attack"] = attack
            monster_stats["defence"] = defence

            # Set properties for the monster dictionary
            monster_dict["id"] = monster.id
            monster_dict["name"] = monster.name
            monster_dict["examine"] = monster.examine
            monster_dict["combat_level"] = monster.combat_level
            monster_dict["hitpoints"] = monster.hitpoints
            monster_dict["max_hit"] = monster.max_hit
            monster_dict["attack_type"] = monster.attack_type
            monster_dict["attack_speed"] = monster.attack_speed
            monster_dict["stats"] = monster_stats
            monster_dict["aggressive"] = monster.aggressive
            monster_dict["poisonous"] = monster.poisonous
            monster_dict["immune_poison"] = monster.immune_poison
            monster_dict["venomous"] = monster.venomous
            monster_dict["immune_venom"] = monster.immune_venom
            monster_dict["category"] = monster.category
            monster_dict["attributes"] = monster.attributes
            monster_dict["slayer_monster"] = monster.slayer_monster
            monster_dict["slayer_masters"] = monster.slayer_masters
            monster_dict["slayer_level"] = monster.slayer_level
            monster_dict["slayer_xp"] = monster.slayer_xp

            monster_dict["size"] = monster.size

        elif monster.combat_level == 0:
            monster_dict["id"] = monster.id
            monster_dict["name"] = monster.name
            monster_dict["examine"] = monster.examine
            monster_dict["combat_level"] = monster.combat_level

        monsters_list.append(monster_dict)

    out_file_name = "monster_list_arix.json"
    with open(out_file_name, "w", newline="\n") as out_file:
        json.dump(monsters_list, out_file, indent=4)

