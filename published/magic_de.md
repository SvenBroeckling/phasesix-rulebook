{% if world.identifier == "tirakan" %}
Die Magie Tirakans ist in unterschiedlicher Weise besonders. Auf der Welt herrscht ein **Magieniveau**, welches die Stärke von Zaubern beeinflusst. Zudem ist die Magie immer von einem **Ursprung**, und Zauber können **Nebeneffekte** verursachen.
{% else %}
Deine Kampagne soll Magie enthalten? Also versteht mich nicht falsch, verwechselt Magie nicht mit göttlichem Wirken oder gar mit Körpermodifikationen. Magie ist eine sonderbare Macht, welche je nach Universum ganz anders dargestellt sein kann.

In der Antike oder im Mittelalter kann das Hinzufügen von Magie dazu führen, dass die Kampagne sich eher wie eine Fantasywelt anfühlt. In der Moderne mag Magie zu einer Cthulhuiden Geschichte beitragen, in der Zukunft kann es zu einer Szenerie wie im in verschiedenen Geschichten beschriebenen Seattle des Jahres 2052 führen.

Die Magie Erweiterung ist unabhängig von Epochen oder anderen Erweiterungen. Sie kann zu jeder beliebigen Zeit dazu gewählt werden, um in der Kampagne Magie zu ermöglichen.
{% endif %}

### Magieniveau

{% if world.identifier == "tirakan" %}
Die Welt von Tirakan hat ein Magieniveau, welches sich über die Jahrhunderte entwickelt. Es gibt auch besondere Orte, an denen das Magieniveau von dem sonst üblichen abweicht.

* 1. Jahrhundert: Magieniveau 1
* 2. Jahrhundert: Magieniveau 2
* 3. Jahrhundert: Magieniveau 3
* 4. Jahrhundert: Magieniveau 4
* 5. Jahrhundert: Magieniveau 5
* 6. Jahrhundert: Magieniveau 4
* 7. Jahrhundert: Magieniveau 3
* 8. Jahrhundert: Magieniveau 2
* 9. Jahrhundert: Magieniveau 1
* 10. Jahrhundert: Magieniveau 0
{% else %}
In der Welt herrscht ein gewisses *Magieniveau* vor. Dieses verdeutlicht die Stärke der Magie, welche die Charaktere umgibt. In der Regel ist dieses Magieniveau **3**. Besondere Orte können ein davon abweichendes Magieniveau haben, so kann zum Beispiel ein magischer Ort an einer alten Eiche in einem verwunschenen Wald ein höheres Magieniveau haben. Auch ist es möglich, dass in einer Welt gespielt wird, in der Magie einen weitaus höheren Einfluss hat.
{% endif %}

Das aktuelle *Magieniveau* hat Einfluss auf den jeweils ausgeführten Zauber. Die Beschreibung des Zaubers enthält in der Regel eine Angabe darüber, wie das *Magieniveau* bei dem Zauber berücksichtigt wird.

Liegt das Magieniveau über 5, so äußert sich die gewirkte Magie vollkommen chaotisch und unzuverlässig. Der Spielleiter entscheidet hierbei, wie ein Zauber genau ausgeführt wird. Zudem verursacht jeder bei einem Magieniveau von 6 oder höher gewirkte Zauber auf jeden Fall **Nebeneffekte**.

### Grundlegende Attribute

Die Magie basiert auf zwei grundlegenden Attributen, welche Charaktere haben und welche durch Schablonen erlangt werden können.

#### Arkana

*Arkana* spiegelt die Menge an Magie wider, die der Charakter in sich vereinen und speichern kann. Mit *Arkana* wirkt der Charakter Zauber und führt Rituale aus. Schablonen, wie z.B. "Arkaner Lehrmeister" steigern das maximal mögliche Arkana, welches ein Charakter haben kann.

*Arkana* regeneriert sich durch eine Rast.

#### Zauberpunkte

*Zauberpunkte* werden verwendet, um Zauber zu erlernen. *Zauberpunkte* kann der Charakter auch durch Schablonen erlangen. So gibt die Schablone "Arkane Schule" zum Beispiel 10 Zauberpunkte.

Sind *Zauberpunkte* einmal für einen Zauber ausgegeben, so sind sie verbraucht und können nicht erneut verwendet werden. Im Gegensatz zu *Arkana* ist dies kein Wert, der sich durch Rast auffrischt.

### Fertigkeiten

Mit der Magie Erweiterung erhält jeder Charakter zwei neue Fertigkeiten, welche er für das Handeln in der magischen Welt verwenden kann.

#### Zaubern

Die Fertigkeit *Zaubern* wird zum Ausführen von Zaubern und Ritualen verwendet. Sie setzt sich aus den Attributen *Willenskraft* und *Charme* zusammen und kann durch Schablonen gesteigert werden. 

#### Magiekunde

*Magiekunde* wird immer dann verwendet, wenn es um das Wissen um magische Begebenheiten oder Artefakte geht. Jeder Charakter hat diese Fertigkeit, welche sich aus *Bildung* und *Gewissenhaftigkeit* zusammensetzt.

### Zauber erlernen

Um einen Zauber zu erlernen, benötigt ein Charakter drei Dinge: Ruhe (es kann nur zwischen den Spielsitzungen ein Zauber erlernt werden) und verfügbare Zauberpunkte. Zudem benötigt er eine Thesis, eine Möglichkeit auch an das Wissen über diesen Zauber zu gelangen. Letzteres ist Sache der Kampagne, oder des Spielleiters.

*Zauberpunkte* sind dann verfügbar, wenn die Zahl der ausgegebenen *Zauberpunkte* kleiner ist als die durch Schablonen erhaltenen *Zauberpunkte*. Jeder Zauber hat bestimmte Punktekosten. Um ihn zu erlernen wird der Zauber auf dem Charakterbogen als gelernt vermerkt.

Ein Zauber kann mehrfach gelernt werden. Dies ist möglich, da man Zauber durch Zauberschablonen verändern kann. So kann man zum Beispiel einen Energieblitz einmal als Energiezauber und einmal als Lichtzauber gestalten.

#### Zauberwerte

Ein Zauber hat verschiedene Werte, welche im Spiel berücksichtigt werden.

Das *Zauberattribut* gibt vor, auf welches Attribut (zusammen mit dem Wert *Zaubern*) zum Ausführen des Zaubers geworfen wird. Es wird von der Schule der Magie vorgegeben (s.U.).

Der Wert unter *Arkana* beschreibt die Kosten des Zaubers beim Ausführen. Um einen Zauber mit einem *Arkanawert* von 2 auszuführen, muss der Spieler auch zwei Arkana verfügbar haben und beim Ausführen abstreichen.

Die *Stärke* des Zaubers beschreibt, wie effektiv der Zauber wirkt. Bei neu erlernten Zaubern ist die Stärke in der Regel 1, kann aber durch Zauberschablonen gesteigert werden. Zudem wird die Stärke beim Ausführen durch die Erfolge des Zauberwurfs gesteigert (s. [[section-cast-a-spell|Zauber ausführen]]).

Jeder Zaubert hat eine bestimmte *Reichweite*. Hierbei handelt es sich um die maximale Entfernung vom Zaubernden, in der ein Zauber wirken kann. Dies ist nicht zu verwechseln mit einer möglichen Fläche, auf der der Zauber wirkt. Diese ist dann in der Zauberbeschreibung erwähnt. Ist die *Reichweite* eines Zaubers 0, so wirkt der Zauber nur bei/an dem Zaubernden selbst.

Die *Form* des Zaubers bestimmt den Wirkungsbereich. Es kann eine geometrische Form, etwa eine Linie oder eine Sphäre sein, oder auch keine bestimmte Form. Letzteres ist der Fall, wenn der Zauber Berührung erfordert oder direkt beim Zaubernden wirkt.

Die *Aktionen* eines Zaubers geben an, wie viele Aktionen das Ausführen des Zaubers benötigt.

Die *Dauer* eines Zaubers gibt an, wie lange der Zauber wirkt. Einige Zauber haben eine sofortige Wirkung, andere wirken über eine bestimmte Zeit hinweg.

Wenn ein Zauber *Konzentration* erfordert, muss sich der Zaubernde auf den Zauber konzentrieren. Solange er dies tut, kann er keine anderen Zauber wirken. Ein Zauber, der Konzentration erfordert, endet, wenn der Zaubernde Schaden erleidet.

#### Schulen

Zauber in Phase Six sind Schulen zugeordnet, welche Zauber in grobe Kategorien einordnen. Jeder Charakter kann aus beliebigen Schulen Zauber wählen, der Schule ist jedoch jeweils ein unterstützendes Attribut zugeordnet.

* Schaden *(Kraft)*
* Kontrolle *(Willenskraft)*
* Transmutation *(Geschick)*
* Heilung *(Gewissenhaftigkeit)*
* Illusion *(Schnelligkeit)*
* Weissagung *(Auffassungsgabe)*
* Widerrufung *(Logik)*
* Beschwörung *(Charme)*
* Verzauberung *(Attraktivität)*

### Zauberschablonen

Zauberschablonen verändern die Werte eines Zaubers, können zudem Effekte hinzufügen oder das Verhalten des Zaubers komplett ändern. Zauberschablonen sind in vier Kategorien eingeteilt:

* Grundlegend: Grundlegende Anpassungen von Zaubern
  * Kraftvoller Zauber (3 Zauberpunkte): Die Stärke des Zaubers wird um eins erhöht.
  * Einfach auszuführen (5 Zauberpunkte): Der Zauber benötigt 1 Arkana weniger, jedoch mindestens 1 Arkana.
  * Zwillingszauber (5 Zauberpunkte): Der Zauber erfasst ein Ziel zusätzlich. Für alle Ziele tritt die Wirkung ein.
  * Große Reichweite (2 Zauberpunkte): Die Reichweite des Zaubers ist um 20 Meter erhöht.
  * Schnelle Ausführung (3 Zauberpunkte): Der Zauber benötigt eine Aktion weniger, jedoch mindestens 1 Aktion.
* Affinität (1 Zauberpunkt): Das Element des Zaubers wird geändert. Dies hat zunächst keine Auswirkung in der Spielmechanik, jedoch kann so z.B. ein Säurezauber zu einem Feuerzauber werden.
* Form (3 Zauberpunkte): ändert die Form des Zaubers, zum Beispiel von einem Punkt auf eine Sphäre mit gewissem Durchmesser.
* Schule (7 Zauberpunkte): ändert die Schule des Zaubers, z.B. von Beschwörung auf Schaden. Damit wird auch das Attribut geändert, auf das was geworfen wird.

Zauberschablonen können zu jedem gelernten Zauber hinzugefügt werden. Hierzu wird auf dem Charakterbogen beim Zauber vermerkt, dass er die spezielle Schablone enthält, z.B. "Einfache Heilung (Kraftvoller Zauber)"

Jede Zauberschablone kann auch öfter als ein mal zu einem Zauber hinzugefügt werden.



### Zauber vergessen

Ebenso wie das Lernen von Zaubern ist es mit der notwendigen Ruhe möglich, Zauber zu vergessen. Hierzu wird der Zauber vom Charakterbogen entfernt, und dem Charakter können die verwendeten Zauberpunkte wieder gut geschrieben werden.

### Zauber ausführen

<span id="section-cast-a-spell"></span>

Ein Zauber kann ausgeführt werden, wenn der Charakter noch mindestens die beim Zauber angegebenen Arkana verfügbar hat.

Um einen Zauber zu wirken, wirft der Spieler auf den *Zaubern* Wert, welcher beim Zauber angegeben ist. Dieser Wert setzt sich aus der *Zaubern-Fertigkeit* des Charakters und dem Attribut der Zauberschule zusammen.

Erreicht der Wurf mindestens einen Erfolg, so ist der Zauber gelungen. Für jeden erzielten Erfolg wird nun die *Stärke des Zaubers* um eins erhöht.

Der Effekt des Zaubers tritt, wie in der Beschreibung angegeben, ein. Die angegebenen Arkana-Kosten werden beim Charakter abgestrichen, auch wenn der Zauber misslungen ist.

> Luta möchte eine einfache Heilung wirken. Ihr *Zaubern* Wert ist 1, in dem Attribut *Gewissenhaftigkeit* (Welches das Attribut der Heilungsschule ist) hat sie 5. Sie hat somit für das Ausführen des Zaubers 6 Würfel zur Verfügung.
> 
> Sie wirft ein Ergebnis von 3,4,5,5,3,1. Somit hat sie 2 Erfolge erreicht, welche zur *Stärke* des Zaubers addiert werden. Sie heilt somit 3 Wunden.

### Nebeneffekte

Die Magie ist instabil, es können Nebeneffekte auftreten. Immer dann, wenn ein Zauberwurf genau **zwei Einsen** zeigt treten Nebeneffekte auf, egal ob der Zauber gelungen ist, oder nicht.

* Die genauen Auswirkungen auf den Zauber liegen in der Hand des Spielleiters. Es kann kleine Abweichungen der Beschreibung geben, aber auch eine komplette Umkehr.
* Nebeneffekte wirken auf Magiespeicher. Diese haben eine Chance zu explodieren, wenn es in ihrer Nähe zu Nebeneffekten kommt. Wenn in direkter Nähe eines Magiespeichers Nebeneffekte auftreten, wird für jedes im Magiespeicher gespeicherte Arkana ein W6 geworfen. Der Magiespeicher verliert für jede 1, welche geworfen wird, ein Arkana. Die Explosion verursacht an allen Charakteren im Umkreis von 3 Schritt für jedes Arkana **3 Treffer mit je 2 Wunden und Durchschlag 1**. Deckung und Rüstung gelten wie gewohnt.

### Magisches Duell

In einigen der folgenden Regeln ist das **Magische Duell** eine verwendete Regel. Magier können sich auf ein magisches Duell einlassen.

Wenn das Duell von einem Magier initiiert wird, muss der aufgeforderte Magier dem Duell zustimmen, sonst kommt es nicht dazu. Es hat keine Auswirkungen, wenn ein Duell abgelehnt wird. Das Duell findet ausschließlich im Geist statt, es sind keinerlei körperlichen Handlungen erforderlich.

Um Zauber zu übernehmen, bedarf es keiner Zustimmung zu einem magischen Duell, es wird einfach die Probe geworfen.

Um ein magisches Duell auszutragen, werfen beide Kontrahenten auf ihre **Zaubern-Fähigkeit**. Der Teilnehmer mit den meisten Erfolgen gewinnt das Duell. Der Unterlegene nimmt die Differenz der Erfolge direkte Wunden hin. Schutz und Deckung verhindert hierbei keine Wunden.

### Übernehmen fremder Zauber

Ist ein Zauber aktiv, so kann er von einem Magier übernommen werden. Hierzu wird ein **Magisches Duell** durchgeführt, wobei der Magier gegen den **Zaubern-Wert** des Magiers wirft, der den Zauber ausgeführt hat. Ist das Duell gelungen, so ist der Zauber nun unter Kontrolle des Übernehmenden, und kann z.B. **fallengelassen** werden.

### Umlenken von Zaubern

Eigene Zauber können umgelenkt werden, solange sie aktiv sind. Das Umlenken eines Zaubers benötigt eine Aktion, und einen Wurf auf die **Zaubern-Fähigkeit**. Es kostet 1 Arkana, einen Zauber auf ein anderes Ziel umzulenken. Das Ziel muss hierbei ein gültiges Ziel für den Zauber sein. So kann ein Zauber mit einer Reichweite von 0 (Berührung) nicht auf ein entferntes Ziel umgelenkt werden.

### Magie und Rüstungen

Das Tragen von Rüstungen behindert die Ausübung von Magie nicht direkt. Weder das Material der Rüstung, noch die Ausgestaltung der Rüstungsform haben einen Einfluss auf das Wirken von Zaubern. Bei Rüstungen, die die Bewegungsfreiheit sehr einschränken, kann es jedoch zu Schwierigkeiten bei notwendigen Gesten der Ausführung kommen.

Rüstungen vom Typ **Schwere Rüstung** erhöhen den Mindestwurf beim Zaubern um ihre **Belastung**.

### Magische Artefakte

Die Magieerweiterung bringt neben Zaubern auch die Möglichkeit von magischen Gegenständen, Waffen, Rüstungen oder Waffenmodifikationen mit sich. Zudem können Artefakte vom Spieler erstellt werden.

Ein *Einfacher Heiltrank* stellt etwa bei Benutzung 1W3 Wunden wieder her.

#### Artefakte erstellen

Der Charakter, der ein Artefakt erstellen will, benötigt nur den Gegenstand, in den der Zauber hineinfliessen soll. Um ein Artefakt zu erstellen, führt er den Zauber normal aus und bindet ihn in dem Gegenstand. Dabei legt er auch die Handlung fest, mit der der Zauber in dem Artefakt ausgelöst werden soll. Das kann eine komplexe Handlung oder auch nur ein gesprochenes Wort sein.

Nach normaler Ausführung des Zaubers bestimmt die Anzahl der Erfolge, wie stark ein Artefakt ist. Ist der Wurf misslungen, so ist auch die Erschaffung des Artefakts misslungen. Gelingt der Wurf, so ist das Artefakt so oft zu benutzen, wie der Wurf Erfolge zeigt. Die Kosten für die Erschaffung eines Artefaktes ergeben sich aus den Arkanakosten für den Zauber multiplizert mit den Anwendungen des Artefaktes. Übersteigen diese die maximalen Arkanapunkte des Charakters, so werden so viele Anwendungen im Artefakt gebunden, wie der Charakter mit seinem Arkana bezahlen kann.

Ganz selten kann es passieren, dass ein Artefakt unbegrenzt aktiv ist. Welche Qualität ein Artefakt hat, bestimmt nicht der Charakter, der das Artefakt erstellt, sondern nur das Schicksal selbst. Kein Magier kann vorhersehen, wie stark ein Artefakt wird, das er erstellt.

Zeigt ein Erfolg des Wurfes mindestens einen Wert von 30, so hat er ein unendliches Artefakt geschaffen.

Bei einem unendlichen Artefakt wird die Zahl der Erfolge für die Ermittlung der Kosten verdoppelt. Überschreiten diese das verfügbare Arkana des Charakters, so werden überschüssige Kosten durch Wunden abgedeckt.

Bei der Erschaffung des Artefaktes wird die Magiekunde des Charakters, der das Artefakt erstellt, in einem Wert festgehalten, der Artefaktstufe genannt wird. Diese Artefaktstufe gibt an, wie mächtig der Ersteller zu dem Zeitpunkt war, als er das Artefakt geschaffen hat.

#### Artefakte benutzen

Um ein Artefakt zu benutzen, genügt es, die beschriebene Handlung auszuführen. Ist ein Zauber in dem Gegenstand gesichert, dann wird er so ausgeführt, den Ausführenden kostet das kein Arkana. Die Wirkung des Zaubers tritt so in Erscheinung, als währe er direkt von einem Magier ausgesprochen worden.

Um ein Artefakt benutzen zu können, muss die Magiekunde der Person, die das Artefakt benutzen will, gleiche oder höher der Artefaktstufe des Artefakts sein. Ist die Magiekunde des Anwenders niedriger, so muss er bei einem *Zaubern-Wurf* bestehen, dessen Erfolge mindestens der Differenz zwischen seiner Magiekunde und der Artefaktstufe entsprechen.

### Das Speichern von Arkana

Die Magie ist ein nicht einfach fassbares Element. Doch wenn es einem Wesen gegönnt ist, mit ihr umzugehen (ein Charakter also *Arkana* besitzt), so kann der Charakter sie problemlos in allen nichtmagischen Materialien speichern, um später wieder auf sie zurückzugreifen. Doch dieses Speichern ist nicht ganz gefahrlos.

#### Speicher erstellen

Um einen magischen Speicher zu erstellen, genügt es, den Gegenstand, in dem *Arkana* gespeichert werden soll, zu berühren und die Kraft einfach in den Gegenstand hineinfließen zu lassen. Die Prozedur dauert so viele Stunden, wie der Charakter an *Arkana* in den Speicher fliessen lassen will und ist völlig ungefährlich. Das *Arkana* des Charakters wird anschliessend vom *Arkana* des Charakters abgezogen und bei dem Speicher notiert.

Magische Speicher erhalten, wie Artefakte eine Artefaktstufe, welche der *Magiekunde* des Erstellers entspricht.

#### Speicher benutzen

Ein Charakter entlädt einen Speicher, indem er ihn berührt und die gespeicherte Kraft in sich aufnimmt. Dabei darf er nicht über seine maximales *Arkana* kommen. Er muss nicht das ganze gespeichete *Arkana* auf einem Mal entnehmen, die Kraft kann auch dosiert werden.

Ein Fremder kann den magischen Speicher nur nutzen, wenn seine *Magiekunde* gleich oder höher ist als die Artefaktstufe des Speichers.

#### Gefahren der Speicher

Magische Speicher sind instabil, sie explodieren, wenn es in ihrer Nähe zu magischen Instabilitäten kommt. Misslingt in der Nähe eines Speichers ein Zauber, so wirft der Träger des Speichers auf seine *Magiekunde*. Erreicht er hierbei mindestens so viele Erfolge wie der Speicher *Arkana* hat, so ist eine Explosion verhindert. Andernfalls explodiert der Speicher.

Wenn ein Speicher explodiert, verursacht er im Umkreis von 2W6 Metern doppelt so viele Treffer, wie *Arkana* im Speicher gespeichert ist. Die Explosion verursacht eine Bonuswunde und sowohl *Brennend 1* als auch *Geschockt 1*.
