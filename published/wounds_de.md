Die körperliche Unversehrtheit des Charakters wird in Form von Wunden dargestellt. Ein Charakter kann eine bestimmte Anzahl von Wunden aushalten, ohne ohnmächtig zu werden. 

### Wunden und Boosts

Betrachtet man den Charakterbogen eines unversehrten Charakters, so sieht man eine Leiste von gefüllten Herzen:

<i class="fas fa-heart fa-2x text-danger"></i>
<i class="fas fa-heart fa-2x text-danger"></i>
<i class="fas fa-heart fa-2x text-danger"></i>
<i class="fas fa-heart fa-2x text-danger"></i>
<i class="fas fa-heart fa-2x text-danger"></i>
<i class="fas fa-heart fa-2x text-danger"></i>
<i class="fas fa-heart fa-2x text-danger"></i>
<i class="fas fa-heart fa-2x text-danger"></i>
<i class="fas fa-heart fa-2x text-danger"></i>
<i class="fas fa-heart fa-2x text-danger"></i>

Diese 10 Herzen stellen die Wunden dar, die ein Charakter hinnehmen kann, ohne ohnmächtig zu werden. Jede Schadensquelle verursacht eine bestimmte Zahl von Wunden. Dies kann eine feste Zahl an Wunden sein, wie bei den meisten Waffen. Es kann jedoch auch eine Würfelformel verwendet werden. 

Die Herzen werden abgestrichen oder geleert, sobald der Charakter Wunden hinnimmt. So kann sich die Lebensanzeige nach einem Treffer einer Waffe folgendermaßen entwickeln:

<i class="fas fa-heart fa-2x text-danger"></i>
<i class="fas fa-heart fa-2x text-danger"></i>
<i class="fas fa-heart fa-2x text-danger"></i>
<i class="fas fa-heart fa-2x text-danger"></i>
<i class="far fa-heart fa-2x text-danger"></i>
<i class="far fa-heart fa-2x text-danger"></i>
<i class="far fa-heart fa-2x text-danger"></i>
<i class="far fa-heart fa-2x text-danger"></i>
<i class="far fa-heart fa-2x text-danger"></i>
<i class="far fa-heart fa-2x text-danger"></i>

Diese leeren Herzen können durch Heilung wieder gefüllt werden. 

#### Boost

Anders verhält es sich mit Boost. Einige Gegenstände verleihen bei Anwendung Boosts. Boosts werden als andersfarbige Herzen dargestellt und können ebenso Wunden absorbieren, wenn sie abgestrichen werden. 

Bei Boosts werden diese Herzen jedoch komplett wieder entfernt und können nicht durch Heilung wieder hergestellt werden. Ein Boost ist also eine zeitweise Verbesserung des Zustands.

Nimmt der Charakter Schaden, wird immer von rechts abgestrichen. Zunächst werden die Boosts verbraucht, danach die noch vollständigen Herzen. Bei folgender Anzeige ist der Boost also *nach* der Verwundung (die leeren Herzen) eingetreten.

<i class="fas fa-heart fa-2x text-danger"></i>
<i class="fas fa-heart fa-2x text-danger"></i>
<i class="fas fa-heart fa-2x text-danger"></i>
<i class="fas fa-heart fa-2x text-danger"></i>
<i class="fas fa-heart fa-2x text-danger"></i>
<i class="fas fa-heart fa-2x text-danger"></i>
<i class="fas fa-heart fa-2x text-danger"></i>
<i class="far fa-heart fa-2x text-danger"></i>
<i class="far fa-heart fa-2x text-danger"></i>
<i class="far fa-heart fa-2x text-danger"></i>
<i class="fas fa-heart fa-2x text-info"></i>

### Ohnmacht und Tod

Ein Charakter der weder volle Herzen noch Boosts hat, wird ohnmächtig und gilt als *sterbend*. Bei dem Zustand weiter unten wird beschrieben wie hier genau zu verfahren ist.

### Heilung

Es gibt unterschiedliche Arten der Heilung. Charaktere können durch Anwendung von *Erster Hilfe*, durch einen Zauber oder durch besondere Gegenstände mögliche Wunden zurückerhalten. *Erste Hilfe* heilt, wenn es mit passenden Utensilien wie Bandagen ausgeführt wird, die Hälfte der Erfolge des Wurfes (aufgerundet).

### Die Rast

Kommen die Charaktere zu einer Ruhepause von mindestens 6 Stunden, so gilt dies als *Rast*.

Bei einer Rast hat der Charakter die Möglichkeit Wunden zu heilen. Hierzu werden die Werte *Resistenz*, *Ausdauer* und *Willenskraft* addiert. Es werden Würfel entsprechend der Summe geworfen, für jeden Erfolg heilt der Charakter eine Wunde.

Alle *Bonuswürfel*, *Schicksalswürfel* und *Wiederholungswürfe* frischen auf, werden also auf das Maximum des Charakters gesetzt.

Boost verfällt bei der Rast, alle vorhandenen Boosts werden bei der Rast entfernt.

{% if world_book.identifier != "tirakan" %}
Wird die Magie Erweiterung verwendet, wirft der Charakter auf die Summe der Werte *Charme*, *Gewissenhaftigkeit* und *Willenskraft*. Für jeden Erfolg wird ein *Arkana* wiederhergestellt.
{% else %}
Der Charakter wirft zudem auf die Summe der Werte *Charme*, *Gewissenhaftigkeit* und *Willenskraft*. Für jeden Erfolg wird ein *Arkana* wiederhergestellt.
{% endif %}

{% if world_book.identifier != "tirakan" %}
Bei aktiver Horrorerweiterung wirft der Charakter einen *Stress Test*. Ist der Wurf gelungen, so kann der Stress um Eins reduziert werden.
{% endif %}

### Zustände

Ein Charakter kann verschiedene Zustände haben. Diese haben verschiedene Auswirkungen auf das Handeln des Charakters, aber auch Effekte über Zeit. Die Zustände werden auf dem Charakterbogen mit einem Zähler vermerkt.

Einige Zustände haben Rettungswürfe, mit denen sie entfernt werden können. Diese Würfe sind in der Beschreibung des Zustands angegeben. Alle Einschränkungen und Erschwerungen, die durch Zustände verursacht werden gelten nicht für diese Rettungswürfe.

#### Sterbend

Dieser Zustand wird verursacht, wenn die Wunden des Charakters die maximalen Wunden übersteigen, die Herzen also auf 0 sinken. In diesem Moment wird der Wert dieses Zustands auf 1 gesetzt.

Erhält ein Charakter den Zustand *Sterbend*, so werden alle anderen Zustände entfernt.

Ist der Wert des Zustands eins oder höher, so würfelt der Charakter zu Beginn jeder Runde auf seine *Resistenz*. Gelingt dieser Wurf, so passiert nichts. Misslingt dieser Wurf, so wird der Wert des Zustands um eins angehoben.

Erreicht der Wert des Zustands 6, so stirbt der Charakter.

Für das Stabilisieren sind Erfolge entsprechend dem "Sterbend" Wert des Charakters erforderlich. Hierbei kann es sich um einen Wurf auf Erste Hilfe, Medizin oder etwas ähnlich hilfreichem handeln. Sind genug Erfolge erreicht, wird der Zustand sterbend entfernt.

Wird ein Charakter mit dem Zustand *sterbend* angegriffen, wird der Wert *Sterbend* um die Anzahl der zugefügten Wunden erhöht (siehe [[chapter-combat|Der Kampf, Coup de grâce]]).


#### Bewusstlos

Der Character ist zu keiner Handlung fähig (seine *Aktionen* pro Runde sind null). Der Wert dieses Zustands zeigt die Tiefe der Bewusstlosigkeit an.

Zu Beginn jeder Runde kann der Charakter auf seine *Willenskraft* werfen. Zeigt der Wurf Erfolge entsprechend dem Wert dieses Zustands, so wird der Wert auf 0 gesetzt und der Charakter erwacht.

#### Geschockt

Der Charakter hat für jeden Wurf so viele Würfel weniger als der Wert dieses Zustands ist.

Zu Beginn jeder Runde kann der Charakter auf seine *Ausdauer* werfen. Er kann den Wert des Zustands um die Anzahl der Erfolge verringern. Erreicht der Zustand dabei einen Wert von 0, so wird er entfernt.

#### Brennend

Der Mindestwurf des Charakters ist für alle Würfe auf *Wahrnehmung* und für alle Angriffe um den Wert dieses Zustands erhöht.

Dieser Zustand endet, wenn der Charakter gelöscht wurde.

#### Blutend

Zu Beginn jeder Runde wirft der Charakter auf seine *Ausdauer*. Misslingt der Wurf, so nimmt der Charakter je eine Wunde für jede Stufe dieses Zustands hin.

Dieser Zustand endet, wenn der Charakter verbunden wurde (z.B. durch *Erste Hilfe*)

#### Vergiftet

Der Mindestwurf des Charakters ist für alle Würfe um den Wert dieses Zustands erhöht.

Zu Beginn jeder Runde kann der Charakter auf seine *Resistenz* werfen. Er kann den Wert des Zustands um die Anzahl der Erfolge verringern. Erreicht der Zustand dabei einen Wert von 0, so wird er entfernt.

#### In der Hocke

Der Charakter hat 6+ Deckung (siehe [[chapter-combat|Der Kampf]]).

Alle Aktionen, welche körperliches Handeln erfordern (Physis Attribute, Angriffe und Fähigkeiten) haben einen um +1 erhöhten Mindestwurf.

Es kostet eine Aktion, sich hinzulegen oder aufzustehen.
