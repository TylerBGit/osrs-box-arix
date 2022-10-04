import json

if __name__ == "__main__":
    with open('world_spawns_old.json') as world_spawns:
        data = json.load(world_spawns)

        for d in data:
            if 'colourReplacements' in d:
                d.pop('colourReplacements')
            if "chatHeadModels" in d:
                d.pop('chatHeadModels')
            if 'models' in d:
                d.pop('models')

        out_file_name = 'world_spawns_new.json'
        with open(out_file_name, "w", newline="\n") as out_file:
            json.dump(data, out_file, indent=4)
