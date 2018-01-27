# Random Encounters

[![Build Status](https://travis-ci.org/Kreonn/RandomEncounters.svg?branch=master)](https://travis-ci.org/Kreonn/RandomEncounters)[![Coverage Status](https://coveralls.io/repos/github/Kreonn/RandomEncounters/badge.svg?branch=master)](https://coveralls.io/github/Kreonn/RandomEncounters?branch=master)

## Goal of the project

This project started on January, 12th 2018. Its primary goal is entertainment, so please don't expect anything serious ;p

Here is the pitch:

Have you ever thought, while playing Final Fantasy or Dragon Quest, "am I the only person in the whole world who fight monsters?"? 
Well, in Random Encounters, you will play as a regular person in a fantasy world who decides, one day, to pick up their knife and fight monsters. 
Will you become the most fearsome warrior in the world? Will you just clean your village whereabouts? Will you be beaten by the first slime to come? It's your tale!

## Design ideas - Core

Basic functionalities for the game to be considered "playable". Nothing too fancy around here.

### Creating a character

At the start of the game, we create a new character.

What the player can choose:
- Name
- Gender (does not affect gameplay)
- ...

What the player cannot choose:
- Stats (generic, balanced stats for all starting characters)
- Starting equipment (basic set)
- ...

### Generating random encounters

- Generate unique monsters (name, stats, ...)

### Battle system 
- Turn-based RPG battle

### Gear up

- "Village" menu: central hub where the player can:
    - upgrade their equipment 
    - begin next combat
    - ...
- Equipment system:
    - Head
    - Armor
    - Weapon

## Design ideas - Next steps

Once the core game is complete, its basic concept may be enhanced, preferably in the following order.

### Save system

Not in the core system, but really important for a game, right?

### Character evolution

The character should be able to level up.
Player should be able to spend points

### Enhanced equipments

- Multiple slots of equipment
    - Head
    - Neck (Accessory)
    - Shoulders
    - Chest
    - Back (Cloaks, Bags...)
    - Wrists
    - Hands
    - Left Ring (Accessory)
    - Right Ring (Accessory)
    - Waist
    - Legs
    - Feet
    - Right Hand (Weapons, Shields)
    - Left Hand (Weapons, Shields)
- Generating pieces of equipment

### Generating monsters background

### Generating locations

- Travel system

### Enhanced character evolution

- Mutations
- Religious beliefs
- ...

### Generating skills

### Generating world lore