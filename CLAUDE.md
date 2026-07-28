# CLAUDE.md: terrariumdla.pl

Wytyczne dla Claude pracującego w tym repozytorium. Statyczna strona HTML o terrarystyce: węże, gekony, agamy, kameleony, żółwie, bezkręgowce, płazy, sprzęt, karma, opieka uniwersalna. Bez frameworka, bez procesu budowania, pliki HTML publikowane wprost przez GitHub Actions na cPanel (patrz `.github/workflows/deploy.yml`).

**Faza obecna: informacyjnie, nie sprzedażowo.** Serwis ma teraz działać jak osobisty dziennik terrarystyczny: wiedza, doświadczenia, zdjęcia, opisy gatunkowe, opieka. Bez nacisku na afiliację czy sprzedaż sprzętu. Afiliacja (terraria, sprzęt, rośliny) wchodzi w kolejnej fazie, gdy serwis zacznie łapać realny ruch. Nie dodawaj CTA sprzedażowych (kalkulatory kosztów jako główny hak, „kup teraz”) na obecnym etapie bez wyraźnej prośby Wojciecha.

## Kolejność czytania na starcie nowej sesji

1. `SITE_WORKFLOW.md`: pamięć trwała między sesjami: standing rules, pełny workflow pisania podstrony, sekcja "Bieżący status" na dole (tam kończy się poprzednia sesja).
2. Ten plik.
3. `.claude/skills/no-ai-slop/SKILL.md`: zasady pisania, twarde zakazy. Obowiązkowe przed napisaniem jednego zdania treści.
4. `internal-linking-plan.md`: polityka linkowania wewnętrznego i tabela progów.
5. Materiały planistyczne: `plan-podstron.csv` / `priorytet-podstron.csv` (arkusze dostarczone przez Wojciecha); które podstrony pisać w jakiej kolejności, jaka fraza główna, jaki wolumen.

Nie ufaj wpisowi „gotowe” z poprzedniej sesji bez zweryfikowania go samodzielnie (`scripts/link_audit.py`, wizualne sprawdzenie obrazów, sprawdzenie tagów).

## Zasady operacyjne

- Przy pisaniu lub redagowaniu dowolnej prozy: najpierw przeczytaj `.claude/skills/no-ai-slop/SKILL.md` i `.claude/skills/no-ai-slop/references/ai-writing-detection.md`. Samosprawdź tekst względem tej listy przed oddaniem.
- Żadnych niepodpartych statystyk ani zmyślonych faktów o gatunkach, cenach czy przepisach; patrz zasady 2, 18, 19 w skillu no-ai-slop.
- Każda nowa podstrona: sprawdź `internal-linking-plan.md` pod kątem progu linków dla danego typu strony i słownika kotwic.
- Każda nowa podstrona musi być wpięta w indeks swojej rodziny (np. `/weze/index.html`) i w `sitemap.xml`.
- Struktura URL: trójpoziomowa, rodzina/gatunek/temat; np. `/weze/waz-zbozowy/przewodnik/`. Kopiuj `template.html` jako punkt startowy dla nowej podstrony.
- Paleta i komponenty: `css/style.css`. Nie twórz nowych kolorów ani nowych wzorców komponentów bez potrzeby; rozszerzaj istniejące klasy (`.card`, `.compare-table`, `.badge`, `.btn`).

## Struktura repo

```
index.html              strona główna
template.html           wzorzec podstrony do kopiowania
css/style.css            arkusz główny, jedna paleta na całą stronę
assets/img/              obrazy i SVG
weze/ gekony/ agamy/ kameleony/ zolwie/ bezkregowce/
plazy/ inne-gady/ sprzet/ karma/ opieka-uniwersalna/ rosliny/ blog/
                          rodziny treści, każda z własnym index.html-hubem
.github/workflows/deploy.yml   auto-deploy FTPS na push do main
.claude/skills/no-ai-slop/     zasady pisania (patrz wyżej)
scripts/link_audit.py          brama jakości: próg linków + sprawdzenie hrefów
SITE_WORKFLOW.md                pamięć trwała, pełny workflow, status sesji
internal-linking-plan.md        polityka linkowania wewnętrznego
```

## Kontekst biznesowy w skrócie

209 podstron w 5 falach publikacji, priorytet wg wolumenu wyszukiwań (dane Ahrefs, źródła: `plan-podstron.csv`, `priorytet-podstron.csv`). Fala 1 (fundament, 30 stron): 12 filarów gatunków, potem zaskroniec/padalec (ruch identyfikacyjny), potem strony cenowe i „terrarium dla X”. Docelowo: blog → sklep na subdomenie → forum. Monetyzacja przez afiliację sprzętu, nie reklamę displayową (CPC 0,02–0,06 USD w tej niszy).
