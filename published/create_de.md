Zur Erstellung eines Charakters werden Charakterschablonen ausgewählt, die dessen Lebensstationen, Talente und Interessen abbilden (siehe [[appendix-templates|Anhang Charakterschablonen]]). Jede Schablone kann die Attribute und Fertigkeiten des Charakters verändern und Wissen sowie Schatten mit sich bringen. Darüber hinaus können Charakterschablonen Spielmechaniken freischalten, wie etwa das Ausführen von Priesteraktionen oder das Erlernen von Zaubern eines Magieursprungs.

### Werdeganspunkte

Werdegangspunkte werden verwendet, um Charakterschablonen hinzuzufügen. Jede Schablone kostet eine bestimmte Anzahl an Werdegangspunkten.

Neue Charaktere beginnen in der Regel mit **20** Werdegangspunkten. Diese Zahl kann jedoch von der Spielleiterin beliebig festgelegt werden.

Charakterschablonen können negative Punktekosten aufweisen. In diesem Fall erhält der Spieler die Punkte, wenn er die Schablone auswählt. Dies ist beispielsweise bei der Schablone "Säufer" der Fall.

{% if world_book.identifier != "tirakan" %}
### Epochen

Vor Beginn der Kampagne oder des Abenteuers legt die Spielleiterin fest, in welcher Epoche und mit welchen Erweiterungen gespielt wird. Diese Auswahl legt fest, welche Charakterschablonen, Waffen, Rüstungen und Gegenstände verwendet werden können und ob Magie, Körpermodifikationen oder Priesteraktionen möglich sind.

Mögliche Epochen sind:

* Die klassische Antike
* Mittelalter, Wikinger und Kreuzzüge
* Viktorianisches Zeitalter und der Wilde Westen
* Imperialismus und Weltkriege
* Der kalte Krieg und die 80er
* Moderne Zeit
* Nahe Zukunft
* Science Fiction

Optionale Erweiterungen sind:

* Magie
* Horror
* Pantheon
* Körpermodifikationen
* Fahrzeuge und Dronen

{% endif %}

### Schablonen wählen

Eine Charakterschablone stellt eine bestimmte Lebensstation eines Charakters dar. Jede Schablone ist einem der folgenden Bereiche zugeordnet: Bildung, Beruf, Talent, Interessen, Charakter oder Lebensumstände.

Jede Schablone verändert eine kleine Anzahl von Eigenschaften und Fertigkeiten des Charakters positiv oder negativ und kann Wissen oder Schatten mit sich bringen. Darüber hinaus können Schablonen eigene Regeln enthalten, die der Charakter dann übernimmt.

Jede Schablone ist eine bestimmte Anzahl von Werdegangspunkten wert. Dies ist die Anzahl der Punkte, die aufgewendet werden müssen, um die Schablone in den eigenen Werdegang zu übernehmen.

#### Basiswerte

Alle Attribute, Fertigkeiten und sonstigen Werte des Charakters beginnen mit einem einheitlichen Wert. Auf diesen Wert werden die Angaben der Charakterschablonen addiert.

* Aktionen: 2
* Mindestwurf: 5+
* Bonus-, Schicksals- und Wiederholungswürfe: 0
* Persona- und Physiseigenschaften: 1
* Fertigkeiten: 0
* Angeborener Schutz: 0
* Maximale Lebenspunkte: 10
* Arkana: 0
* Zauberpunkte: 0
{% if world_book.identifier != "tirakan" %}* Maximaler Stress: 8
* Biolast: 0{% endif %}

#### Abstammung

Zunächst wird die Abstammungsschablone gewählt, die die Herkunft des Charakters beschreibt. Unterschiedliche Abstammungen haben unterschiedliche Boni. Es kann nur eine Abstammungsschablone gewählt werden, diese kostet keine Werdegangspunkte.

Die verfügbaren Abstammungsschablonen sind im [[appendix-templates|Anhang Charakterschablonen]] aufgelistet.

Die Abstammungsschablone wird beim Werdegang notiert, und die angegebenen Modifikationen werden auf die Werte des Charakters addiert.

#### Weitere Schablonen

Nun können nach Belieben weitere Schablonen ausgewählt werden, bis keine Werdeganspunkte mehr verfügbar sind. Es können Schablonen aus allen Kategorien beliebig zusammengestellt werden. So kann der Charakter einen oder mehrere Berufe haben oder auch gar keinen.

Die angegebenen Modifikationen der jeweiligen Schablone werden auf die Werte des Charakters addiert. Zusätzlich werden Wissen, Schatten und weitere Regeln der Schablone dem Charakterbogen hinzugefügt.

Dabei können alle Werte auch negativ werden (siehe [[chapter-rolls|Würfe und Proben]]).

#### Übrige Werdeganspunkte

Ist der Spieler mit der Zusammenstellung der Schablonen zufrieden, kann er den Charakter einfach als *fertig* deklarieren. Sollten noch nicht ausgegebene Werdeganspunkte übrig sein, so werden diese dem *Ruf* des Charakters hinzugefügt (siehe [[chapter-advancement|Steigern]]). Es gehen also keine Punkte verloren.

### Kontakte und Sprachen

Nachdem die Charakterschablonen festgelegt sind, können Sprachen und Kontakte des Charakters festgelegt werden.

#### Kontakte

Kontakte sind Bekanntschaften oder Verbindungen, die der Charakter bereits vor der Kampagne hatte. Kontakte werden mit Namen und Beschreibung festgehalten, und können nach Belieben ausgedacht werden.

Ein neuer Charakter kann eine bestimmte Anzahl an Kontakten haben, die sich nach der Summe der Attribute *Charme* und *Attraktivität* richtet. 

Die Kontakte werden auf dem Charakterbogen festgehalten.

#### Sprachen

Ein neuer Charakter kann eine bestimmte Anzahl von Sprachen entsprechend der Summe seiner Attribute *Bildung* und *Logik* erlernen. Dies können beliebige Sprachen sein. Beträgt die Summe der Attribute 0 oder weniger, beherrscht der Charakter selbst seine Muttersprache nur eingeschränkt.

Die Sprachen werden auf dem Charakterbogen festgehalten.

### Ausrüstung

Nachdem die Charakterwerte durch die Schablonen festgelegt wurden, kann der Charakter noch mit Ausrüstung ausgestattet werden. Die Spielleiterin legt für die Kampagne oder das Abenteuer ein Startkapital für die Charaktere fest.

{% if world_book.identifier == "tirakan" %}
Das Startkapital beträgt üblicherweise 2.000 Gulden.
{% else %}
Das Startkapital beträgt üblicherweise 2.000 Einheiten der üblichen Währungseinheit, beispielsweise Euro.
{% endif %}

Dieses Startkapital kann dafür verwendet werden, um Ausrüstung, wie etwa Waffen, Rüstungen und Gegenstände zu kaufen. Näheres dazu findet sich im Kapitel [[chapter-gear|Ausrüstung]].

#### Ausrüstungsgegenstände

[[appendix-weapons|Waffen]], [[appendix-riot_gear|Rüstung]] und [[appendix-items|Gegenstände]] können nun für das Startkapital erworben werden. Beliebige Ausrüstungsgegenstände können mit ihren Werten auf dem Charakterbogen notiert, und der Preis vom Startkapital abgezogen werden.

{% comment %}
#### Fahrzeuge und Dronen
{% endcomment %}

#### Vermögen

Alles Startkapital, das nicht für Waffen, Rüstungen und Ähnliches ausgegeben wurde, wird zum Vermögen des Charakters.

### Zauber

{% if world_book.identifier != "tirakan" %}
Wird im Abenteuer oder der Kampagne die Magie-Erweiterung verwendet, so kann der Charakter auch Zauber erlernen.
{% endif %}

Charakterschablonen bieten *Zauberpunkte* und ermöglichen das Erlernen von Zaubern eines bestimmten *Ursprungs*.

Hat der Charakter nun durch die Wahl von Charakterschablonen beides erhalten, so kann er für die Zauberpunkte Zauber wählen, die er beherrscht.

Zauber werden ähnlich wie Schablonen für Punkte erworben. Hierfür werden Zauberpunkte verwendet. Jeder Zauber hat bestimmte Kosten, für die er dem Charakterbogen hinzugefügt werden kann (siehe [[appendix-spells|Anhang Zauber]]). Es können nur Zauber der Ursprünge gewählt werden, die der Charakter durch Charakterschablonen freigeschaltet hat. Näheres dazu findet sich im Kapitel [[chapter-magic|Magie]].

{% if world_book.identifier != "tirakan" %}
### Körpermodifikationen

Wird mit der Erweiterung *Körpermodifikationen* gespielt, so können für das Startkapital [[appendix-body_modifications|Körpermodifikationen]] erworben und eingebaut werden.

Hierbei sind die [[chapter-body_modifications|Regeln]] für Körpermodifikationen zu berücksichtigen, so muss beispielsweise genügend Energie für die Verbraucher verfügbar sein.

Der Vorgang der Integration durch einen Arzt entfällt bei der Charaktererschaffung, die Körpermodifikationen können einfach auf dem Charakterbogen vermerkt werden.
{% endif %}
