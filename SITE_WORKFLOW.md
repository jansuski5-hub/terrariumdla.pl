# Site Workflow: terrariumdla.pl

Przeczytaj ten plik w całości przed jakąkolwiek pracą w tym repozytorium. Zastępuje odtwarzanie kontekstu z historii czatu; sesje w tym projekcie się resetują, więc ten plik jest trwałą pamięcią między sesjami.

## Kolejność czytania na starcie nowej sesji

1. Ten plik (`SITE_WORKFLOW.md`).
2. `CLAUDE.md`: zasady pisania (twarde zakazy w skillu `no-ai-slop`), obowiązkowe.
3. `internal-linking-plan.md`: polityka linkowania i tabela progów.
4. Sekcja „Bieżący status” na dole tego pliku; tu kończy się poprzednia sesja.

Nie ufaj wpisowi „gotowe” z poprzedniej sesji bez weryfikacji. Sprawdzaj samodzielnie skryptem i wzrokiem; strona bez obrazów albo z martwym linkiem `<img src>` przejdzie przez `link_audit.py` bez ostrzeżenia, bo skrypt sprawdza tylko `<a href>`, nie `<img src>`.

## Standing rules (dotyczą każdej podstrony, każdej sesji)

- **Próg linków w `<main>`**, sprawdzany przez `python3 scripts/link_audit.py`. Progi per typ strony są w `internal-linking-plan.md`.
- **Ramka „zobacz też”: maksymalnie 5, celuj w 4.** Priorytet mają linki kontekstowe w treści nad upychaniem w ramce. Jeśli link w treści i w ramce prowadzą do tego samego adresu, usuń duplikat z ramki, nie zostawiaj obu.
- **Linki w treści: kotwica dopasowana dokładnie albo częściowo do frazy, priorytet nad kotwicą ogólnikową.** Drobna przeróbka zdania pod naturalną kotwicę jest w porządku, jeśli nie psuje sensu zdania czy akapitu.
- **Żadnych niepodpartych statystyk ani zmyślonych faktów**; każda liczba, data, przypisanie musi prowadzić do realnego źródła (zasady 2, 18, 19 w `.claude/skills/no-ai-slop/SKILL.md`).
- **Każda nowa podstrona potrzebuje prawdziwych obrazów.** `link_audit.py` nie sprawdza `<img src>`; zweryfikuj ręcznie, że plik istnieje i renderuje się poprawnie. Styl SVG do zachowania: tło `#16181A`, panel `#1E2023`, akcent miętowy `#98FB98`, akcent szmaragdowy `#50C878`, tekst `#E8EAE6`; patrz `assets/img/favicon.svg` jako punkt odniesienia dla palety.
- **Nowe podstrony muszą być wpięte**: w `index.html` swojej rodziny (np. nowa strona w `/weze/waz-zbozowy/` wpięta w `/weze/index.html`) oraz w `sitemap.xml`.
- **Nawigacja i stopka są kopiowane ręcznie do każdej strony** (brak systemu includes; statyczny HTML bez build procesu). Przy zmianie menu w `template.html` trzeba ręcznie zaktualizować już opublikowane strony albo zaakceptować rozjazd do czasu, aż powstanie skrypt sczytujący współdzielone bloki. To otwarty dług techniczny; nie udawaj, że jest rozwiązany.
- **BLUF na stronach porównawczych/rankingowych** (np. przyszła strona „ranking terrariów 60x40x40”): tabela porównawcza od razu po wstępie, przed metodologią czy kryteriami oceny. Czytelnik dostaje odpowiedź (co kupić, w jakiej kolejności) zanim dostanie uzasadnienie.
- **Każda podstrona gatunkowa kończy się sekcją „czego potrzebujesz”** z linkami do `/sprzet/`; most do przyszłego sklepu na subdomenie.
- **Tabele porównawcze: `<div class="table-wrap">` wokół `<table class="compare-table">`.** Bez tego opakowania tabela nie dostaje przewijania poziomego na wąskich ekranach i może rozjechać layout.
- **Filar gatunku (przewodnik) musi istnieć, zanim opublikujesz satelitę tego gatunku.** Publikowanie „wąż zbożowy niebieski” przed „wąż zbożowy: przewodnik” zostawia stronę bez kontekstu do linkowania. Zasada z `priorytety-kolejnosc-publikacji.md`: nie zaczynaj nowego gatunku, dopóki poprzedni nie ma filaru plus co najmniej czterech satelitów.
- **H1 nigdy nie jest animowany.** Animacja CSS „terrarium dla X” żyje tylko w podtytule strony głównej (`.hero-tagline .rotator-list`), nie w H1; inaczej Google widzi tylko pierwsze słowo z listy.

## Pełny workflow pisania/poprawiania podstrony

1. Skopiuj `template.html` do właściwej ścieżki (`/rodzina/gatunek/temat/index.html` albo płaski plik, zależnie od wzorca już przyjętego w danej rodzinie). Uzupełnij `<title>`, meta description, canonical, breadcrumbs.
2. Napisz treść zgodnie z `.claude/skills/no-ai-slop/SKILL.md`: samosprawdzenie względem `references/ai-writing-detection.md` przed przejściem dalej.
3. Dodaj linki wewnętrzne wg `internal-linking-plan.md`: pierwsza sensowna wzmianka każdej frazy, która ma swoją stronę na serwisie, dostaje link. Bez duplikatów tego samego celu w treści i w ramce „zobacz też”.
4. Dodaj prawdziwe obrazy (SVG w stylu strony albo zdjęcie z podpisem źródła). Sprawdź ręcznie, że się renderują.
5. Wepnij stronę w `index.html` rodziny i w `sitemap.xml`.
6. Uruchom `python3 scripts/link_audit.py <ścieżka-do-pliku>`: 0 błędów, brak martwych linków wewnętrznych.
7. Sprawdź balans tagów (otwarcie/zamknięcie `<div>`, `<section>`, `<table>` itd.); ręcznie albo krótkim skryptem, tak jak przy audycie szkieletu technicznego.
8. Ostatni krok zawsze: pełne, świeże odczytanie tekstu pod kątem banned-words z `.claude/skills/no-ai-slop/references/ai-writing-detection.md`. Redagowanie w trakcie pisania łatwo wprowadza nowe naruszenia (np. wzmacniacz dodany przy poprawianiu zdania); sprawdzenie na końcu, nie tylko na starcie, jest obowiązkowe.

## Enforcement: brama linkowa

`scripts/link_audit.py` liczy `<a href>` wewnątrz `<main>`, pomijając breadcrumbs, nagłówek i stopkę, i sprawdza, czy każdy wewnętrzny href prowadzi do istniejącego pliku lub katalogu z `index.html`. Kod wyjścia 1 oznacza, że coś trzeba poprawić przed commitem.

```
python3 scripts/link_audit.py weze/waz-zbozowy/przewodnik/index.html   # jeden plik
python3 scripts/link_audit.py weze gekony                              # jeden lub więcej katalogów
python3 scripts/link_audit.py                                          # cała strona
```

Flaga `--strict` sprawdza pełną tabelę progów per archetyp z `internal-linking-plan.md` (strona główna, filar, satelita, hub rodziny, poradnik) zamiast płaskiego minimum. Tryb strict jest informacyjny; sposób na znalezienie stron wartych wzmocnienia, nie twarda brama, dopóki większość serwisu nie osiągnie tych progów naturalnie (na starcie projektu prawie wszystkie strony będą poniżej `--strict`, to oczekiwane).

## Bieżący status

_Ostatnia aktualizacja: 2026-08-07 (sesja 11)_

**Zrobione (ta sesja; kafelek gatunku na hubie węży):**
- Dodano na `/weze/index.html` sekcję „Gatunki" z pierwszym kafelkiem gatunkowym: zdjęcie `assets/img/podkategoriaimperator.jpg` (dodane wcześniej przez Wojciecha do repo, 512x341) w zielonej ramce (`border: 3px solid var(--emerald)`), podpis „Boa imperator (Boa cesarski)" pod zdjęciem, cały kafelek klikalny do `/weze/boa-imperator/przewodnik/`.
- Nowy komponent CSS `.species-tiles`/`.species-tile` w `style.css` (flex-wrap, żeby kolejne gatunki dało się dokładać obok), hover zmienia ramkę na miętowy akcent, spójny ze wzorcem `.cat`/`.post` reszty strony.
- Dopisano wpis do słownika kotwic w `internal-linking-plan.md`: „boa imperator, boa cesarski” → `/weze/boa-imperator/przewodnik/`.
- **Otwarte, ważne**: strona `/weze/boa-imperator/przewodnik/` (filar gatunku) jeszcze nie istnieje, więc kafelek to na razie martwy link wewnętrzny, potwierdzone przez `link_audit.py`. To spójne z resztą serwisu (te same dead linki do `/blog/` i `/opieka-uniwersalna/` widoczne od poprzednich sesji), ale ten konkretny link trzeba domknąć, zanim strona pójdzie na żywo: napisać filar boa imperator zgodnie z zasadą „filar przed satelitą” z `SITE_WORKFLOW.md`.
- Zweryfikowano: `python3 scripts/link_audit.py weze/index.html` (6/5 linków, próg przechodzi; 4 martwe linki wewnętrzne wypisane, wszystkie do stron jeszcze nienapisanych), balans tagów (`div`/`section`/`main`/`header`/`footer`/`article`/`a`/`nav`/`ul`, wszystkie pary równe).

_Ostatnia aktualizacja: 2026-07-30 (sesja 10)_

**Zrobione (ta sesja; poprawka layoutu stopki + czyszczenie nav headera):**
- **Naprawiono zepsuty layout kolumny "Zwierzęta" w stopce**, zgłoszony przez Wojciecha na screenie jako wizualnie oderwany od nagłówka i przesunięty w prawo. Przyczyna: `.fcols` miało tor gridowy `1.3fr` dla tej kolumny (zamiast `1fr` jak reszta), a `.fanimals` miało `justify-content: center`, co centrowało wąski blok dwóch podkolumn wewnątrz sztucznie poszerzonego toru, tworząc odstęp od lewostronnego nagłówka "Zwierzęta" nad nim. Fix: tor z powrotem na `1fr`, `justify-content: center` usunięte z `.fanimals` (teraz `display:flex; gap:24px;` bez centrowania) — dwie podkolumny siedzą teraz przy lewej krawędzi, bezpośrednio pod nagłówkiem, spójnie z kolumnami Opieka/Serwis.
- **Usunięto Kameleony, Żółwie i Opiekę z nawigacji w headerze** na wyraźne życzenie Wojciecha ("nie mam zamiaru pisac" o kameleonach/żółwiach; Opieka też ma zniknąć z tego miejsca). Zmiana objęła `<nav><ul>` we wszystkich 11 plikach HTML (`index.html`, `template.html` i 9 stron rodzinnych). Nav teraz: Blog, Węże, Gekony, Agamy, Ptaszniki, Skorpiony, Modliszki, Żaby — dokładnie lista, którą Wojciech podał wcześniej dla rotatora/tekstu wprowadzającego, teraz spójna też w headerze.
- **Ważne rozróżnienie**: kolumna "Opieka" w stopce (z podlinkami zdrowie/karmienie/terrarium/rozpoznanie-płci/zimowanie) NIE została ruszona — instrukcja "Opieki tez nie ma tam byc" odczytana jako dotycząca wyłącznie nav headera (to samo zdanie co "z headingu"), nie szczegółowej sekcji stopki. Jeśli to złe zrozumienie, trzeba to jeszcze poprawić.
- **Pliki `kameleony/index.html` i `zolwie/index.html` zostają na dysku**, tylko odpięte z nav i ze stopki; dalej dostępne pod bezpośrednim URL i wpięte w `sitemap.xml`. Nie usunięto ich, bo nie było wyraźnej prośby o usunięcie, a sandbox i tak nie potrafi trwale kasować plików.
- Zweryfikowano: brak Kameleony/Żółwie/Opieka w żadnym bloku `<nav>` (sprawdzone `awk`+`grep` na wszystkich 11 plikach), balans `<nav>`/`</nav>` bez zmian, `link_audit.py` bez nowych regresji (nav jest wykluczony z audytu `<main>`, więc liczby linków identyczne jak w sesji 9; martwe linki to nadal tylko jeszcze nienapisane `/blog/...` i `/opieka-uniwersalna/...`, spójne z resztą serwisu).

_Ostatnia aktualizacja: 2026-07-30 (sesja 9)_

**Zrobione (ta sesja; wszystkie rodziny maja teraz realny hub, wieksze fonty, stopka):**
- **Cala Fala 1 rodzinna ma teraz prawdziwa strone hub**: dopisano `weze/`, `gekony/`, `agamy/`, `kameleony/`, `zolwie/index.html` (wczesniej tylko `.gitkeep`), tym samym stylem co `ptaszniki/skorpiony/modliszki/zaby` z sesji 8: ogolne, sprawdzalne fakty hodowlane bez zmyslonych statystyk, zgodnie z `no-ai-slop`. Wszystkie 9 rodzin ma teraz min. 5/5 linkow w `<main>`, jedyne martwe linki to `/blog/...` i `/opieka-uniwersalna/...`, ktore same jeszcze nie istnieja (spojne z reszta serwisu).
- **Wojciech zglosil, ze tekst na desktopie wyglada za malo** (blog, FAQ, stopka). Powod: `--maxw` zostal poszerzony w sesji 6 (1180->1720px) pod inny layout hero, ale rozmiary fontow tresci zostaly ze starego, waskiego projektu. Zwiekszono: body 16->18px, `.post h3` 16->19px, `.post p` 13.5->15.5px, `.faq summary` 15->18px, `.faq details p` 14.5->16.5px, `footer li a` 14->15.5px, `.sec-head p` 15->17px, `.fabout p` 14->15.5px.
- **Stopka**: kolumna "Gatunki" zmieniona na "Zwierzeta" (Wojciech: "to nie sa gatunki"), rozbita na dwie podkolumny (`.fanimals`, flex + `justify-content:center`) z 7 pozycjami: Weze/Agamy/Gekony/Ptaszniki w pierwszej, Skorpiony/Modliszki/Zaby w drugiej. Kameleony i Zolwie usuniete z tej sekcji stopki (zostaja w nav headera, tam ich nie ruszano, bo nie bylo o to prosby).
- **Diagnostyka rotatora "terrarium dla X"**: Wojciech zglosil w incognito natychmiastowy widok "Ciebie" zamiast animacji od poczatku listy. To najprawdopodobniej NIE jest blad: sekwencyjna animacja (sesja 8) konczy sie na stale po ok. 14.4s i zostaje na "Ciebie" przez `animation-fill-mode: both`. Jesli od zaladowania strony do spojrzenia minelo wiecej niz ~15s (bardzo latwe przy przelaczaniu kart/screenshotach), user zobaczy wylacznie stan koncowy, poprawny z zalozenia. Nie da sie tego potwierdzic bez realnej przegladarki w tym sandboxie; jesli Wojciech obejrzy strone od pierwszej sekundy po twardym odswiezeniu i nadal nie zobaczy przejscia miedzy slowami, dopiero wtedy to realny blad CSS do dalszej diagnozy.
- Dodano `?v=8` do linku `style.css` na kazdej stronie (cache-busting), na wypadek buforowania niezaleznego od cache przegladarki (serwer/CDN po stronie hostingu).
- `sitemap.xml` rozszerzony o 5 nowych URLi (`weze/gekony/agamy/kameleony/zolwie`), priorytet 0.8 (wyzszy niz nowe rodziny bezkregowe/plazie, bo to filary z wiekszym wolumenem w `plan-podstron.csv`).
- Zweryfikowano: `link_audit.py` na wszystkich 9 rodzin + homepage (kazda >=5/5 linkow), brak pauzy i kontrastu negacyjnego, brak zabronionych slow z `ai-writing-detection.md` (spot-check), balans tagow we wszystkich nowych plikach. Zlapano i poprawiono przy pisaniu: 3 naruszenia zasady 25 w `agamy/index.html`, przypadkowe cyrylickie „языком” w `kameleony/index.html` (literowka, poprawiono na „językiem”), 1 zabronione slowo „kluczowy” w `zolwie/index.html`.

_Ostatnia aktualizacja: 2026-07-30 (sesja 8)_

**Zrobione (ta sesja; nowa taksonomia + header + rotator + pierwsze prawdziwe podstrony rodzinne):**
- **Zmiana taksonomii na wyraźne życzenie Wojciecha**: „Bezkręgowce” jako parasol zniknęło z nav/stopki. Zamiast tego cztery nowe rodziny na tym samym poziomie co węże/gekony/agamy: `/ptaszniki/`, `/skorpiony/`, `/modliszki/`, `/zaby/`, każda z prawdziwą stroną hub (skopiowaną z `template.html`, treść pisana od zera zgodnie z `no-ai-slop`, bez zmyślonych statystyk, tylko ogólnie znane, sprawdzalne fakty hodowlane). To odchodzi od zagnieżdżenia `/bezkregowce/ptasznik/...` z `plan-podstron.csv`; oryginalny plik planistyczny nie ma wpisów dla skorpionów ani żab w ogóle, więc nie było tu konfliktu z realnymi danymi Ahrefs, tylko z wcześniejszym zagnieżdżeniem katalogów.
- Header (pasek nawigacji) powiększony ok. 3x: wysokość, logo, linki nav, pole wyszukiwania, ikona logo-mark. Osobny override na `max-width: 900px` sprowadza rozmiary do użytecznych na mobile.
- Rotator w hero przebudowany po raz trzeci: teraz pełna lista 7 słów (węża, agamy, gekona, ptasznika, skorpiona, modliszki, żaby) przechodzi jednorazowo, sekwencyjnie (nie w pętli), i ląduje na „Ciebie” na stałe (`animation-fill-mode: both`, jedno przejście na słowo, bez `iteration-count: infinite`). Poprzednie dwie wersje (nieskończona pętla 9 słów z ujemnym `animation-delay`, potem uproszczona wersja 2-słowna) Wojciech zgłaszał jako „nadal się nie zmienia” mimo wyczyszczenia cache przeglądarki.
- **Zdiagnozowano, że to prawdopodobnie nie jest kwestia CSS**: `git status` pokazuje, że lokalne commity były w pełni zsynchronizowane z `origin/main` w momencie zgłoszenia problemu, a Wojciech potwierdził wyczyszczenie cache przeglądarki. Sandbox nie ma dostępu do sieci, więc nie da się sprawdzić logów GitHub Actions ani realnej odpowiedzi serwera. **Otwarte pytanie do Wojciecha**: sprawdzić zakładkę Actions w repo na GitHubie, czy ostatnie joby deploy (FTPS) faktycznie kończą się sukcesem (zielony check), zanim dalej debianuje się CSS, które lokalnie wygląda poprawnie za każdym razem.
- Tekst wprowadzający pod hero zaktualizowany: linki do węży/agam/gekonów/ptaszników/skorpionów/modliszek/żab wskazują teraz na nowe, realne URL-e zamiast na `/bezkregowce/`.
- `sitemap.xml` rozszerzony o 4 nowe strony. Poprawiono przy okazji pauzę (—) w komentarzu XML.
- Zweryfikowano: balans tagów w 4 nowych plikach i w `template.html`/`index.html`, `link_audit.py` na nowych stronach (5/5 linków każda, martwe linki to wyłącznie `/blog/...` i inne jeszcze nienapisane rodziny, spójne z resztą serwisu), brak pauzy i kontrastu negacyjnego we własnej nowej prozie.
- **Otwarte**: katalog `bezkregowce/.gitkeep` zostaje pusty w repo (nie da się go usunąć w tym sandboxie, rename/mv działa, unlink nie); nieszkodliwe, ale można kiedyś posprzątać ręcznie z komputera. Strony hub dla ptaszniki/skorpiony/modliszki/zaby są startowe, bez zdjęć i bez podstron gatunkowych (satelitów); kolejny krok to realne zdjęcia i pierwsze podstrony gatunkowe w tych rodzinach, zgodnie z zasadą „filar przed satelitą”.

_Ostatnia aktualizacja: 2026-07-30 (sesja 7)_

**Zrobione (ta sesja; ikony kategorii, iteracje hero-boxu, potem duża przebudowa homepage):**
- Zaprojektowano 9 własnych ikon SVG (linia, mięta/szmaragd) dla kart „Gatunki według grupy” zamiast emoji: węże, gekony, agamy, kameleony, żółwie, bezkręgowce, płazy, opieka uniwersalna, blog. Zweryfikowane wizualnie przez render SVG→PNG (`convert`).
- Kilka iteracji rozmiaru/pozycji `.hero-box` (powiększenie, przesunięcie w lewo, kształt kwadratu, odstępy) i `.hero-cta` (przezroczysty przycisk z animowaną linią-wężem na hover); **wszystkie te elementy zostały później usunięte** w tej samej sesji, patrz niżej. Historia zostaje w git, nie trzeba jej odtwarzać.
- **Duża przebudowa struktury strony głównej na wyraźne życzenie Wojciecha**: nowy układ to Header → zdjęcie hero z rotującym logotypem „Terrarium dla [gekona / węża / ptasznika / agamy / kameleona / żółwia / skorpiona / płaza / Ciebie]” (czysty CSS, `@keyframes` + `animation-delay` per słowo, bez JS, z `prefers-reduced-motion`) → krótki tekst wprowadzający pod zdjęciem (dostarczony przez Wojciecha, wklejony niemal dosłownie, dodane tylko linki wewnętrzne do węży/agam/gekonów/bezkręgowców/bloga żeby domknąć próg linkowy) → „Z bloga” → FAQ skrócone z 12 do 5 pytań (start dla początkujących, materiał na terrarium, koszt, definicja terrarystyki, terrarium vs akwarium) → Footer.
- **Usunięto z homepage**: sekcje „Gatunki według grupy” (siatka `.cats`, w tym nowe ikony z tej samej sesji), „Rodzaje terrariów”, „Wyposażenie terrarium”, „Jakie zwierzęta trzyma się w terrarium”, „Kilka liczb o gatunkach”, „Coś jest nie tak ze zwierzakiem?”. CSS tych komponentów (`.cats`/`.cat`, `.mini-grid`/`.mini-card`, `.grid`/`.callout`, `.probs`/`.prob`) zostało w `style.css` nietknięte, do ewentualnego użycia na stronach hubów rodzin w przyszłości; nieużywane teraz na homepage, ale nie martwy kod w sensie architektury komponentów.
- **Dodano własne fonty** (folder źródłowy `Fonts/` w repo, wdrożone pliki w `assets/fonts/`): Karla (wariable, body/`--font: Karla`), Fragment Mono (akcenty: `.tag`, `.count`, `.callout-label`, `.post .meta`, `.btn`, słowo w rotatorze), Recoleta (nagłówki, h1-h4 i `.sec-head h2`). `@font-face` w `style.css`, `font-display: swap`.
- **Aktualizacja tej samej sesji**: Wojciech zamienił Recoletę na Fraunces do nagłówków (font dostarczony w `Fonts/Fraunces/`, wariable, z plikiem `OFL.txt`, w porządku do użycia komercyjnego). Usunięto `Recoleta-RegularDEMO.otf` z repo (i z `assets/fonts/`), dodano `.gitignore`. Wątpliwość licencyjna z wcześniejszego wpisu jest nieaktualna, Fraunces ma pełną licencję OFL.
- Zweryfikowano: balans tagów, brace/parens w `style.css` (163/163, 167/167), `link_audit.py index.html` (9/5 linków po dodaniu linków w tekście wprowadzającym, martwe linki to wyłącznie strony jeszcze nienapisane), brak em-dash (—) we własnej prozie (tekst od Wojciecha zawiera en-dash – to jego oryginalny tekst, wklejony bez zmian).
- Odkryto kolejny commit Wojciecha spoza tej sesji: `0222fe5 "Wymuszenie https bez www przez .htaccess"`, już na `origin/main`.

_Ostatnia aktualizacja: 2026-07-29 (sesja 6)_

**Zrobione (ta sesja; wymuszenie kanonicznego adresu):**
- Dodano `.htaccess` (root) z regułą `mod_rewrite`: każde żądanie po `http://` albo z `www.` (w dowolnej kombinacji) dostaje 301 na `https://terrariumdla.pl%{REQUEST_URI}`. Jedna reguła z `[OR]` obsługuje oba przypadki naraz.
- Zweryfikowano, że `.htaccess` nie trafia na listę `exclude` w `.github/workflows/deploy.yml` (wzorzec `**/.git*` łapie `.git`/`.gitattributes`/`.gitkeep`, nie `.htaccess`), więc plik pojedzie na serwer przy najbliższym pushu.
- `<link rel="canonical">` w `index.html` już wskazywał `https://terrariumdla.pl/` (bez www) od wcześniej; ta zmiana dodaje wymuszenie po stronie serwera, nie tylko deklarację.
- **Nie zweryfikowano na żywym serwerze** (sandbox bez dostępu do produkcyjnego cPanel/DNS): po wypchnięciu commitu i wdrożeniu warto ręcznie sprawdzić `http://terrariumdla.pl`, `https://www.terrariumdla.pl`, `http://www.terrariumdla.pl` w przeglądarce albo `curl -I`, żeby potwierdzić 301 na czystą wersję https bez www.

_Ostatnia aktualizacja: 2026-07-28 (sesja 5)_

**Zrobione (ta sesja; poprawki UX po feedbacku Wojciecha na screenie homepage):**
- Favicon skorygowany do v3: Wojciech sprecyzował, że wersja z sesji 4 (pełna głowa węża) poszła za daleko; miał zostać oryginalny łuk z sesji 1, tylko kropka zamieniona na rozwidlony język. Poprawiono `assets/img/favicon.svg` zgodnie z tym, zweryfikowano wizualnie (SVG→PNG przez `convert` + librsvg).
- Trzy sekcje z sesji 4 („Rodzaje terrariów”, „Wyposażenie terrarium”, „Jakie zwierzęta trzyma się w terrarium”) zgłoszone jako ściana tekstu; skrócone i przebudowane na siatki kart (`.mini-grid`/`.mini-card`, nowy komponent w `style.css`: karta z ikoną emoji, nagłówkiem, jednym krótkim zdaniem). Wojciech jawnie zniósł priorytet pełnego pokrycia słów kluczowych Surfera na rzecz czytelności („Surfer nie musi być idealny, ważne żeby nie straszyło ścianą treści”); pokrycie fraz z sesji 4 spadło w tych trzech sekcjach, to świadomy kompromis.
- Samosprawdzenie: złapano i poprawiono 1 pauzę (—) w komentarzu `style.css` i 1 nawrót konstrukcji negacyjnej („nie od gatunku”) w nowym zdaniu wstępu do „Rodzaje terrariów”.
- Zweryfikowano: balans tagów (`section`/`div`/`main`/`header`/`footer`, wszystkie pary równe), `link_audit.py index.html` (21/5 linków, martwe linki to wyłącznie strony jeszcze nienapisane, zgodnie ze stanem repo).
- Commit `1e79c05`.

**Następne / otwarte (przeniesione z sesji 4, nadal aktualne):**
- Zero opublikowanych podstron treściowych poza `index.html`. Fala 1 (filary gatunków) jeszcze nie napisana.
- Rozważyć, czy inne sekcje homepage (poza trzema poprawionymi) też warto przerobić na format kartowy zamiast prozy, jeśli Wojciech uzna to za spójniejsze.

_Ostatnia aktualizacja: 2026-07-28 (sesja 4)_

**Zrobione (ta sesja; SEO homepage wg briefu Surfera):**
- Nowy hero: zdjęcie węża boa (`assets/img/pexels-botanphotography-29378239.jpg`, dodane przez Wojciecha bezpośrednio do repo) na całą szerokość, nagłówek „Cześć, jestem Wojtek” + opis w półprzezroczystym boxie (`.hero-box`, `rgba(30,32,35,.74)` + blur), przycisk „Przeczytaj, jak zaczynałem” obok. Usunięto stary `.hero-grid` i kartę `.picker` (element po prawej).
- Usunięto sekcję „Porównanie gatunków dla początkujących” (tabela porównawcza) i zdublowaną sekcję „Cześć, jestem Wojtek” z dołu strony (treść przeniesiona do hero).
- Nowy favicon: głowa węża z rozwidlonym językiem zamiast kropki (`assets/img/favicon.svg`), zweryfikowany wizualnie przez konwersję SVG→PNG (`convert` + librsvg w sandboxie). Ta sama ikona jako `.logo-mark` w prawym rogu headera, obok pola wyszukiwania.
- Zoptymalizowano treść strony głównej pod `surfer-guidelines-terrarium-28-07-2026.txt` (80 fraz kluczowych z zadanym zakresem wystąpień + 12 pytań FAQ). Dodano nowe sekcje: „Rodzaje terrariów”, „Wyposażenie terrarium”, „Jakie zwierzęta trzyma się w terrarium”, „Kilka liczb o gatunkach” (callouty z faktami od Wojciecha: długości gatunków, wymiary terrarium, wilgotność, temperatura), oraz FAQ (`<details>/<summary>`, 12 pytań z briefu, bez windowania liczby nagłówków bo `<summary>` nie jest tagiem nagłówkowym).
- Policzono pokrycie skryptem (regex + zliczanie substring case-insensitive na tekście, alt, title, meta description): wynik końcowy 80/80 fraz z co najmniej jednym wystąpieniem, 57/80 z pełnym minimum z briefu. Nie dobijano do górnych/wysokich progów (np. „ptaszników” min 15, „zwierzęta” min 11) celowo, żeby nie przejść w keyword stuffing; Wojciech potwierdził, że strona nie musi mieć ~2000 słów z briefu.
- Samosprawdzenie własnej nowej prozy: złapano i poprawiono kilka świeżo wprowadzonych naruszeń zasady 25 (kontrast negacyjny, „nie tylko X, to Y” itp.) przed commitem, nie po.
- Zweryfikowano: balans tagów (`html/head/body/header/main/footer/section/article/nav/div/table/thead/tbody/tr/td/th/ul/li/details/summary/strong`), `html.parser` bez błędów, `link_audit.py index.html` (21/5 linków, wszystkie martwe linki to strony jeszcze nienapisane, zgodnie z rzeczywistym stanem repo), balans klamer w `style.css` (133/133).
- **Odkryto commit Wojciecha spoza tej sesji**: `7f64869 "ds"` (dodanie zdjęcia węża do `assets/img/`), już wypchnięty na `origin/main` zanim ta sesja się zaczęła. Nasz commit `b387e0e` jest na tym oparty.

_Ostatnia aktualizacja: 2026-07-28 (sesja 3)_

**Zrobione (ta sesja; restyling homepage + zmiana fazy):**
- Wojciech dostarczył gotowy mockup stylu strony głównej (`index (5).html`): bardziej dopracowany design system niż szkielet z sesji 1: sticky nagłówek z podkreśleniem linków przy hover, pole wyszukiwania, karta „quick-pick” gatunków startowych, siatka kategorii z ikonami, tabela porównawcza, karty problemów opieki, karty bloga, 4-kolumnowa stopka.
- **Zmiana fazy projektu, jawnie zakomunikowana przez Wojciecha**: teraz nacisk na informacje, doświadczenia, zdjęcia, opisy gatunkowe, opiekę; serwis ma działać jak osobisty dziennik. Afiliacja (terraria, sprzęt, rośliny) wchodzi w kolejnej fazie, gdy pojawi się realny ruch. Usunięto z homepage CTA sprzedażowe („ile kosztuje pierwszy gad”, kalkulator kosztów jako główny hak) i zastąpiono blokiem „o autorze” wzmacniającym E-E-A-T (realny hodowca, realne doświadczenie), zgodnie z głosem opisanym w skillu `no-ai-slop`.
- Przebudowano `css/style.css` na design system z mockupu (nowe klasy: `.wrap`, `.cat`, `.tag`/`.t-easy`/`.t-mid`/`.t-hard`, `.picker`, `.prob`, `.post`, `.strip`, `.fcols`), zachowując dokładnie tę samą paletę co wcześniej. Usunięto nieużywaną animację rotatora z hero (mockup jej nie używa).
- Przebudowano `template.html` i `index.html` pod nowy nagłówek/stopkę. Nawigacja nie ma już JS-owego hamburgera; na wąskich ekranach linki się zawijają (prostsze, zgodne z mockupem).
- **Zmieniono nazwę katalogu `/poradniki/` na `/opieka-uniwersalna/`** (przez `mv`, rename zadziałał mimo że usuwanie plików w tym folderze jest zablokowane). Powód: `priorytety-podstron.xlsx` (nowszy, finalny plan 209 stron) i mockup Wojciecha oba używają `opieka-uniwersalna`/`opieka-ogolna`, nie `poradniki` z pierwszej wersji planu. Zaktualizowano wszystkie odwołania w `CLAUDE.md`, `internal-linking-plan.md`, `scripts/link_audit.py`.
- Dodano „Płazy” jako 9. kartę kategorii na stronie głównej; pominięte w mockupie Wojciecha, ale to rodzina z pozycją #1 w całym rankingu priorytetów (aksolotl, 51 000/mies.), więc pominięcie na homepage byłoby niespójne z `priorytet-podstron.csv`.
- Dodano aksolotl do tabeli porównawczej gatunków startowych z tego samego powodu.
- Samosprawdzenie własnej prozy względem `no-ai-slop`: znaleziono i poprawiono 5 użyć pauzy (—, zasada 1) we własnym tekście `index.html` i `template.html`.

_Ostatnia aktualizacja: 2026-07-28 (sesja 2)_

**Zrobione (sesja 2):**
- Przekształcono cztery pliki od Wojciecha (`AGENTS.md`, `CLAUDE.md`, `SITE_WORKFLOW.md`, `internal-linking-plan.md`; pierwotnie z innego projektu, marketintelligencetools-clean) na potrzeby terrariumdla.pl, po polsku.
- Zbudowano skill `.claude/skills/no-ai-slop/` (SKILL.md + references/ai-writing-detection.md) z głosem dopasowanym do terrarystyki: precyzja hodowcy, nie copywritera.
- Napisano ten plik, `CLAUDE.md` (root), `internal-linking-plan.md`, `scripts/link_audit.py`, minimalny `sitemap.xml`.
- Usunięto ze `SITE_WORKFLOW.md` wszystko specyficzne dla poprzedniego projektu: Surfer (płatne narzędzie SEO, nieużywane tu), `build.py` generujący nagłówki/liczniki (nie mamy takiego systemu; nawigacja jest kopiowana ręcznie, to świadomy dług techniczny odnotowany w standing rules), cały log sesji poprzedniego projektu.

**Zrobione (sesja 1; szkielet techniczny):**
- Struktura katalogów pod architekturę URL (rodziny: węże, gekony, agamy, kameleony, żółwie, bezkręgowce, płazy, inne-gady, sprzęt, karma, opieka-uniwersalna, rośliny, blog).
- `css/style.css` z paletą (`#16181A` / `#1E2023` / `#98FB98` / `#50C878`), nawigacją, stopką, kartami, tabelą porównawczą, animacją CSS „terrarium dla…”.
- `template.html`, `index.html` (szkielet strony głównej, treść placeholder), `.github/workflows/deploy.yml` (FTPS na cPanel, sekrety `FTP_SERVER`/`FTP_USERNAME`/`FTP_PASSWORD`/`FTP_TARGET_DIR` skonfigurowane przez Wojciecha).

**Następne / otwarte:**
- Zero opublikowanych podstron treściowych poza szkieletem `index.html`. Fala 1 (30 stron, filary gatunków) jeszcze nie napisana; patrz `priorytet-podstron.csv` dla kolejności.
- Brak systemu współdzielonych includes dla nav/footer; jeśli liczba stron urośnie, warto rozważyć prosty skrypt budujący (poza zakresem tej sesji, nikt o to nie prosił).
- `index.html` ma treść placeholder (przykładowe teksty kart, wymiary w tabeli startowej); do weryfikacji merytorycznej przed publikacją na żywo.
- `sitemap.xml` zawiera na razie tylko stronę główną; rozbudowywać przy każdej nowej podstronie (patrz standing rules wyżej).
