import json
from litemapy import Schematic
from collections import Counter

# Configuration file
with open("config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

# You can replace originrealms.json with your own blocks list.
with open("originrealms.json", "r", encoding="utf-8") as f:
    customNames = json.load(f)

# Blocks used in Origin Realms to make custom blocks and entities.
keepProps = set(config.get("keepProps", []))

# Some custom blocks have 2 halves (upper/lower). Counting both of them will return wrong count.
# Some 2-high blocks have tripwire (all values false) as base, that also can be ignored.
ignoreKeys = set(config.get("ignoreKeys", []))

# Vanilla blocks that have upper/lower half, they need to be divided by two, otherwise it returns 2x block amount.
doubleBlocks = set(config.get("doubleBlocks", []))

schem = Schematic.load("./schematics/schem.litematic")

blockCounter = Counter()
for region in schem.regions.values():
    for x, y, z in region.block_positions():
        block = region[x, y, z]
        fullId = block.to_block_state_identifier()
        baseId = block.id

        key = fullId if baseId in keepProps else baseId

        if key.startswith("minecraft:"):
            key = key[len("minecraft:"):]

        if key in ignoreKeys:
            continue

        displayName = customNames.get(key, key)
        blockCounter[displayName] += 1

for key in list(blockCounter.keys()):
    baseName = key.split("[")[0]
    if baseName in doubleBlocks:
        blockCounter[key] = blockCounter[key] // 2

sortedData = dict(sorted(blockCounter.items(), key=lambda item: item[1], reverse=True))

with open("blockCounts.json", "w", encoding="utf-8") as f:
    json.dump(sortedData, f, indent=4, ensure_ascii=False)

print("Data written to blockCounts.json")
