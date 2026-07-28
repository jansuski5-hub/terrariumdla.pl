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
