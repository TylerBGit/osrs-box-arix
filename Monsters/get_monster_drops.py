import json

from osrsbox import monsters_api


def loot_drops():
    monster_drop_list = list()
    for d in monster.drops:
        monster_drops = dict()
        monster_drops["id"] = d.id
        monster_drops["name"] = d.name
        monster_drops["quantity"] = d.quantity
        monster_drops["noted"] = d.noted
        monster_drops["rarity"] = d.rarity
        monster_drops["rolls"] = d.rolls
        monster_drop_list.append(monster_drops)

    monster_drop_dict["drops"] = monster_drop_list


if __name__ == "__main__":
    # Load the database
    all_db_monsters = monsters_api.load()

    # Setup output dictionary
    monsters_drops = list()

    for monster in all_db_monsters:
        monster_drop_dict = dict()

        monster_drop_dict["id"] = monster.id
        monster_drop_dict["name"] = monster.name
        loot_drops()
        monsters_drops.append(monster_drop_dict)

    # Export extracted data
    out_file_name = "drop_list_arix.json"
    with open(out_file_name, "w", newline="\n") as out_file:
        json.dump(monsters_drops, out_file, indent=4)
