# Automatizované testy – Engeto přihlášení

Tento repozitář obsahuje automatizované End-to-End (E2E) testy pro přihlašovací proces na výukový portál Engeto. Projekt je postaven na Pythonu s využitím frameworků **Pytest** a **Playwright**.

## Funkcionalita testů
- **Ověření úspěšného přihlášení** s platnými údaji.
- **Ověření neúspěšného přihlášení** (špatné heslo/email) s kontrolou zobrazení chybové hlášky.
- **Ověření chování formuláře** při pokusu o odeslání s prázdnými poli.
- Využití `conftest.py` pro automatizovanou navigaci před každým testem (**DRY princip**).

## Požadavky na prostředí 
- **Python:** verze 3.10 a vyšší (projekt byl vyvíjen na verzi 3.14.7)
- **Git**

## Instalace

1. **Naklonování repozitáře:**
   ```bash
   git clone <odkaz-na-tvuj-repozitar>
   cd <nazev-slozky>
   ```

2. **Instalace závislostí:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Instalace Playwright prohlížečů:**
   Tento krok je nezbytný pro správné spuštění testů.
   ```bash
   playwright install
   ```

## Nastavení přihlašovacích údajů (.env)
Testy vyžadují platné přihlašovací údaje k portálu Engeto. Z bezpečnostních důvodů nejsou tyto reálné údaje součástí repozitáře (soubor je chráněn přes `.gitignore`).

Pro úspěšné spuštění testů je nutné provést následující kroky:

1. V hlavní složce projektu **vytvořte nový soubor** s názvem `hesla.env`.
2. Otevřete šablonu `hesla.env.example` a **zkopírujte její obsah** do nově vytvořeného `hesla.env`.
3. **Doplňte platný registrační e-mail a heslo**:
   ```env
   ENGETO_EMAIL=tvuj.realny.email@domena.cz
   ENGETO_PASSWORD=tvoje_realne_heslo
   ```

## Spuštění testů

Pro spuštění všech testů na pozadí (**headless mód**) zadejte do terminálu:
```bash
pytest
```

Pokud chcete vizuálně vidět, jak prohlížeč webem prochází (**headed mód**), použijte příkaz:
```bash
pytest --headed
```
