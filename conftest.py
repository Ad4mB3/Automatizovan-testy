import pytest
import re
from playwright.sync_api import Page, expect

COOKIE_REJECT_BUTTON = "#cookiescript_reject"

"""
Fixture pro navigaci na přihlašovací stránku před každým testem.
Odmítne cookies a prokliká se až na formulář.
"""

@pytest.fixture
def login_page(page: Page):
   
    page.goto("https://engeto.cz/prehled-kurzu/")
    page.locator(COOKIE_REJECT_BUTTON).click()
    page.get_by_role("link", name="Výukový portál").click()
    
    expect(page).to_have_url(re.compile(r".*portal\.engeto\.com/lobby/sign-in"), timeout=10000)
    page.get_by_text("Přihlásit se pomoci e-mailu a hesla").click()
    
    expect(page).to_have_url(re.compile(r"engeto-v2\.eu\.auth0\.com/u/login"))
    return page

