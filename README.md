# schemreader
Reads .litematica file and lists materials needed with support for custom blocks.
Made for Minecraft Java server Origin Realms. Use for whatever you need it.

Requires Python library `litemapy`.



Provided as-is, without waranties.

<h1 align="center">🧱 schemreader</h1>
<p align="center">Custom Block Reader from .litematica</p>

## 📝 Description
schemreader - Simple, easy to use `Minecraft: Java Edition` schematic reader, that outputs all the necessary blocks.
Works with custom blocks used in servers.\
**Only .litematica files are supported**

* Currently supports only `Origin Realms` server. It has 400+ custom blocks.

## 🔧 Setup & Usage
schemreader is easy to setup and run, but to run it, you need `Python`.

For first time setup:
```sh
pip install litemapy
```

To run `schemreader`, rename your schematic to `schem.litmatic` and place it in the schematics folder.
Then just run `python index.js`

The blocks needed with amounts will be outputed to `blockCounts.json`

## 📰 Known Issues
* Origin Realms:
  * Pebbles/Rocks return incorrect amount on variants 2 & 3.
  * Ruby Deposit / Decorated Pot cannot be counted.
  * Channeling Rod uses chain model, impossible to count.
  * Display Plaque cannot be counted.
