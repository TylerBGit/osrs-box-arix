"""
Author:  Krizz
"""

import json

from osrsbox import items_api

if __name__ == "__main__":
    # Load the database
    all_db_items = items_api.load()

    # Setup output dictionary
    item_list = list()

    # Loop through all items in the database
    for item in all_db_items:
        stats_dict = dict()
        item_dict = dict()
        # Convert stats if item is equipable
        if item.equipable_by_player:
            offensive = [item.equipment.attack_stab,
                         item.equipment.attack_slash,
                         item.equipment.attack_crush,
                         item.equipment.attack_magic,
                         item.equipment.attack_ranged]
            defensive = [item.equipment.defence_stab,
                         item.equipment.defence_slash,
                         item.equipment.defence_crush,
                         item.equipment.defence_magic,
                         item.equipment.defence_ranged]
            other = [item.equipment.melee_strength,
                     item.equipment.ranged_strength,
                     item.equipment.magic_damage,
                     item.equipment.prayer]

            # Append extracted data to a dictionary
            stats_dict["offensive"] = offensive
            stats_dict["defensive"] = defensive
            stats_dict["other"] = other

            # Set properties for the item dictionary
            item_dict["id"] = item.id
            item_dict["name"] = item.name
            item_dict["equipable"] = item.equipable
            item_dict["stats"] = stats_dict
            item_dict["slot"] = item.equipment.slot
            item_dict["skill_reqs"] = item.equipment.requirements
            item_dict["stackable"] = item.stackable
            item_dict["stacked"] = item.stacked
            item_dict["tradeable"] = item.tradeable
            item_dict["tradeable_on_ge"] = item.tradeable_on_ge
            item_dict["lowalc"] = item.lowalch
            item_dict["highalch"] = item.highalch

        # Elif the item is not equipable
        elif not item.equipable_by_player:
            # Set properties for the item dictionary
            item_dict["id"] = item.id
            item_dict["name"] = item.name
            item_dict["equipable"] = item.equipable
            item_dict["members"] = item.members
            item_dict["stackable"] = item.stackable
            item_dict["stacked"] = item.stacked
            item_dict["tradeable"] = item.tradeable
            item_dict["tradeable_on_ge"] = item.tradeable_on_ge
            item_dict["lowalc"] = item.lowalch
            item_dict["highalch"] = item.highalch

        # Add item data to list
        item_list.append(item_dict)

    # Export extracted data
    out_file_name = "item_list_arix.json"
    with open(out_file_name, "w", newline="\n") as out_file:
        json.dump(item_list, out_file, indent=4)
