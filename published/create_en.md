To create a character, you select character templates that reflect their life stages, talents and interests (see [[appendix-templates|Appendix Character Templates]]). Each template can alter the character's attributes and skills, as well as bringing knowledge and shadows. Additionally, character templates can unlock game mechanics, such as performing the actions of a priest or learning magic spells.

### Career points:

Career points are used to add character templates. Each template costs a certain number of career points.

New characters usually start with **20** career points. However, the game master can set this number arbitrarily.

Character templates can have negative point costs. In this case, the player receives the points when they select the template. This applies to the *Drunkard* template, for example.

{% if world_book.identifier != "tirakan" %}
### Eras

Before the campaign or adventure begins, the game master decides which era and extensions to use. This determines which character templates, weapons, armour and items can be used, as well as whether magic, body modifications or priests' actions are possible.

The possible eras are:

* Classical antiquity
* The Middle Ages, Vikings and Crusades
* The Victorian era and the Wild West
* Imperialism and World Wars
* The Cold War and the 1980s
* Modern times
* Near future
* Science fiction

Optional extensions include:

* Magic
* Horror
* Pantheon
* Body modifications
* Vehicles and drones

{% endif %}

Selecting templates:

A character template represents a specific stage in a character's life. Each template is assigned to one of the following categories: education, occupation, talent, interests, character or environment.

Each template alters a small number of the character's attributes and skills, either positively or negatively, and may bring with it knowledge or shadows. Additionally, templates may contain their own rules, which the character then adopts.

Each template is worth a certain number of career points. This is the number of points that must be spent to incorporate the template into the character's career.

#### Base values

All of a character's attributes, skills and other values start with a uniform base value. Information from the character templates is then added to these values.

* Actions: 2
* Minimum roll: 5+
* Bonus, destiny, and re-rolls: 0
* Persona and physical attributes: 1
* Skills: 0
* Innate protection: 0
* Maximum hit points: 10
* Arcana: 0
* Spell Points: 0
{% if world_book.identifier != “tirakan” %}* Maximum Stress: 8
* Biostrain: 0{% endif %}

#### Lineage

First, select the lineage template that best describes your character's origin. Different lineages offer different bonuses. You can only select one lineage template, and it does not cost any career points.

The available templates are listed in the [[appendix-templates|Appendix Character Templates]].

The chosen lineage is noted in the career and the specified modifications are added to the character's values.

#### Additional templates

You can now select as many additional templates as you wish until you have used up all your career points. You can combine templates from all categories. This means that your character can have one or more occupations, or none at all.

The modifications specified for each template are added to the character's values. In addition, the knowledge, shadows and other rules of the template are added to the character sheet.

All values can also become negative (see [[chapter-rolls|Rolls and Checks]]).

#### Remaining career points

Once the player is satisfied with the template, they can declare the character finished. Any remaining career points that have not been spent will be added to the character's reputation (see [[chapter-advancement|Advancement]]). This means that no points are lost.

### Contacts and languages

Once the character templates have been finalised, the character's languages and contacts can be determined.

#### Contacts

Contacts are acquaintances or connections that the character had before the start of the campaign. They are recorded with their names and descriptions, and can be imagined as desired.

The number of contacts a new character can have is determined by the sum of the attributes *Charm* and *Attractiveness*.

Contacts are recorded on the character sheet.

#### Languages

A new character can learn a certain number of languages based on the sum of their *Education* and *Logic* attributes. These can be any languages. If the sum of these attributes is 0 or less, the character has only a limited command of their native language.

Languages are recorded on the character sheet.

### Equipment

Once the character's stats have been determined using the templates, the character can be equipped with gear. The game master sets a starting capital for the characters for the campaign or adventure.

{% if world_book.identifier == "tirakan" %}
The starting capital is usually 2,000 Gulden.
{% else %}
The starting capital is usually 2,000 units of the standard currency, for example, euros.
{% endif %}

This starting capital can be used to purchase equipment such as weapons, armor, and items. For more details, see the [[chapter-gear|equipment]] chapter.

#### Equipment

[[appendix-weapons|Weapons]], [[appendix-riot_gear|Armor]] and [[appendix-items|Items]] can now be purchased with your starting capital. Any purchased items can be noted on the character sheet with their values, and the price can be deducted from your starting capital.

{% comment %}
#### Vehicles and Drones
{% endcomment %}

#### Assets

Any starting capital not spent on weapons, armor, and similar items becomes the character's assets.

### Spells

{% if world_book.identifier != "tirakan" %}
If the magic extension is used in the adventure or campaign, the character can also learn spells.
{% endif %}

Character templates offer *spell points* and allow the character to learn spells of a certain *origin*.

If the character has obtained both through the choice of character templates, they can use the spell points to choose spells that they have mastered.

Spells are acquired in a similar way to templates for points. Spell points are used for this purpose. Each spell has a specific cost for which it can be added to the character sheet (see [[appendix-spells|Appendix Spells]]). Only spells of origins that the character has unlocked through character templates can be selected. More details can be found in the chapter [[chapter-magic|Magic]].

{% if world_book.identifier != "tirakan" %}
### Body Modifications

When playing with the *Body Modifications* extension, [[appendix-body_modifications|body modifications]] can be purchased and installed for the starting capital.

The [[chapter-body_modifications|rules]] for body modifications must be taken into account here; for example, sufficient energy must be available for the consumers.

The process of integration by a doctor is not necessary when creating a character; body modifications can simply be noted on the character sheet.
{% endif %}

