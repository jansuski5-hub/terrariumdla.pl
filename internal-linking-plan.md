# Plan linkowania wewnętrznego: terrariumdla.pl

Lipiec 2026. Dotyczy wszystkich 209 zaplanowanych podstron (`priorytet-podstron.csv`) w 5 falach publikacji oraz strony głównej.

## Zasada podstawowa

Linkuj pierwszą sensowną wzmiankę każdej frazy lub bytu, który ma własną stronę na serwisie: nazwa gatunku z przewodnikiem, temat z poradnikiem, kategoria sprzętu ze stroną sprzętową, rodzina z hubem. Linkuj tylko jedno wystąpienie tego samego celu w treści jednej strony, chyba że strona jest na tyle długa, że drugi link pojawia się w osobnej sekcji i realnie pomaga czytelnikowi. Jeśli naturalne miejsce pierwszej wzmianki jest w zdaniu, które już ma link, albo dwa linki wylądowałyby zbyt blisko siebie, przejdź do kolejnej, lepiej rozstawionej wzmianki zamiast piętrzyć linki w jednym zdaniu. Zasada dotyczy całego serwisu: strony głównej, hubów rodzin, filarów gatunkowych, satelitów, poradników, stron sprzętu, wpisów blogowych i ramek „zobacz też”.

## Architektura, na której opiera się linkowanie

Struktura URL: rodzina / gatunek / temat, np. `/weze/waz-zbozowy/opis/`, `/weze/waz-zbozowy/cena/`, `/gekony/gekon-lamparci/terrarium/`. Wyjątki: strony identyfikacyjne dzikich gatunków (`/weze/dzikie-w-polsce/zaskroniec/`, `/weze/dzikie-w-polsce/padalec/`) i strony ogólne rodziny (`/weze/ogolne/terrarium/`).

Rodziny i liczba zaplanowanych podstron: węże (43), bezkręgowce (55), gekony (21), agamy (11), żółwie (10), kameleony (3), jaszczurki inne (7), płazy (7), sprzęt (15), rośliny (9), opieka uniwersalna i ogólna (26), karma (1), inne zwierzęta (1).

Każdy gatunek ma jeden filar (przewodnik) i kilka satelitów (cena, terrarium, odmiany, konkretna odmiana barwna). Filar musi istnieć, zanim opublikujesz satelitę tego gatunku; patrz `SITE_WORKFLOW.md`.

## Co liczy się jako okazja do linku

Fraza liczy się jako okazja do linku, gdy spełnione są trzy warunki:

1. Fraza nazywa lub opisuje istniejącą stronę na serwisie.
2. Link pomógłby czytelnikowi lepiej zrozumieć bieżący akapit.
3. Link da się umieścić bez tłoczenia innego linku w tym samym zdaniu lub krótkim akapicie.

### Słownik kotwic (przykłady, rozbudowuj przy każdej nowej podstronie)

| Wzmianka w treści | Cel linku |
|---|---|
| wąż zbożowy | `/weze/waz-zbozowy/opis/` |
| ile kosztuje wąż zbożowy | `/weze/waz-zbozowy/cena/` |
| pyton królewski | `/weze/pyton-krolewski/opis/` |
| ile kosztuje pyton królewski | `/weze/pyton-krolewski/cena/` |
| terrarium dla pytona królewskiego | `/weze/pyton-krolewski/terrarium/` |
| odmiany pytona królewskiego | `/weze/pyton-krolewski/odmiany/` |
| pyton tygrysi, Python molurus | `/weze/pyton-tygrysi/opis/` |
| ile kosztuje pyton tygrysi | `/weze/pyton-tygrysi/cena/` |
| terrarium dla pytona tygrysiego | `/weze/pyton-tygrysi/terrarium/` |
| odmiany pytona tygrysiego | `/weze/pyton-tygrysi/odmiany/` |
| boa dusiciel | `/weze/boa/opis/` |
| boa imperator, boa cesarski | `/weze/boa-imperator/opis/` |
| ile kosztuje boa imperator | `/weze/boa-imperator/cena/` |
| terrarium dla boa imperator | `/weze/boa-imperator/terrarium/` |
| odmiany boa imperator | `/weze/boa-imperator/odmiany/` |
| zaskroniec | `/weze/dzikie-w-polsce/zaskroniec/` |
| padalec | `/weze/dzikie-w-polsce/padalec/` |
| terrarium dla węża, jak urządzić terrarium dla węża | `/weze/ogolne/terrarium/` |
| gekon lamparci | `/gekony/gekon-lamparci/opis/` |
| terrarium dla gekona lamparciego | `/gekony/gekon-lamparci/terrarium/` |
| gekon orzęsiony | `/gekony/gekon-orzesiony/opis/` |
| agama brodata | `/agamy/agama-brodata/opis/` |
| kameleon jemeński | `/kameleony/kameleon-jemenski/opis/` |
| żółw lądowy | `/zolwie/zolw-ladowy/opis/` |
| żółw wodno-lądowy | `/zolwie/zolw-wodno-ladowy/opis/` |
| aksolotl | `/plazy/aksolotl/opis/` |
| aksolotl cena, ile kosztuje aksolotl | `/plazy/aksolotl/cena/` |
| salamandra plamista | `/plazy/salamandra/opis/` |
| traszka grzebieniasta | `/plazy/traszka/opis/` |
| rzekotka drzewna | `/plazy/rzekotka/opis/` |
| modliszka różowopręga, Sphodromantis lineola | `/modliszki/modliszka-rozowoprega/opis/` |
| modliszka storczykowa, modliszka orchideowa, Hymenopus coronatus | `/modliszki/modliszka-storczykowa/opis/` |
| modliszka chińska, Tenodera sinensis | `/modliszki/modliszka-chinska/opis/` |
| modliszka diabelska, Idolomantis diabolica | `/modliszki/modliszka-diabelska/opis/` |
| modliszka duch, modliszka liściogłowa, Phyllocrania paradoxa | `/modliszki/modliszka-duch/opis/` |
| ptasznik czerwonokolanowy, Brachypelma hamorii | `/ptaszniki/ptasznik-czerwonokolanowy/opis/` |
| ptasznik złotokolanowy, Chaco, Grammostola pulchripes | `/ptaszniki/ptasznik-zlotokolanowy/opis/` |
| ptasznik chilijski różowy, Grammostola rosea | `/ptaszniki/ptasznik-chilijski-rozowy/opis/` |
| ptasznik kędzierzawy, Tliltocatl albopilosum | `/ptaszniki/ptasznik-kedzierzawy/opis/` |
| ptasznik olbrzymi, LP, Lasiodora parahybana | `/ptaszniki/ptasznik-olbrzymi/opis/` |
| ptasznik GBB, Chromatopelma cyaneopubescens | `/ptaszniki/ptasznik-gbb/opis/` |
| Avicularia avicularia, pinktoe | `/ptaszniki/avicularia-avicularia/opis/` |
| ptasznik wielobarwny, Caribena versicolor | `/ptaszniki/ptasznik-wielobarwny/opis/` |
| ptasznik królewski indyjski, Poecilotheria regalis | `/ptaszniki/ptasznik-krolewski/opis/` |
| ptasznik goliat, Theraphosa blondi | `/ptaszniki/ptasznik-goliat/opis/` |
| patyczak, straszyk | `/bezkregowce/patyczak/opis/` |
| formikarium | `/bezkregowce/formikarium/opis/` |
| waran, waran z komodo | `/jaszczurki-inne/waran/jako-zwierze-domowe/` |
| jeż pigmejski | `/inne-zwierzeta/jez-pigmejski/opis/` |
| mata grzewcza | `/sprzet/mata-grzewcza/` |
| lampa grzewcza, oświetlenie terrarium | `/sprzet/oswietlenie/` |
| termostat, termometr | `/sprzet/termostat-termometr/` |
| wymiary terrarium | `/sprzet/wymiary-terrarium/` |
| gdzie kupić terrarium | `/sprzet/gdzie-kupic/` |
| legalność hodowli gada | `/opieka-uniwersalna/legalnosc-hodowli/` |
| kwarantanna nowego gada | `/opieka-uniwersalna/kwarantanna-nowego-gada/` |
| start w terrarystyce, jak zacząć | `/opieka-uniwersalna/start-w-terrarystyce/` |

Aktualizuj tę tabelę razem z każdą nową falą publikacji; nowy filar gatunku dopisujesz od razu, żeby kolejne podstrony mogły linkować do niego od pierwszego dnia.

## Zasady rozstawu linków

Użyj pierwszej sensownej wzmianki, potem przestań linkować ten sam cel na tej stronie, chyba że artykuł jest wystarczająco długi, by uzasadnić drugi link w osobnej sekcji.

1. Unikaj dwóch linków kontekstowych w jednym zdaniu.
2. Unikaj dwóch linków w sąsiadujących krótkich zdaniach, gdy wyglądają jak lista niebieskiego tekstu.
3. Jeśli pierwsza wzmianka jest w nagłówku, nagłówku tabeli, przycisku albo elemencie nawigacji, użyj kolejnej wzmianki w treści.
4. Jeśli jedyna wzmianka jest w gęstej tabeli porównawczej, linkuj ją tam i unikaj kolejnego linku do tego samego adresu bezpośrednio pod tabelą.
5. Jeśli akapit nazywa trzy powiązane pojęcia, linkuj najbardziej konkretne pierwsze. Wybierz `/weze/waz-zbozowy/opis/` zamiast ogólnej strony węży, gdy fraza dotyczy konkretnie węża zbożowego.
6. Używaj naturalnej kotwicy ze zdania. Nie dodawaj sztucznych fraz dokładnego dopasowania tylko po to, by wymusić link.

## Minimalna gęstość linków wewnętrznych wg typu strony

Progi na `<main>`, bez nawigacji i stopki.

| Typ strony | Minimum linków w treści | Uwagi |
|---|---:|---|
| Strona główna | 20+ | Link do każdego hubu rodziny, filarów gatunków startowych, sprzętu, poradników, bloga. |
| Hub rodziny (np. `/weze/index.html`) | 10–20 | Link do każdego gatunku w rodzinie, filarów i wybranych satelitów, powrót do strony głównej. |
| Filar gatunku (przewodnik) | 10–15 | Link do wszystkich satelitów tego gatunku, powiązanych gatunków, sprzętu, poradników ogólnych. |
| Satelita gatunku (cena, terrarium, odmiana) | 5–8 | Link do filaru, huba rodziny, sprzętu, 1–2 powiązanych satelitów. |
| Poradnik ogólny | 6–10 | Link do gatunków, których dotyczy poradnik, i do powiązanych poradników. |
| Strona sprzętu | 6–10 | Link do gatunków, dla których sprzęt jest istotny, i do innych stron sprzętu. |
| Wpis blogowy | 5–10 | Link do stron gatunkowych/sprzętowych, których dotyczy wpis. |

Próg to podłoga, nie sufit. Dłuższe strony mogą go przekraczać, gdy linki są rozłożone po sekcjach i każdy pomaga czytelnikowi zejść głębiej w serwis.

## Klastry

**Klaster rodziny.** Każdy hub rodziny (`/weze/index.html` itd.) linkuje do wszystkich swoich gatunków z opisowymi kotwicami. Każda strona gatunku linkuje z powrotem do huba swojej rodziny i do strony głównej.

**Klaster gatunku.** Filar linkuje do każdego swojego satelity przy pierwszej naturalnej okazji (np. sekcja o cenie linkuje do `/gatunek/cena/`, jeśli nie jest już wyczerpana w tym samym akapicie). Satelity linkują z powrotem do filaru w pierwszym zdaniu, które nazywa gatunek.

**Klaster sprzętu.** `/sprzet/index.html` linkuje do wszystkich 15 podstron sprzętowych. Każda strona gatunku linkuje do przynajmniej jednej strony sprzętu w sekcji „czego potrzebujesz” (standing rule w `SITE_WORKFLOW.md`). Strony sprzętu linkują z powrotem do gatunków, dla których dany sprzęt jest szczególnie istotny.

**Klaster opieki uniwersalnej.** `/opieka-uniwersalna/index.html` linkuje do wszystkich poradników ogólnych. Poradniki linkują do gatunków, których dotyczą (np. `/opieka-uniwersalna/kwarantanna-nowego-gada/` linkuje do kilku filarów gatunkowych jako przykłady).

**Dzikie gatunki (zaskroniec, padalec).** To ruch identyfikacyjny: ktoś zobaczył węża w ogrodzie i sprawdza, czy to zagrożenie. Każda taka strona linkuje do `/weze/ogolne/terrarium/` i do filarów gatunków hodowlanych („nie ten wąż w ogrodzie? sprawdź hodowlane gatunki jak wąż zbożowy”), żeby przekierować zasięg identyfikacyjny w stronę treści hodowlanych.

## Publikacja: checklista dla każdej nowej lub edytowanej podstrony

1. Sprawdź szkic względem słownika kotwic wyżej. Linkuj pierwszą sensowną wzmiankę każdej frazy pasującej do istniejącej strony. Pomiń powtórzone wzmianki tego samego celu, chyba że kolejna jest w osobnej sekcji i coś wnosi.
2. Jeśli naturalne miejsce pierwszej wzmianki już ma link w pobliżu, albo dwa linki wylądowałyby w jednym zdaniu, przejdź do kolejnej wzmianki.
3. Zamień ogólnikową ramkę „zobacz też” na dwa-trzy linki specyficzne dla tej strony: hub rodziny lub filar, jeden pokrewny gatunek, jedna strona sprzętu lub poradnika.
4. Gdy dwa gatunki z tej samej rodziny mają już oba filary, dodaj między nimi wzajemny link w naturalnym zdaniu porównującym, nie tylko w ramce „zobacz też”.
5. Uruchom `python3 scripts/link_audit.py <ścieżka-do-nowej-strony>` przed commitem. To twarda brama: kończy się kodem 1, jeśli strona ma za mało linków w treści albo zawiera martwy link wewnętrzny.
6. Sprawdź balans tagów i to, że strona jest wpięta w `index.html` swojej rodziny i w `sitemap.xml`; patrz `SITE_WORKFLOW.md`.

## Bieżący stan

Serwis jest na starcie: opublikowany jest wyłącznie szkielet strony głównej z treścią placeholder. Zero podstron gatunkowych, zero hubów rodzin poza wpisami w nawigacji i stopce. Ten plan obowiązuje od pierwszej opublikowanej podstrony fali 1; nie czekaj z jego stosowaniem do „później”, bo naprawianie linkowania wstecz na 209 stronach jest droższe niż robienie tego dobrze od pierwszej strony.

Gdy powstaną pierwsze huby rodzin i filary, zaktualizuj słownik kotwic powyżej i odnotuj w `SITE_WORKFLOW.md`, które strony przeszły audyt `link_audit.py`.

**Rozbieżność znaleziona 2026-08-16 (sesja 25):** nawigacja i stopka na żywym repo mają `modliszki`, `ptaszniki`, `skorpiony`, `zaby` jako osobne rodziny najwyższego poziomu (własne katalogi w root repo, własne wpisy w nav), nie jako podkatalogi `bezkregowce`/`plazy`, jak zakładał ten dokument przy pierwszym spisaniu. Katalog `bezkregowce/` w repo zawiera tylko `.gitkeep`, bez `index.html` i bez wpisu w nav. Wpisy dla `patyczak`, `formikarium` w tabeli wyżej mogą być z tego samego powodu nieaktualne, nie zweryfikowane (poza zakresem tej sesji, dotyczy tylko bezkręgowców innych niż ptaszniki).

**Poprawione 2026-08-16 (sesja 26):** wpis `ptasznik | /bezkregowce/ptasznik/opis/` był nieaktualny z tego samego powodu (rodzina `ptaszniki/` istnieje jako osobny katalog najwyższego poziomu, nie podkatalog `bezkregowce/`), zastąpiony 10 realnymi wpisami pod `/ptaszniki/`, po napisaniu pierwszych 10 filarów gatunkowych tej rodziny (wcześniej `ptaszniki/index.html` był samym hubem bez żadnej podstrony gatunkowej).
