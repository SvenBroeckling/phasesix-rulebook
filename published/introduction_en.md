Welcome to *{{ world_book.book_title }}*!

*{{ world_book.book_title }}* is a complete role-playing game. The rules and all associated materials are sufficient to play adventures in the world of {{ world_book.book_title }}. You can use these rules freely, and adventure with friends.{% if world_book.identifier != "tirakan" %} Alternatively you can create your very own world based on the eras and settings within the system.{% endif %}

The *{{ world_book.book_title }}* system is available for download as a PDF and can be played without a digital device. However, the focus of the system is to be played over an internet platform such as Discord, Teamspeak or similar. The associated platform [{{ world_book.book_website }}]({{ world_book.book_website }}) offers all kinds of tools for managing characters and campaigns. In addition you can roll any check directly on your character page and  optionally display the results in your Discord chat.

### What is a role-playing game?

In this case we are, of course, talking about pen and paper role-playing games, not computer games. Traditionally, a role-playing game is played with 2-4 *players* and a *game master*, with players using character sheets and dice to play. 

The role-playing game always tells a story that is carried and spun on by all the players. The players create characters for a game session or campaign. The character sheet contains the description of the character, his or her origins, interests and abilities. The latter are recorded in numerical values, because action in the role-playing game requires so-called *checks* or *rolls*, which determine the outcome of an action. For example:

{% if world_book.identifier == "tirakan" %}
> Tom has decided to join a role-playing group with Julia, the game leader. Julia has chosen an adventure in the Kingdom of Asgoran in the year 322.
>
> So Tom decides to create his character *Jamie*, a noble knight from Thenon. He chooses the character templates "Knight" and "Aristocratic", and the lineage template "Asgoran". He adds up all the values of the templates and records them on his character sheet.
>
> Due to the chosen background, Jamie has particularly high initial values in skills such as *Hand to hand combat*, *Endurance* and *Deftness*. However, in *Nature* or *Performance* his skills are rudimentary at best.

{% else %}
> Tom has decided to join a role-playing group with Julia, the game leader. Julia has chosen an adventure on Earth in the year 1982. Since the story is supposed to be in the style of a retro-science fiction mystery, Julia has chosen the era "The Cold War and the 80s" as well as the "Horror Extension".
> 
> So Tom decides to create his character *Jamie*, a journalist with a high school degree. He chooses the character templates "Journalist" and " High School". He adds up all the values of the templates and records them on his character sheet.
> 
> Due to the chosen background, Jamie has particularly high initial values in skills such as *Investigation*, *Communication* and *Politics*. However, in *Shooting* or *Acrobatics* his skills are rudimentary at best.

{% endif %}

For more information on creating a character, see the chapters [[chapter-create|Create a character]] and [[chapter-rolls|Rolls and Checks]].

While each player creates a character for the game, the *game master* prepares a story. This is often called an *adventure*, *plot* or *campaign*. This story is not, as like a novel, written out to the last detail. Instead, it is a rough script consisting of a general setting, possible courses of events, the description of places and locations, as well as so-called *non-player characters* (NPC).

Once the game starts, everyone player acts in the role of their character. The game leader describes situations to the best of their ability and occasionally shows maps or drawings. The players speak for their characters in the first person ("I sneak up the stairs."). If the characters' actions have an uncertain outcome, checks are used and dice are rolled.

> After preparing, the group around game leader Julia meets on a Discord video chat.  They choose [Owlbear Rodeo](https://www.owlbear.rodeo/) as the platform for a virtual game table to represent their characters there as figures with markers. (There are many more online platforms, do a search ;) ) 
> 
> At the start of the session, Julia sets the scene.
>
{% if world_book.identifier == "tirakan" %}
> Julia: "It is the 2nd of Fogmoon 322. You are in a tavern in the tranquil town of Lindfield in the south of Asgoran. It is late in the evening, and outside a light drizzle has caused the blanket of snow from the last few days to be covered in a thin layer of ice. It's going to be cold tonight, and slippery. The tavern is well filled. With a creak, the front door opens and a cloud of fine rain enters the pub. Immediately followed by a figure in a far too tight tar rain jacket."
{% else %}
> Julia: "It is the 2nd of January 1982. You are in a pub in the tranquil town of Lindfield in the south of England. It is late in the evening, and outside a light drizzle has caused the blanket of snow from the last few days to be covered in a thin layer of ice. It's going to be cold tonight, and slippery. The pub is well filled, and you hear the song Tainted Love from a jukebox as you wait for another pint. With a creak, the front door opens and a cloud of fine rain enters the pub. Immediately followed by a figure in a far too tight plastic yellow rain jacket."
{% endif %}
> 
> This is the prelude, and Tom decides that his character *Jamie* would like to have a look at the newcomer. He announces the actions for Jamie:
> 
> Tom: "I'm going to have a very close look at the stranger, I've already noticed this ill-fitting jacket."
> 
> Julia: "You notice that wet, black hair is falling from under the hood into the face of an old man. Why don't you do a *perception* check, to see what else is going on?"

So you see, the whole game is about a cooperative development of the story through the actions of the characters. The game leader has a plan of how the story could develop, which characters could appear and what their motivations actually are. Something is happening around the players' characters, and they are drawn into this action.

Where this story leads is uncertain. It may be that something bad is about to happen, or that a secret is uncovered. The game leader has a rough plan, but the players determine the progress.

#### Design note: It's all about storytelling

If you think of computer role-playing games, the strategic development of the character is the most important point. He must be able to survive future battles and have the best possible stats for possible challenges.

In pen and paper role-playing games, it is about the progress of the story, about shared experiences and memories. The best possible focus on "strong" characteristics (so-called *power gaming*) should not be in the foreground here. Because the story is always carried forward together, there are very flexible solutions for all challenges.

**A though on power gaming**: The {{ world_book.book_title }} rulebook deliberately does not prevent the possibility of pushing a relevant value (e.g. *shooting*) to astronomical heights. There should be agreement in the game group on what style of play you want to have. The rules deliberately allow these constructions in order giveyou  freedom in the creation of characters and adventures.

Also, the old role-playing rule comes into play here:  "**The word of the game master always weighs more than the rules**. Of course, it should normally be the case that the rules are applied as written, because it is the framework for the players to rely on. However, if there is an unclear rule, situation or case, the ruling of the game master decides the outcome.


#### Combat in the role-playing game

Even if the focus in pen and paper role-playing lies less on armed confrontation, combat still plays an important role. Not every situation can be resolved peacefully. A fight can quickly break out or maybe the characters plan to rob a trader.

Combat in role-playing is treated differently from free play. Time is compressed into combat rounds, and you usually visualise the situation with a map on the (virtual) table. Players take turns, the game leader controls the NPCs. Wounds, or hit points, indicate how well the characters are still doing. You can find more details on the course of the battle in the chapter [[chapter-combat|Combat]].

In the game, free play and combat should be balanced. There may be adventures that consist of only one (epic) battle, but {{ world_book.book_title }} is not a realistic battle simulation. The aim is to carry out a conflict in the most entertaining, cinematic and or exciting way possible.

When fighting in the *{{ world_book.book_title }}* system, however, the following things should always be followed due to the special features (reactions, stealing actions, etc.):

* Always use a map. A basic map of the situation ensures that there are no misunderstandings in positioning, no matter how short the fight is. A map can be a pre-made, elaborate map, but  a quickly drawn floor plan works just as well. When playing online, visual aid systems such as [Roll20](https://roll20.net/), [Owlbear Rodeo](https://www.owlbear.rodeo/) or [FoundryVTT](https://foundryvtt.com/) are useful.
* Always use a scale. Characters have different movement ranges. To keep track of advantages and drawbacks make sure not to mix metric and imperial systems. 
* Use an initiative tracker. Initiative determines the turn order in combat and visualizes it tranparent for all players . In {{ world_book.book_title }}, it is important for the players to know when it is their turn again (not just because they lose their unsused actions).

### Characteristics of {{ world_book.book_title }}

{{ world_book.book_title }} has different approaches compared to other role-playing systems. In part, these were designed to achieve flexibility in the scenarios possible. The system puts a lot of focus on being easily accessible while allowing the player to perform heroic actions in combat.

Standard six-sided dice are used for rolls and checks. Dice are rolled in the number of the respective value. Rolling a 5 or higher means *success*. Usually, a single success enough to pass a check.

#### Character templates

*{{ world_book.book_title }}* is not just a numbers game. Characters are not created or enhanced by allocating points to skills, attributes or other stats. Instead, *character templates* are used. Each one represents a small stage in the character's life.

These templates are subdivided into the life aspects: *lineage*, *occupation*, *education*, *character*, *talent* and *environment*. While the templates in the first two categories carry many traits (i.e. a healer is conscientiousness, and has first aid and medicine skills), a template from the talent section can be, for example, "Good Speaker", which only buffs the *communication* skill.

Character templates "bought" with *reputation* points, which are similar to experience points that characters receive for completing adventures. 

#### Special actions in combat

The combat is designed to make the action as impressive as possible, but the mechanics are kept simple.

The usual turn order of players applies, but the process is a little more fluid. Players are able to use *Reactions*, that are built into the combat system. Every player can safe one or more actions in their turn until the next round of combat. These can be used to *react* other players or NPC actions in their respective turns turns. An example:

Additionally, it is possible to spontaneously create your own actions in combat by spending *bonus dice*, which are obtained through templates. Or the player can even steal an action from opponents by spending a *destiny die*. Although destiny dice are very rare, it may be possible to steal the enemies fatal blow and turn it into the players own action.

This may sound somewhat unrealistic, but it gives the battle very dynamic options and can often lead to epic cinematic situations that even the game master cannot foresee.

#### Weapons

Weapons are designed to be upgradeable in {{ world_book.book_title }}. There is a list of weapon modifications. Different ammunition is also represented as a weapon modification.

{% if world_book.identifier != 'tirakan' %}
For example: the *horror expansion* includes silver ammunition, which certainly works better against werewolves than the usual lead. Still, the modification makes sense in the Middle Ages for usage with bows. It's the modular nature of *{{ world_book.book_title }}* that makes it a toolkit for any scenario you can imagine.
{% endif %}

You can find more information about the combat rules and weapon modifications in the chapter [[chapter-combat|Combat]].

{% if world_book.identifier != 'tirakan' %}
#### Eras and extensions

{{ world_book.book_title }} is designed to be as flexible as possible. It can be used for many scenarios, whether it's fantasy, science fiction, horror or stories in the "real" world. 

It offers a basic set of ready-made weapons, character templates, items and armour, which are divided into earthly eras. In addition, it is of course possible for a game group to create and use its own content.

To ensure that every scenario is possible, {{ world_book.book_title }} distinguishes between three types of extensions.

##### The basic rules

Some elements are always and everywhere valid. They apply regardless of which era or extension is chosen. Many character templates such as "Conscientious", "Gun nut", "Tattletale", but also weapons and items are always available regardless of era or extension.

##### Era or Age

Eras or ages are earthly time periods that are the template for all scenarios (including fantasy). They provide a technological level for weapons and items and determine what is available to players. Earthly history is divided into 8 ages.

* **Classical Antiquity** - 800 BC-600 AD.
* **Medieval Ages, Vikings and Crusades** - 500-1500
* **Victorian Age and the Wild West** - 1700-1900
* **Imperialism and World Wars** - 1900-1950
* **Cold War and the 80s** - 1950-1990
* **Modern Times** - 1990 and beyond
* **Near Future** - a dystopian near future
* **Science Fiction** - a distant future

The content of the era is based on the earthly technology of the time. An adventure always takes place in one of the eras.

In addition, the contents of the eras are kept as free as possible from specifically earthly elements so that they can also be used in a fantasy world of their own. Of course, the Modern Era, has well-known modern weapons, and the two-handed sword is also an earthly invention. However, it is kept as generic as possible so that it also fits into a scenario that is not set on Earth.

##### Extensions

In addition to the eras, certain extensions can be chosen to add magic or the workings of gods to an adventure, for example. These extensions can be chosen at will by the game master and are optional.

* **Magic** - adds the magic resource "Arcana" for the characters and brings spells and artifacts.
* **Horror** - defines rules for dealing with horror elements, stress and quirks.
* **Pantheon** - provides rules for interacting with gods: invocations, prayers and grace.
* **Body modifications** - provides a catalog of biomechanical elements that can be integrated into the body according to specific rules.
* **Vehicles and Drones** - provides special rules for vehicles, vehicle combat, and vehicle attachments.

#### Worlds

By combining eras and extensions, any scenario can be created. A Cthulhu story in the Wild West is just as possible as a magical world in the modern age. A classic fantasy world of your own creation could make use of the Middle Ages era and the "magic" extension.

Some existing worlds combine this combination of eras and extensions, and also give you the description of an entire world. They are available as a complete template and can be used directly.

###### Realms of Tirakan

The world of Tirakan is a complete fantasy world that can be played at any time in a 1000-year history. An elaborate story of humans, elves, gnomes and many other peoples tells the struggle of civilisations against minotaurs, lizards and a nameless darkness.

* **Era**: Middle Ages
* **Extensions**: Magic, Pantheon
* **World Description**: [tirakans-reiche.de](https://tirakans-reiche.de)

###### The Adventures of Division V of the NEXUS

The story of Department V of the NEXUS is set in the modern era. It is a fictional secret organisation founded to protect humanity from alien and paranormal threats. Players play agents of Department V of the NEXUS, and through the ability to time travel, experience adventures in all sorts of eras and worlds.

* **Era**: Modern
* **Extensions**: Horror, Body Modifications, Vehicles and Drones
* **World Description**: [phasesix.org](https://phasesix.org/world/nexus)
{% endif %}
