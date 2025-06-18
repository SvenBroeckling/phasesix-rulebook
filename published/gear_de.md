Einen wesentlichen Teil des Abenteurerlebens macht die Ausrüstung aus. Bei einem neuen Charakter kann das Startkapital dafür verwendet werden, Ausrüstung zu kaufen. Dieser Teil beschreibt die verschiedenen Ausrüstungsarten, ihre Eigenschaften und ihre Werte.

## Gegenstände

Die einfachste Form der Ausrüstung sind Gegenstände. Hierbei kann es sich um alles handeln, was der Charakter in seinem Leben ansammelt. Zelte, Fackeln und Bandagen sind Ausrüstungsgegenstände. Auch Tiere und Fuhrwerke fallen unter die Ausrüstung. Erwirbt oder erlangt der Charakter einen Gegenstand, so wird dieser einfach auf dem Charakterbogen vermerkt.

Gegenstände werden in die folgenden Kategorien einsortiert:

* Erste Hilfe
* Fahrzeuge
* Gefäße
* Kuriositäten
* Lichter
* Musikinstrumente
* Tierbedarf
* Trekking Ausrüstung
* Tränke
* Werfbares
* Werkzeuge
* Zutaten
* Überwachung

### Eigenschaften

Gegenstände können verschiedene spielrelevante Eigenschaften haben. Alle Gegenstände haben die folgenden Eigenschaften:

* **Preis**: dies ist der durchschnittliche Kaufpreis des Gegenstands, wenn er erworben wird. Dieser Preis ist in {% if world_book.identifier == "tirakan" %}Gulden{% else %}der Haupteinheit der verwendeten Währung{% endif %} angegeben.
* **Gewicht**: das Gewicht des Gegenstands. Dies dient zur Beurteilung der Traglast des Charakters, auch wenn es hier keine Regel für Überlastung gibt.
* **Verborgenheit**: die Verborgenheit gibt an, wie einfach ein Gegenstand zu finden ist, falls ein Beobachter gezielt danach sucht. Ein höherer Wert steht hier für einen einfacher zu findenden Gegenstand.

{% if world_book.identifier != "tirakan" %}
Ein Gegenstand ist immer einer oder mehreren Erweiterungen zugeordnet. So gibt es zum Beispiel Gegenstände, die nur verfügbar sind, wenn die Magieerweiterung für das Spiel gewählt wurde.
{% endif %}

### Gegenstandsregeln

Einige Gegenstände haben spezielle Regeln, die auch einen Wurf auf eine Fertigkeit oder ein Attribut erfordern können. Diese Regeln sind dann bei dem Gegenstand beschrieben. Eine Bandage erlaubt es zum Beispiel, die Fertigkeit Erste Hilfe zu benutzen, um einen Charakter zu heilen.


### Ladungen

Gegenstände können Ladungen enthalten. Ist dies der Fall, so wird bei einer erfolgreichen Verwendung eine Ladung abgestrichen.

{% if world_book.identifier != "tirakan" %}
Ein professioneller Notfallkoffer hat zum Beispiel 5 Ladungen.
{% else %}
Eine Karaffe Zaubertrank hat zum Beispiel 3 Ladungen.
{% endif %}

Sind alle Ladungen verbraucht, so kann der Gegenstand nicht mehr gemäß seiner Bestimmung benutzt werden, bis er evtl. aufgefüllt wird.

## Waffen

Waffen werden von Alltagsgegenständen unterschieden, sie haben andere Spielwerte und andere Mechaniken. Wie Gegenstände werden Waffen auf dem Charakterbogen vermerkt, wenn sie erstanden oder auf anderem Wege erlangt werden.

Waffen sind unterschiedlichen Waffengattungen zugeordnet. Im Spiel ist hierbei nur der Unterschied zwischen Nahkampf-, Fernkampf- und Wurfwaffe wichtig, da auf den jeweiligen Wert (Schießen, Nahkampf, Werfen) gewürfelt wird. Es gibt folgende Waffengattungen:

* Äxte
* Bögen
* Hiebwaffen
* Klingenwaffen
* Schleudern
* Stangenwaffen
* Wurfwaffen
{% if world_book.identifier != "tirakan" %}* Gewehre
* Maschinengewehre
* Maschinenpistolen
* Pistolen
* Schrotflinten
* Schwere Waffen
* Sturmgewehre{% endif %}

{% if world_book.identifier != "tirakan" %}
In unterschiedlichen Epochen können unterschiedliche Waffengattungen verfügbar sein. Granaten zählen zu Gegenständen, und nicht zu den Waffen.
{% endif %}

### Eigenschaften

Waffen haben die folgenden Eigenschaften:

* **Preis**: wie bei Gegenständen ist dies der Preis, für den die Waffe im Durchschnitt erstanden werden kann
* **Seltenheit**: Die Seltenheit beschreibt, wie verfügbar die Waffe ist. Diese kann *Gewöhnlich*, *Außergewöhnlich*, *Selten*, *Legendär* oder *Einmalig* sein.
* **Gewicht**: das Gewicht der Waffe dient wie bei den Gegenständen dazu, einen groben Überblick über die Traglast des Charakters zu erhalten
* **Verborgenheit**: die Verborgenheit der Waffe gibt an, wie leicht sie zu erkennen ist, wenn nach ihr gesucht wird. Ein höherer Wert bedeutet ein leichteres Erkennen der Waffe
* **Typ**: der Typ der Waffe gibt an, zu welcher Waffengattung die Waffe gehört.
* **Schadenspotential**: dieser Wert ist mit einer Anzahl an Würfeln angegeben. Die Würfel stellen das Potenzial der Waffe dar, mehr Schaden zu verursachen, und werden bei Angriffswürfen zum Fertigkeitswert hinzugenommen.
* **Durchschlag**: verringert den Schutz des Angegriffenen um die angegebene Anzahl Schutzeinheiten. Damit der Schutz noch wirksam ist, muss der Angegriffene mehr Einheiten einsetzen, als der Durchschlag der Waffe beträgt.
* **Aktionen zum Bereitmachen**: Waffen können eine unterschiedlich lange Zeit benötigen, um sie bereitzumachen. In der Regel dauert es eine Aktion, eine Waffe zu wechseln oder zur Hand zu nehmen. Es gibt jedoch auch sehr schnelle Waffen, auf die ohne Verzögerung gewechselt werden kann, und auch sehr aufwändige Waffen.
* **Reichweite (Meter)**: die Reichweite ist bei allen Waffengattungen angegeben. Bei Fernkampf- und Wurfwaffen gibt sie die maximale Reichweite an, auf der ein Ziel sinnvoll getroffen werden kann. Nahkampfwaffen mit einer Reichweite über einem Meter können auf die angegebene Reichweite benutzt werden, wie etwa Stangenwaffen.

Fernkampfwaffen haben zusätzlich folgende Eigenschaften:

* **Kapazität** beschreibt, wie viel Munition die Waffe gleichzeitig halten kann, also z.B. die Magazingröße bei modernen Waffen.
* **Nachladeaktionen** gibt an, wie viele Kampfaktionen der Charakter investieren muss, um die Waffe vollständig neu zu laden.
{% if world_book.identifier != "tirakan" %}* **Rückstosskompensation**: bei einem direkt auf einen Schuss folgenden weiteren Schuss in *derselben* Kampfrunde kommt ein Rückstossmalus zum Tragen. Die Rückstosskompensation wird von diesem Malus abgezogen, eine Waffe mit hoher Rückstosskompensation macht direkt aufeinander folgende Schüsse also einfacher.{% endif %}

{% if world_book.identifier != "tirakan" %}
#### Angriffsmodi

Waffen haben immer mindestens einen Angriffsmodus. Diese sind in der Waffentabelle bei den Waffen angegeben. Gibt es mehr als einen Angriffsmodus, so kann der Charakter diesen bei jeder Verwendung der Waffe wählen, ohne eine Aktion für das Umschalten zu verwenden. Die Angriffsmodi sind (siehe [[chapter-combat|Der Kampf]]):

* **Einzelschuss**: kann kritische Treffer verursachen.
* **Feuerstoß**: gibt zwei Würfel zusätzlich zum Trefferwurf, kann keine kritischen Treffer verursachen.
* **Nahkampf**: die Waffe wird im Nahkampf verwendet, kann kritische Treffer verursachen.

In zusätzlichen Erweiterungen oder Welten kann es auch weitere Angriffsmodi mit besonderen Regeln geben.
{% endif %}

### Regeln

Waffen können, ähnlich wie Gegenstände, besondere Regeln haben. Diese beschreiben im Detail, was bei der Benutzung der Waffe zu beachten ist.

Zusätzlich zu ausformulierten Regeln gibt es auch die Angabe besonderer verursachter Zustände (siehe [[chapter-wounds|Wunden und Heilung]]). In der Regel werden diese mit einem Wert angegeben. Dies ist der Wert, den der getroffene auf den entsprechenden Zustand addiert, **wenn die Waffe Wunden verursacht**. Mögliche Zustände sind:

* Blutend X
* Vergiftet X
* Geschockt X
* Brennend X

### Waffenmodifikationen

Zusätzlich zu den Waffen gibt es eine Liste an Waffenmodifikationen. Durch diese lassen sich Waffen modifizieren.

{% if world_book.identifier != "tirakan" %}
So ist es in der Moderne möglich, ein Visier an einer Waffe anzubringen. Aber auch besondere Munition wird als Waffenmodifikation dargestellt, so bringt die *Horror-Erweiterung* zum Beispiel Silbermunition mit.
{% endif %}

Waffenmodifikationen sind in die folgenden Kategorien eingeteilt:

* **Klinge**: etwa eine gehärtete Klinge oder eine besondere Gravur
* **Munition**: besondere Munitionstypen, aber auch Köcher
* **Griffe**: Lederumwickelte Griffe für Schwerter und ähnliches
{% if world_book.identifier != "tirakan" %}* **Lauf**: Schalldämpfer für moderne Waffen
* **Visiere**: Visiere für moderne Waffen
* **Sondervorrichtung**: Lichter, Dreibeine und ähnliches{% endif %}

In der Regel verändert diese Waffenmodifikationen einen oder mehrere Werte der Waffe. Sie können jedoch auch eigene Regeln mitbringen.

Charaktere können im Spiel bereits modifizierte Waffen finden oder erwerben, aber natürlich auch eine Modifikation in Auftrag geben.

## Rüstung

Rüstungsgegenstände werden wie auch Waffen von den normalen Gegenständen getrennt auf dem Charakterbogen vermerkt. Rüstung bietet *Schutz*, welcher im Kampf Wunden verhindern kann. Zusätzlich zu tragbarer Rüstung werden in dieser Liste auch Schilde aufgeführt, die dem Charakter Deckung bieten können.

Rüstungen werden in Kategorien eingeteilt:

* Kleidung
* Leichte Rüstung
* Mittlere Rüstung
* Schwere Rüstung
* Schild

### Eigenschaften

Rüstungsgegenstände haben die folgende spielrelevanten Werte:

* **Typ**: die Rüstungsart, also z.B. "Leichte Rüstung"
* **Preis**: der durchschnittliche Kaufpreis der Rüstung
* **Gewicht**: das Gewicht der Rüstung
* **Verborgenheit**: wie schwer ist die Rüstung auszumachen, wenn ein Beobachter gezielt danach sucht?
* **Belastung**: Schwere Rüstung behindert den Charakter bei körperlichen Handlungen. Die Belastung wird vom Ausweichen-Wert des Charakters abgezogen.

#### Schutz

Jedes Rüstungsteil hat eine bestimmte Anzahl von Schutzeinheiten. Diese werden bei der Rüstung in Form von Schilden dargestellt. Dieser Schutz kann im Kampf ausgegeben werden, um Treffer zu verhindern. Es gibt folgende Arten von Schutz:

* **Normaler Schutz**: Dieser Schutz kann verwendet werden, um einen normalen Treffer zu verhindern.
* **Schutz vor kritischen Treffern**: Dieser Schutz kann einen kritischen Treffer oder einen normalen Treffer verhindern.
* **Haftender Schutz**: Verhindert einen normalen Treffer. Die Waffe bleibt in der Rüstung stecken und muss für eine Aktion gelöst werden.
* **Blutungsschutz**: Verhindert einen Treffer, und dass ein Angriff den Blutend Status verursacht.
* **Giftschutz**: Verhindert einen Treffer und dass ein Angriff den Status Vergiftet verursacht.
* **Feuerschutz**: Verhindert einen Treffer und dass ein Angriff den Status Brennend verursacht.
* **Reflektionsschutz**: Verhindert einen normalen Treffer und verursacht einen Treffer beim Angreifer.
* **Schutz vor Schock**: Verhindert einen Treffer, und dass der Angriff den Zustand Geschockt verursacht.

Der Schutz aller Rüstungsteile wird zu einem Schutzpool zusammengefasst, der im Kampf eingesetzt werden kann. Näheres siehe [[chapter-combat|Der Kampf]].


## Währung

{% if world_book.identifier == "tirakan" %}
Obwohl es in unterschiedlichen Reichen Tirakans unterschiedliche Währungen gibt, ist das Asgoraner Währungssystem jedoch nahezu überall gültig. 

Die übliche Münze ist der *Gulden*, in dieser Einheit sind auch die Preise aller Gegenstände angegeben. Ein Gulden setzt sich aus 100 *Deut* zusammen. Für 250 *Gulden* erhält man eine goldene Unze, und für 4 Unzen einen *Barren*.
{% else %}
In unterschiedlichen Szenarien und Welten kann es unterschiedliche Währungen geben. Jedem Charakter und jeder Kampagne wird eine Währungstabelle zugeordnet, die die verschiedenen Einheiten der Währung vorgibt. Charaktere können ihr Vermögen auf dem Charakterbogen notieren. Währungstabellen sind z.B.

* Euro
* Dollar
* Taler
* Gulden (Tirakans Reiche)
* Yuan

Ob im Spiel Währung eine Rolle spielt, liegt allein in der Hand der Gruppe und des Spielleiters, sie ist optional.
{% endif %}
