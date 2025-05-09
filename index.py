import json
from litemapy import Schematic
from collections import Counter

# You can replace originrealms.json with your own blocks list.
with open("originrealms.json", "r", encoding="utf-8") as f:
    customNames = json.load(f)

# Blocks used in Origin Realms to make custom blocks and entities.
keepProps = {
    "minecraft:note_block",
    "minecraft:tripwire",
    "minecraft:sugar_cane",
    "minecraft:cave_vines",
    "minecraft:twisting_vines",
    "minecraft:small_dripleaf",
    "minecraft:barrier",
    "minecraft:oak_leaves",
    "minecraft:azalea_leaves"
}

schem = Schematic.load("./schematics/test.litematic")

blockCounter = Counter()

for region in schem.regions.values():
    for x, y, z in region.block_positions():
        block = region[x, y, z]
        fullId = block.to_block_state_identifier()
        baseId = block.id

        key = fullId if baseId in keepProps else baseId

        if key.startswith("minecraft:"):
            key = key[len("minecraft:"):]

        displayName = customNames.get(key, key)

        blockCounter[displayName] += 1

# Vanilla blocks that are two high, they need to be divided by two, otherwise it returns wrong count.
doubleBlocks = {
    "lilac",
    "rose_bush",
    "sunflower",
    "peony",
    "spruce_door",
    "oak_door",
    "birch_door",
    "jungle_door",
    "dark_oak_door",
    "acacia_door",
    "mangrove_door",
    "cherry_door",
    "bamboo_door"
}

for key in list(blockCounter.keys()):
    baseName = key.split("[")[0]
    if baseName in doubleBlocks:
        blockCounter[key] = blockCounter[key] // 2


sortedData = dict(sorted(blockCounter.items(), key=lambda item: item[1], reverse=True))

with open("blockCounts.json", "w", encoding="utf-8") as f:
    json.dump(sortedData, f, indent=4, ensure_ascii=False)

print("Data written to blockCounts.json")
