An essential part of the adventurer's life is the equipment. For a new character, the starting capital can be used to buy equipment. This section describes the different types of equipment, their characteristics and their values.

## Items

The simplest form of equipment are items. These can be anything that the character accumulates in their life. Tents, torches and bandages are equipment items. Animals and carts also fall under equipment. If the character acquires or obtains an item, it is simply noted on the character sheet.

Items are sorted into the following categories:

* First aid
* Vehicles
* Containers
* Curiosities
* Lights
* Musical instruments
* Pet supplies
* Trekking equipment
* Potions
* Throwables
* Tools
* Ingredients
* Surveillance

### Properties

Items can have various properties relevant to the game. All items have the following properties:

* **Price**: this is the average purchase price of the item when it is acquired. This price is expressed in {% if world_book.identifier == "tirakan" %}Gulden{% else %}the main unit of the currency used{% endif %}.
* **Rarity**: Rarity describes how available the item is. It can be *common*, *uncommon*, *rare*, *legendary* or *unique*.
* **Weight**: the weight of the item. This is used to judge the carrying capacity of the character, although there is no rule for overloading here.
* **Concealment**: the concealment indicates how easy an item is to find if an observer is specifically looking for it. A higher value here represents an item that is easier to find.

{% if world_book.identifier != "tirakan" %}
An object is always assigned to one or more extensions. For example, there are items that are only available if the magic extension has been selected for the game.
{% endif %}

### Item rules

Some items have special rules that may also require a skill or attribute roll. These rules are listed with the item. For example, a bandage allows you to use your First Aid skill to heal a character.

### Charges

Items can contain charges. If this is the case, a charge is removed if it is used successfully.

{% if world_book.identifier != "tirakan" %}
For example, a professional emergency kit has 5 charges.
{% else %}
For example, a carafe of arcane potion has three charges.
{% endif %}

If all charges are used up, the item can no longer be used according to its purpose until it is possibly refilled.

## Weapons

Weapons are distinguished from everyday items, they have different game values and mechanics. Like items, weapons are recorded on the character sheet when they are purchased or obtained by other means.

Weapons are assigned to different types of weapons. In the game, only the difference between melee, ranged and throwing weapons is important, as the respective value (shooting, hand to hand combat, throwing) is rolled. There are the following types of weapons:

* Axes
* Blades
* Blunt Weapons
* Bows
* Polearms
* Slings
* Throwing Weapons
{% if world_book.identifier != "tirakan" %}* Assault Rifles
* Heavy weapons
* Machine guns
* Pistols
* Rifles
* Shotguns
* Submachine guns{% endif %}

{% if world_book.identifier != "tirakan" %}
Different types of weapons may be available in different eras. Grenades count as items, not as weapons.
{% endif %}

### Properties

Weapons have the following properties:

* **Price**: as with items, this is the price for which the weapon can be purchased on average.
* **Rarity**: Rarity describes how available the weapon is. It can be *common*, *uncommon*, *rare*, *legendary* or *unique*.
* **Weight**: as with items, the weight of the weapon is used to give a rough idea of how much the character can carry.
* **Concealment**: the concealment of the weapon indicates how easy it is to detect when searching for it. A higher value means easier recognition of the weapon.
* **Type**: the type of the weapon indicates to which weapon class the weapon belongs.
* **Damage potential**: this value is indicated by a number of dice. The dice represent the potential of the weapon to do more damage and are added to the skill value on attack rolls.
* **Piercing**: Reduces the target's protection by the number of protection units specified. For the protection to have effect, the target must expend more protection units than the piercing of the weapon.
* **Actions to ready**: Weapons can take a different amount of time to ready. It usually takes one action to change or pick up a weapon. However, there are also very fast weapons that can be switched to without delay, and also very complex weapons.
* **Range (metres)**: the range is given for all weapon types. For ranged and thrown weapons, it indicates the maximum range at which a target can be reasonably hit. Melee weapons with a range of more than one metre can be used at the indicated range, such as pole weapons.

Ranged weapons have the following additional properties:

* **Capacity** describes how much ammunition the weapon can hold at the same time, e.g. the magazine size in modern weapons.
* **Reload actions** indicates how many combat actions the character must invest to completely reload the weapon.
{% if world_book.identifier != "tirakan" %}* **Recoil compensation**: a recoil penalty is applied to a shot that is immediately followed by another shot in *the same* combat round. The recoil compensation is subtracted from this malus, so a weapon with high recoil compensation makes directly consecutive shots easier.{% endif %}

{% if world_book.identifier != "tirakan" %}
#### Attack modes

Weapons always have at least one attack mode. These are indicated in the weapon table with the weapons. If there is more than one attack mode, the character can select it each time the weapon is used without using an action to switch. The attack modes are (see [[chapter-combat|Combat]]):

* **Single shot**: can cause critical hits.
* **Burst mode**: gives two dice in addition to the hit roll, cannot cause critical hits.
* **Hand to Hand**: the weapon is used in close combat, can cause critical hits.

In additional extensions or worlds, there may also be other attack modes with special rules.
{% endif %}

### Rules

Weapons, like objects, can have special rules. These describe in detail what is to be observed when using the weapon.

In addition to formulated rules, there is also the specification of special caused conditions (see [[chapter-wounds|Wounds and Healing]]). As a rule, these are indicated with a value. This is the value that the hit adds to the corresponding condition **when the weapon causes wounds**. Possible conditions are:

* Bleeding X
* Poisoned X
* Shocked X
* Burning X

### Weapon modifications

In addition to weapons, there is a list of weapon modifications. These allow weapons to be modified.

{% if world_book.identifier != "tirakan" %}
In the modern era, for example, it is possible to attach a sight to a weapon. But special ammunition is also represented as a weapon modification, for example, the *Horror extension* brings silver ammunition.
{% endif %}

Weapon modifications are divided into the following categories:

* **Blade**: such as a hardened blade or a special engraving
* **Ammunition**: special types of ammunition, but also quivers
* **Grips**: leather-wrapped handles for swords and the like
{% if world_book.identifier != "tirakan" %}* **Barrel**: silencers for modern weapons
* **Sights**: Sights for modern weapons
* **Gadget**: lights, tripods and the like{% endif %}

Usually, these weapon modifications change one or more values of the weapon. However, they can also bring their own rules.

Characters can find or acquire already modified weapons in the game, but of course they can also commission a modification.

## Armour

Armour items, like weapons, are noted separately from normal items on the character sheet. Armour provides *protection* which can prevent wounds in combat. In addition to wearable armour, this list also includes shields that can provide cover for the character.

Armour is divided into categories:

* Clothing
* Light armour
* Medium armour
* Heavy armour
* Shield

### Properties

Armour items have the following game-relevant values:

* **Type**: the armour type, e.g. "Light Armour".
* **Price**: the average purchase price of the armour
* **Weight**: the weight of the armour
* **Concealment**: how hard is the armour to spot if an observer specifically looks for it?
* **Encumbrance**: Heavy armour hinders the character in physical actions. Encumbrance is subtracted from the character's evasion value.

#### Protection

Each piece of armour has a certain amount of protection units. These are shown as shields on the armour. These shields can be used in combat to prevent hits. There are the following types of armour:

* **Normal protection**: This protection can be used to prevent a normal hit.
* **Critical protection**: This protection can prevent a critical hit or a normal hit.
* **Sticky Protection**: Prevents a normal hit. The weapon gets stuck in the armour and must be released to perform an action.
* **Bleeding Protection**: Prevents a hit and an attack from causing the Bleeding condition.
* **Poison Protection**: Prevents you from being hit and an attack from causing Poisoned condition.
* **Fire Protection**: Prevents being hit and prevents an attack from causing the Burning condition.
* **Reflecting Protection**: Prevents a normal hit and causes the attacker to be hit.
* **Shock Protection**: Prevents being hit and prevents the attack from causing Shocked condition.

The protection of all armour pieces is combined into a protection pool that can be used in combat. For more details, see [[chapter-combat|Combat]].

## Currency

{% if world_book.identifier == "tirakan" %}
The standard currency is the *gulden*, and all items are priced in this unit. One gulden is equal to 100 *deut*. You can buy one golden *ounce* for 250 gulden, and one *ingot* for 4 ounces.
{% else %}
In different scenarios and worlds, there can be different currencies. Each character and campaign is assigned a currency table that specifies the different units of currency. Characters can record their wealth on the character sheet. Currency tables are e.g.

* Euro
* Dollar
* Taler
* Guilder (Realms of Tirakan)
* Yuan

Whether currency plays a role in the game is entirely up to the group and the game leader, it is optional.
{% endif %}
