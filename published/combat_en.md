When it comes to combat, the game progresses in rounds.

### Start of combat

As soon as a conflict arises, time is frozen, and the group determines the order in which the participants of the combat will act.

To do this, each participant rolls on a D6, and adds the *Quickness value*. The rule of *Exploding Dice* also applies here. The participant with the highest result starts the fight, all others follow in the order of their results.

If two participants have the same result, the *Quickness* value decides first, and if this is also identical, the *Deftness* value.

All participants of the combat have no actions available at the beginning of the combat. Their actions are refreshed the first time they receive the *priority*.

### Sequence of rounds

The combat is divided into *combat rounds*. In each combat round, each participant gets *priority* once, i.e. it is his turn and he can determine which *actions* he will perform.

The participant can perform an action for each of his available actions (see *Actor and Actions*), or save the action to react in the opponent's turn (see *Reactions*).

If the last participant has acted, the next *combat* round starts with the first participant.

#### Actor and actions

If it is a participant's turn, he has the *priority*, he is the *actor* at this moment.

At the beginning of the turn, the *actions* of the participant refresh. The number of the player's actions is taken from the player's lineage. Thus, a human has 2 actions available in combat. The actions per round can be expanded by templates.

"Refresh" therefore means that all actions are available again. If the participant has previously used up actions, for example by taking actions in the previous combat round, he resets his available actions to the maximum.

Once the actions are refreshed, the participant can act in combat. To do this, he performs actions one after another, each act taking a certain number of *actions*. Actions can be, among others, the following:

* To **attack** with a weapon
* Parry **with a weapon or object**.
* Reload a weapon
* **Use** an object
* Evade **a melee attack**.
* **Aim** with a melee weapon or when firing a single shot.
* **Hunker** or lay on the ground (The "Hunkered" status effect is active, see [[chapter-wounds-and-healing|Wounds and Healing]]).
* **Stand Up**
* **Walk** *Quickness* + 1 meter (while performing another action without consuming an action, but the minimum roll is increased by 1).
* **Run** *Quickness* + 5 meters
* **Rob** *Quickness* / 2 + 1 meters (rounded up), the character must be *Hunkered*. (see [[chapter-wounds-and-healing|Wounds and Healing]]: Conditions of the character)

Actions should not be performed together, but always one after the other, because of possible reactions.

#### Reactions

If an *actor* acts in combat, all participants who directly perceive the *actor* can react to this action.

To be able to react to an action, the following conditions must be met:

* The reacting participant must directly perceive the *actor*, i.e. hear, see, or otherwise become aware of his action.
* The reacting participant still has unused *actions*.

The reaction is executed immediately after the *actor's* action, but takes place practically simultaneously. There can only ever be one *reaction* by a participant to an *action*. However, any number of participants can react to the *actor* when they perceive its *action*.

Each *reaction* reduces the available *actions* of the reacting participant by one.

### Actions by bonus dice

Bonus and fate dice can be used in combat to gain or steal actions.

To gain an additional action, a *bonus die* can be subtracted. The additional action is available immediately, even for a reaction.

If a *destiny die* is spent, an action can be stolen from an opponent. This is no longer available to the opponent in his current (or next, if it is not his turn) turn. The participant who spent the fate die has the action immediately available, even as a reaction.

Spending dice for actions does not itself take an action.

### Sequence of an attack

Attacks with weapons are handled exactly the same in melee and ranged combat. The only difference is that attacks with melee weapons are thrown at the *Hand to Hand combat* skill, attacks with firearms are thrown at the *Shooting* skill, and attacks with throwing weapons are thrown at the *Throwing* skill.

An attack has the following phases:

* The **Hit Roll** determines how many hits a character achieves in an attack with a weapon. Here, the dice are rolled on the respective weapon skill, and a distinction is made between *critical hits* and *hits*.
*The **Cover roll** is available to the attacked character if he has cover. Here it is possible to avert damage even before the hits hit the armor. Shields can provide cover.
* Converting *hits* into *wounds* taking into account *protection*, *penetration* and *critical hits*.

#### The hit roll

To make an attack, a roll of a certain number of dice is made. The *minimum roll* of this roll is equal to the *minimum roll* of the character. Here, a possible *recoil penalty* must be taken into account if the character has already fired in the same combat round.

The number of dice is initially equal to the character's respective skill value (shooting, hand to hand combat, throwing) plus the *damage potential* of the weapon.

The hit roll can also be modified by other circumstances. Different firing modes and firing at the wrong distance may cause the available dice to change.

Each success causes a *hit* to the target of the attack. How the target can prevent damage is described under *Wounds and Pierce* and *Cover*.

##### Recoil

Modern weapons usually cause *recoil* when attacking, which makes it difficult to re-aim at a target in a directly following attack.

If an attack with a firearm is followed *directly* by another attack from the same character *within a combat round*, the minimum roll and the critical hit threshold are increased by 2. This malus increases for each subsequent attack in the same combat round. Thus, a third attack has a +4 malus on the minimum roll and critical hit threshold.

The recoil can be prevented if, for example, another action is inserted between two attacks in a combat round. For example, recoil does not apply with bows because a new arrow must be placed on the string between attacks.

Weapons can have a recoil compensation. This value lowers the malus per attack. Thus, the minimum roll for a subsequent attack with a weapon with recoil compensation 1 is only raised by 1. A recoil compensation of 2 ensures that recoil is no longer relevant for the weapon.

Recoil is not accounted for across combat rounds, only within a combat round.

#### Critical hits

*Hits* caused during the hit roll become *critical hits* if they reach the value 11 during the roll. This is equivalent to an *exploding die* "thrown farther", which then shows a result of 5+ again. Changes to the character's *minimum throw* are not applied here.

Critical hits can only be caused by melee attacks, single shot attacks, and throwing weapons, never by burst attacks.

If critical hits are achieved when attacking, they are announced separately from normal hits. A single shot from a bow could thus result in "2 crits, 3 normal hits".

Critical hits are treated like normal hits, but always penetrate any armor. The *protection* of the attacked and the *penetration* of the weapon are only counted on the normal hits, as usual.

If a *cover* roll occurs, critical hits must be treated separately from normal hits. So the attacked person rolls twice on his cover, once for the number of critical hits, and once for the number of normal hits.

##### Megacritical hits

If *critical hits* occur, the *exploding dice* can be rolled further than 11. The roll continues until no 6 is reached on the respective die.

If a die reaches a 5 again after the second roll, it is a *megacritical hit*. These hits are treated as critical hits, but cause an additional wound if not prevented.

For each roll of a 5+, the number of wounds is increased. So one megacritical hit can cause a lot of wounds. The rule of 5+ results in the following limits for wounds:

* **Roll 5+**: normal hit.
* **Roll 11+**: critical hit - ignores armor
* **Roll 17+**: megacritical hit - ignores armor, +1 wound
* **Roll 23+**: megacritical hit - ignores armor, +2 wounds
* **Roll 29+**: megacritic hit - ignores armor, +3 wounds

And so on.

##### Aiming

With melee weapons and single shot, it is possible to aim the weapon. This is not possible in burst mode.

The character can invest actions to aim at his target more precisely. For every 1 action, the critical hit limit is reduced by 1 for the next attack. This bonus to critical hits may not exceed the character's perception value.

If the aiming character is hit while aiming, the accumulated aiming bonus is removed.

#### Attack modes

The *attack modes* with which the bearer of the weapon can use it are indicated with each weapon. The player chooses arbitrarily from the available modes for each attack. Switching the fire mode on modern weapons requires no action.

##### Hand-to-hand combat

All melee weapons have this attack mode exclusively. The character strikes with the weapon in hand-to-hand combat.

* The attack can be *parried*.
* The attack can be *dodged*.
* The attack can cause *critical hits*.
* For the attack, the character can *aim* beforehand.

##### Single shot

One shot is fired per action. This applies to many modern weapons, but also to bows, slingshots and crossbows.

* The attack consumes 1 ammunition.
* The attack **cannot** be *parried**.
* The attack **cannot** be *dodged*.
* The attack can cause *critical hits*.
* The character can *aim* for the attack beforehand.

##### Burst

The weapon is used in burst mode, a short burst of fire is delivered, which is slightly less accurate than a single shot.

* 2 dice are added to the attack roll.
* The attack consumes 3 ammunition.
* The attack **cannot** be *parried**.
* The attack **cannot** be *dodged**.
* The attack cannot **cause** *critical hits*.
* For the attack, the character **cannot** *aim*.

#### Hit rolls for incorrect distance

*Optional Rule*

Each weapon has a specified distance at which it is effective. If the target's distance differs from that specified with the weapon, there is a penalty to the hit rolls.

If the real shooting distance is less than the specified distance of the weapon, the attack is performed normally. If the distance is increased up to the double of the weapon, the minimum roll of the hit roll is increased by 2.

If the target's distance is more than twice the weapon's range away, it is not possible to shoot or attack at the target.

#### Cover

If parts of the person being attacked are hidden from the attacker's view, the rule of cover applies. It depends on how much the attacked is hidden. The cover is classified into 3 levels:

* 4+ Cover: Most of the person being attacked is hidden.
* 5+ cover: The target is half hidden
* 6+ Cover: It is a bit harder to hit the target behind light cover. This effect is achieved among other things by the "hunkered" condition.

If the attacked has at least 6+ cover, he is allowed a cover roll after the *hit roll*. For this, he rolls as many dice as the attacker had *hits*. For each success (on the minimum roll according to the cover), one hit is removed.

If the attacker has had *critical hits*, the cover roll must be rolled separately for critical hits and normal hits to determine which hits were prevented.

##### Shields

Shields can be used when the character wields a one-handed weapon. 

Shields can be used in two different ways.

* For **Shield Block**, the shield is readied in its own turn with two actions. In subsequent combat rounds, the shield provides the cover listed below for all attacks against the character. While the shield block is active, the character's movement range is halved. The **Shield Block** is active until the character cancels it, that is, lowers the shield.
* The **Shield Parry** can be used spontaneously as a *reaction*. It provides the below cover roll for a single attack and costs one action.

Shields provide *cover* according to their protection value when the *Shield Parry* or *Shield Block* is applied. To determine the coverage roll, the *protection* of the shield is subtracted from 7. So a round shield with protection 2 provides a 5+ *cover roll*.

#### Wounds and Piercing

Any success of the *hit roll* which was not prevented by *cover* is a *hit* on the target of the attack. Other circumstances can also cause *hits*, for example a grenade can cause "3 hits with 2 wounds each". Here, hits can be prevented by cover.

If a character takes *hits*, they are reduced by the target's *protection value*. The *protection* is reduced by the *penetration* of the attacker's weapon.

Any hit not prevented by the *protection value* becomes as many wounds as the weapon or effect specifies. If nothing is specified, a hit causes one wound.

##### Damage to armor

*Optional rule*

For every two hits prevented by the *protection*, the armor worn takes 10% damage. If the number of hits is odd, round down. So an attack with 5 hits, 4 of which are prevented by a Kevlar vest reduces the condition of the vest by 20%.

#### Wounds

A *wound* is added directly to the wounds taken by the character. It can only be prevented if a *template*, equipment or other explicitly contains a rule that modifies wounds.

#### Weaponless melee

If the character attacks without a weapon, the player rolls hit dice equal to his *hand-to-hand combat* value. The minimum roll is equal to the character's minimum roll, which is usually 5+.

If the character's *Strength* value is higher than 2, the *Melee* melee attack has *Piercing* 1.

If the character's *Quickness* value is higher than 2, the character adds one die to the roll.

The range of an unarmed melee attack is 1 meter.

#### Dodge

The attacked character can dodge a melee attack as a reaction. This requires that the attacked character has an action available and can sense the attacker. Thus, an attack from behind cannot be dodged.

The value is equal to the dodge value of the lineage plus the average of speed and dexterity (rounded up). The load of armor and weapons reduces this value. Character templates can change it.

To dodge an attack, the character rolls a die to his value in *Dodge*. The minimum roll for this is increased by the number of hits the opponent scores. If the attacked person scores at least one success, he has completely dodged the attack.

### Parry melee attacks

Melee attacks can be parried if the attacked has a suitable melee weapon ready and an action left.

This is done by rolling the weapon as a *reaction*, as if attacking with it. For each success on this roll, one normal hit is removed from the attacker. *Critical hits* are not prevented by the parry and always get through.

### Special Attacks

There are a number of special attacks that a character can use to refine or change their attack.

#### Accurate Attack

In the accurate attack, the character aims longer to land a better hit. The exchange ratio here is 1 action for reducing the minimum roll by 1. The exchange can also go over turns. The minimum roll can be reduced by a maximum of the character's Perception value, but cannot go below 2. No other action can be taken during this time. After that, a normal attack is made with the changed values.

#### K.O. Attack

The K.O. Attack has only the intention of knocking an opponent out, but without inflicting any damage. The attacker must wield a blunt weapon, or at least strike with a blunt object. If the attack is successful, the opponent roll a resistance check. If he does not achieve as many successes as there are hits, he is knocked out.

The attack does not inflict any wounds. Cover and armor are taken into account as usual.

#### Massive attack

In a massive attack, the character gathers all his strength to deliver a massive blow. For each additional action the character invests in this attack, the number of dice for this attack increases by 3, up to a maximum of the character's strength value.

#### Disarming attack

With a disarming attack, the attacker tries to knock the weapon out of the opponent's hand. To do this, he must succeed in an attack on the weapon's arm, with a minimum roll raised by 3. The attacked person must roll on his strength or deftness after the attack, and achieve at least as many successes as the attacker had hits.

If the attacked fails to do so, he has been disarmed.

The disarming attack doesn't cause any wounds.

#### Two-handed fighting

If the character is particularly skilled in the use of a weapon, he can wield two weapons of the same type at the same time, i.e. ambidextrously. Two-handed fighting is only possible with one-handed weapons. Weapons that are wielded with both hands anyway (heavy axes, polearms, etc.) cannot be wielded in two-handed combat.

If a character wields two weapons of the same type at the same time, the character gets one more action per combat round. The weapon he wields with his secondary hand attacks with a minimum roll increased by 1.

#### Support weapon

If this is possible with the weapon being used (usually firearms except bows), the character can place the weapon on a suitable spot before using it. Supporting takes one action. If shooting with a supported weapon, the minimum roll is reduced by 1. It costs no action to pick up a propped weapon again.

#### Coup de grâce

A character can kill an opponent directly if the opponent is *unconscious*, *sleeping*, or *dying*. To do this, the player rolls a normal attack roll. If this roll succeeds with at least one success, the opponent receives the status *dead* with the level corresponding to the successes of the attack. If the opponent is already *dying*, the level of the state is increased by the number of successes of the attack.

If the attack fails, a sleeping victim is likely to awaken.

### Throwing objects

If an item, such as a grenade, is thrown at a target, the character rolls to its *throw* value. The minimum roll is equal to the character's minimum roll, usually 5+.

If the roll results in at least one success, the character has hit his target.

#### Deviation

If the roll on *throwing* shows no success, then the roll has failed. In this case, a roll is made on the deviation.

First, a D12 is thrown to determine the direction of the deviation. The result of the throw gives the direction in the way of the "clock", seen by the throwing character looking at the target. A 3 thus deviates to the right of the target, as seen by the throwing character.

Then a D6 is thrown, which determines the distance of the deviation in meters.

The thrown object thus lands at the determined location.

