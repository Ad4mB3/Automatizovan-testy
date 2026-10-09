
import os 
import re #použil jsem regex kvuli častým změnám u url adres
from dotenv import load_dotenv # použil jsem env kvuli ochraně přihlašovacích udajů 
from playwright.sync_api import Page, expect

load_dotenv("hesla.env")

#lokátory uložené v proměnných 
COOKIE_REJECT_BUTTON = "#cookiescript_reject"
USERNAME_INPUT = "#username"
PASSWORD_INPUT = "#password"
SUBMIT_BUTTON = "button[type='submit']"
LOGIN_ERROR = "#error-element-password"
EMPTY_USERNAME_ERROR = "#error-cs-username-required"
EMPTY_PASSWORD_ERROR = "#error-cs-password-required"


# Úspěšné přihlášení 
def test_successful_login_flow(login_page: Page):
    """Ověřuje úspěšné přihlášení s platnými údaji."""
    page = login_page
    page.locator(USERNAME_INPUT).fill(os.environ["ENGETO_EMAIL"])
    page.locator(PASSWORD_INPUT).fill(os.environ["ENGETO_PASSWORD"])
    page.locator(SUBMIT_BUTTON).click()

    expect(page).to_have_url(re.compile(r"portal\.engeto\.com/study/"))


# Špatné přihlašovací údaje
def test_unsuccessful_login_flow(login_page: Page):
    """Ověřuje, že při zadání špatných údajů se zobrazí chybová hláška a URL se nezmění."""
    page = login_page
    page.locator(USERNAME_INPUT).fill("spatnejmeno@email.cz")
    page.locator(PASSWORD_INPUT).fill("spatneheslo")
    page.locator(SUBMIT_BUTTON).click()

    # Po odeslání se musí objevit chybová hláška a systém nepustí uživatele dál
    expect(page.locator(LOGIN_ERROR)).to_be_visible()
    expect(page).to_have_url(re.compile(r"engeto-v2\.eu\.auth0\.com/u/login"))

# Test s prázdnými poli 
def test_login_with_empty_fields(login_page: Page):
    """Ověřuje, že odeslání prázdného formuláře vyvolá validaci a zobrazí chybové hlášky."""
    page = login_page
    page.locator(SUBMIT_BUTTON).click()

    # Ani s prázdnými poli by uživatel neměl projít dál a měl by vidět chyby u obou polí
    expect(page.locator(EMPTY_USERNAME_ERROR)).to_be_visible()
    expect(page.locator(EMPTY_PASSWORD_ERROR)).to_be_visible()
    expect(page).to_have_url(re.compile(r"engeto-v2\.eu\.auth0\.com/u/login"))

