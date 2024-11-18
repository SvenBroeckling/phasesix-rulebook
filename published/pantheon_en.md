{% if world.identifier == "tirakan" %}
The deity world of Tirakan is diverse and difficult for amateurs to keep track of. All cultures of the world have their own deities, which are more or less present. In general, gods on Tirakan are very approachable, many can be invoked directly. The peoples of Tirakan pray for certain weather, for personal luck, for success in battle, or for fellow humans.

These rules reflect the closeness of the peoples to the world of the gods.
{% else %}
This expansion brings the work of gods into your campaign. Characters are able to invoke Divine action and have a **attitude** and **grace** with their deity. There are various forms of invocation which can be performed by a believer.

The rulebook deliberately refrains from using earthly gods or beliefs here, but there are no limits to the imagination. For a cultist, for example, a being from the Cthulhu mythos can also be a deity.
{% endif %}

### Level of faith

{% if world.identifier == "tirakan" %}
Similar to magic, Tirakan's faith evolves over the centuries. While the churches pray for a long time in silent waiting for the return of the gods' work, the influence of the gods develops into a very strong, direct influence by the end of the age. This is represented by the **faith level**, which behaves similarly to the **magic level** and changes over the centuries.

* 1st century: Faith level 1
* 2nd century: Faith level 1
* 3rd century: Faith level 1
* 4th century: Faith level 1
* 5th century: Faith level 1
* 6th century: Faith level 2
* 7th century: Faith level 3
* 8th century: Faith level 4
* 9th century: Faith level 5
* 10th century: Faith level 6
{% else %}
The power of divine activity depends on the *level of faith*. This is a global value that illustrates the strength of divine activity. In general, it is assumed that the world has a faith level of **3**.

However, particular places can change the level of faith. For example, invocations may be stronger in a large cathedral. Areas may perhaps be subject to a curse, or otherwise have a lower faith level. The faith level, if it differs from 3, is set by the game master.
{% endif %}

### Favor

As a value, favor represents the relationship between services of the priest and favors of the god. The value is 0 at the beginning and can become negative or positive.

The cost of the favors is subtracted from the favor. Favor points can be gained by the priest through godly actions in the game. It depends very much on the type of deity, with which the priest can rise in the deity's favor.

### Relics

Relics have a special role in the churches of Tirakan. They strengthen the bond with the god and help the believer to continue on his path.

Common relics are objects from the possession of saints, but also bones of them. But even a simple object related to the deity can be a low level relic, such as a special stone for Tador. The character can get to a relic in many different ways, but it always requires a consecration.

Relics always have a level, which can range from 1 to 6. A level 1 relic can be an object that a saint once touched, for example. A level 6 relic can be a holy weapon or the bones of a saint.

### The forms of invocation

There are four forms of invocation to a god. Each of them is performed differently. Each has a different effort and requests a different favor from the deity.

Common to all forms of invocation is the influence of the environment, the priest's condition, as well as faith level of the world. Thus, the following modifications are added to the **minimum roll** of each invocation (there are invocations that require multiple rolls).

* Favor of the priest: **-(favor/2)**
* The intention of the character does not correspond to the virtues of the deity: **+10**
* Ceremonial design (candles, clean cloths, etc.) not present: **+5**
* The attitude of the priest is contrary to the deity: **+15**
* The request is not the first request of the day: **+2**
* Sacrifice is offered: **-3**
* The priest uses incense: **-2**
* The invocation is done on Doldag: **-2**
* The invocation is chanted (additional chanting rehearsal): **-5**
* The prevailing level of faith: **-faith level**
* Additional priests at the invocation: **-Number**
* Relic present: **-Level**

#### Shock prayer

The least form of request is the Shock Prayer. In a short, pleading invocation of 3 seconds, the priest can gain a bonus to one of his attributes or skills. The bonus is equal to **faith level** points and lasts for **faith level** minutes.

A Shock Prayer requires a single **Charm** roll.

The Shock Prayer costs the priest 2 favor points.

#### Blessing

A blessing is able to break a divine curse (the work of a dark god, as indicated by the work in each case), but can also be transferred to an object to create a blessed weapon, holy water, or the like. To cast the blessing takes 5 minutes, and it lasts indefinitely.

A Blessing requires a Willpower and a Charm check.

The blessing costs the priest 5 favor points.

#### Lesser request

The Lesser Request invokes direct divine action. In it, the abilities of the character's deity and all of its servants that are classified as "minor" can be requested. The prayer for the low petition takes about 15 minutes. It can also be done as part of a ceremonial service.

A charm roll is required for the minor supplication.

#### Invocation

The invocation requests a deity's work that is classified as "higher". Again, both the deity of the character and its servants may be invoked. The invocation requires a larger ceremony and lasts at least 30 minutes. It can also be done as part of a ceremonial service.

The invocation requires 2 charm rolls and a willpower roll.

> A word about the gods' work. The work of the gods is sometimes described with concrete rules. However, most descriptions remain rather vague. This is to reflect the fact that the nature and workds of the gods are their own business. GMs and players should be open to spontaneous developments when a god or demon intervenes in world events.

#### Consecration

With the consecration, an item such as a weapon is given to a god. The divine power ensures that the item is improved (stats plus about 30-50%), however there is also a chance that the item will be ensouled after the consecration and have some life of its own.

A consecration is a two-hour ceremony during which the deity is invoked three times by means of a charm roll. In addition, a test of strength is required as the item is held for the entire period. Finally, a 50% chance of ensoulment is thrown.

The consecration costs the priest 7 favor points.

#### Silent prayer

Once per day, the priest may spend one hour in silent devotion to his deity. For this, he rolls a **charm** roll and adds one favor point for each success.

#### Ceremonial Service

Ceremonial service is a service to the deity to strengthen their work and spread their word. The service can be both a classical ceremony in memory of the deity and something like a ritual funeral or exorcism. Minor petitions or invocations may be made as part of the ceremonial service, but they do not have to be.

A ceremonial service earns the priest one favor point for each participant, up to the double **faith level** per service. If a petition or invocation is performed, this cost is deducted again.
