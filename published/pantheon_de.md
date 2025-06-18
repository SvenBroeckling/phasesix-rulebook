{% if world_book.identifier == "tirakan" %}

Die Götterwelt Tirakans ist vielfältig und für Laien schwer zu überschauen. Alle Kulturen der Welt haben eigene Gottheiten, die mehr oder weniger präsent sind. Im Allgemeinen sind Götter auf Tirakan sehr nahbar, viele sind direkt anrufbar. Die Völker Tirakans beten für bestimmtes Wetter, für persönliches Glück, für Erfolg in der Schlacht oder für Mitmenschen.

Diese Regeln spiegeln die Nähe der Völker zur Welt der Götter wider.

{% else %}
Diese Erweiterung bringt das Wirken von Göttern in deine Kampagne. Charaktere können in der Lage sein, Göttliches Wirken zu erbitten, und haben eine **Gesinnung** und **Gunst** bei ihrer Gottheit. Es gibt verschiedene Formen der Anrufung, welche von einem Gläubigen ausgeführt werden können.

Das Regelwerk verzichtet hier bewusst auf das Abbilden irdischer Götter oder Glaubensformen, es sind jedoch der Fantasie keine Grenzen gesetzt. So kann etwa für einen Kultisten auch ein Wesen aus dem Cthulhu Mythos eine Gottheit sein.
{% endif %}

### Glaubensniveau

{% if world_book.identifier == "tirakan" %}
Ähnlich wie die Magie entwickelt sich der Glaube Tirakans über die Jahrhunderte. Während die Kirchen lange Zeit in stillem Abwarten für die Rückkehr des Götterwirkens beten, entwickelt sich der Einfluss der Götter zum Ende des Zeitalters zu einem sehr starken, direkten Einfluss. Dies wird durch das **Glaubensniveau** dargestellt, welches sich ähnlich wie das **Magieniveau** verhält und über die Jahrhunderte ändert.

* 1. Jahrhundert: Glaubensniveau 1
* 2. Jahrhundert: Glaubensniveau 1
* 3. Jahrhundert: Glaubensniveau 1
* 4. Jahrhundert: Glaubensniveau 1
* 5. Jahrhundert: Glaubensniveau 1
* 6. Jahrhundert: Glaubensniveau 2
* 7. Jahrhundert: Glaubensniveau 3
* 8. Jahrhundert: Glaubensniveau 4
* 9. Jahrhundert: Glaubensniveau 5
* 10. Jahrhundert: Glaubensniveau 6
{% else %}
Die Macht göttlichen Wirkens richtet sich nach dem *Glaubensniveau*. Dies ist ein globaler Wert, welcher die Stärke von göttlichem Wirken verdeutlicht. Im Allgemeinen wird angenommen, dass in der Welt ein Glaubensniveau von **3** herrscht.

Besondere Orte können jedoch das Glaubensniveau verändern. So können Anrufungen in einer großen Kathedrale stärker sein. Gebiete können vielleicht einem Fluch unterliegen, oder auf andere Art ein niedrigeres Glaubensniveau haben. Das Glaubensniveau wird, wenn es von 3 abweicht, vom Spielleiter festgelegt.
{% endif %}

### Gunst

Die Gunst stellt als Wert das Verhältnis zwischen Diensten des Priesters und Gefälligkeiten des Gottes dar. Der Wert ist zu Beginn 0 und kann sowohl negativ als auch positiv werden.

Die Kosten der Gefälligkeiten werden von der Gunst abgezogen. Gunstpunkte kann der Priester durch gottgläubiges Handeln im Spiel erreichen. Dabei hängt es sehr von der Art der Gottheit ab, womit der Priester in der Gunst der Gottheit steigen kann.

### Reliquien

Reliquien haben in den Kirchen Tirakans eine besondere Rolle inne. Sie stärken die Bindung zum Gott und helfen dem Gläubigen dabei seinen Weg weiterzugehen.

Übliche Reliquien sind Gegenstände aus dem Besitz von Heiligen, aber auch Gebeine dieser. Aber auch ein einfaches Objekt mit Bezug zur Gottheit kann eine Reliquie geringer Stufe sein, wie etwa ein besonderer Stein für Tador. Der Charakter kann auf unterschiedlichsten Wegen zu einer Reliquie gelangen, es bedarf allerdings immer einer Weihe.

Reliquien haben immer eine Stufe, die von 1 bis 6 reichen kann. Eine Reliquie der Stufe 1 kann ein Objekt sein, welches ein Heiliger z.B. einst berührt hat. Bei einer Reliquie der Stufe 6 kann es sich um eine heilige Waffe oder die Gebeine eines Heiligen handeln.

### Die Formen der Anrufung

Es gibt vier Formen der Anrufung eines Gottes. Jede von ihnen wird anders durchgeführt. Jede hat einen anderen Aufwand und erbittet eine andere Gefälligkeit der Gottheit.

Allen Formen der Anrufung gemein ist der Einfluss der Umgebung, der Verfassung des Priesters sowie Glaubensniveau der Welt. So werden auf den **Mindestwurf** jedes Wurfs bei einer Anrufung (es gibt Anrufungen die mehrere Würfe erfordern) die folgenden Modifikationen aufgeschlagen.

* Gunst des Priesters: **-(Gunst/2)**
* Die Intention des Charakters entspricht nicht den Tugenden der Gottheit: **+10**
* Zeremonielle Gestaltung (Kerzen, saubere Tücher etc.) nicht vorhanden: **+5**
* Die Gesinnung des Priesters ist gegensätzlich zur Gottheit: **+15**
* Die Bitte ist nicht die erste Bitte des Tages: **+2**
* Es wird ein Opfer dargebracht: **-3**
* Der Priester verwendet Weihrauch: **-2**
* Die Anrufung geschieht auf Doldag: **-2**
* Die Anrufung wird gesungen (zusätzliche Singen Probe): **-5**
* Das vorherrschende Glaubensniveau: **-Glaubensniveau**
* Zusätzliche Priester bei der Anrufung: **-Anzahl**
* Reliquie vorhanden: **-Stufe**

#### Stoßgebet

Die geringste Form der Bitte ist das Stoßgebet. In einer kurzen, flehenden Anrufung von 3 Sekunden kann der Priester einen Bonus auf eines seiner Attribute oder Fertigkeiten erlangen. Der Bonus entspricht **Glaubensniveau** Punkten und hält für **Glaubensniveau** Minuten an.

Ein Stoßgebet erfordert eine einzelne **Charme-Probe**.

Das Stoßgebet kostet den Priester 2 Gunstpunkte.

#### Segen

Ein Segen vermag einen göttlichen Fluch (das Wirken eines dunklen Gottes, wie jeweils bei dem Wirken angezeigt) zu brechen, kann aber auch auf einen Gegenstand übertragen werden, um so eine gesegnete Waffe, Weihwasser oder ähnliches zu schaffen. Den Segen zu sprechen dauert 5 Minuten, und es hält unbegrenzt an.

Für einen Segen ist eine Willenskraft- und eine Charmeprobe erforderlich.

Der Segen kostet den Priester 5 Gunstpunkte.

#### Geringe Bitte

Die geringe Bitte erfleht direktes göttliches Wirken. Dabei können die als "nieder" eingestuften Fähigkeiten der Gottheit des Charakters und all ihrer Diener erbeten werden. Das Gebet zur geringen Bitte dauert etwa 15 Minuten an. Sie kann auch im Rahmen eines Zeremoniellen Gottesdienstes erfolgen.

Für die geringe Bitte ist ein Charme-Wurf erforderlich.

#### Anrufung

Die Anrufung erbittet einen als "höher" eingestuftes Wirken einer Gottheit. Auch hierbei können sowohl die Gottheit des Charakters als auch dessen Diener angerufen werden. Die Anrufung erfordert eine größere Zeremonie und dauert mindestens 30 Minuten an. Sie kann auch im Rahmen eines Zeremoniellen Gottesdienstes erfolgen.

Für die Anrufung sind 2 Charme Würfe und ein Willenskraftwurf erforderlich.

> Ein Wort zum Wirken der Götter. Das Wirken der Götter wird teilweise mit konkreten Regelvorschlägen beschrieben. Die meisten Beschreibungen bleiben aber eher vage. Dies soll dem Umstand Rechnung tragen, dass das Wesen und Wirken der Götter allein ihre Sache ist. Spielleiter und Spieler sollten sich spontan darauf einlassen, was passiert, wenn ein Gott oder Dämon in das Weltgeschehen eingreift.

#### Weihe

Mit der Weihe wird ein Gegenstand wie z.B. eine Waffe einem Gott übergeben. Die göttliche Macht sorgt dafür, dass der Gegenstand verbessert (Werte plus etwa 30-50%) wird, allerdings gibt es auch eine Wahrscheinlichkeit, dass der Gegenstand nach der Weihe beseelt ist und ein gewisses Eigenleben führt.

Eine Weihe ist eine zweistündige Zeremonie, während der dreimal die Gottheit mittels eines Charme-Wurfes angerufen wird. Zudem ist eine Kraftprobe erforderlich, da der Gegenstand über den ganzen Zeitraum gehalten wird. Zum Abschluss wird auf eine 50% Chance der Beseelung geworfen.

Die Weihe kostet den Priester 7 Gunstpunkte.

#### Stille Andacht

Einmal pro Tag kann der Priester eine Stunde in stiller Andacht an seine Gottheit verbringen. Hierfür wirft er einen **Charme** Wurf und fügt für jeden Erfolg einen Gunstpunkt hinzu.

#### Zeremonieller Gottesdienst

Der zeremonielle Gottesdienst ist ein Dienst an der Gottheit, um ihr Wirken zu stärken und ihr Wort zu verbreiten. Der Gottesdienst kann sowohl eine klassische Zeremonie zum Andenken der Gottheit als auch so etwas wie eine rituelle Beerdigung oder ein Exorzismus sein. Im Rahmen des zeremoniellen Gottesdienstes können geringe Bitten oder Anrufungen erfolgen, das müssen sie jedoch nicht.

Ein zeremonieller Gottesdienst bringt dem Priester für jeden Teilnehmer einen Gunst-Punkt ein, bis zum doppelten **Glaubensniveau** pro Gottesdienst. Wird dabei eine Bitte oder Anrufung ausgeführt werden diese Kosten wieder abgezogen.
