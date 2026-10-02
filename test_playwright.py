
import os 
import re #použil jsem regex kvuli častým změnám u url adres
from dotenv import load_dotenv # použil jsem env kvuli ochraně přihlašovacích udajů 
from playwright.sync_api import Page, expect

load_dotenv("hesla.env")


#USPĚPŠNÉ PŘIHLÁŠENÍ 
def test_successful_login_flow(page: Page):

    page.goto("https://engeto.cz/prehled-kurzu/")
    page.locator("#cookiescript_reject").click()
    page.get_by_role("link", name="Výukový portál").click() 
 
    expect(page).to_have_url("https://portal.engeto.com/lobby/sign-in")
    
    page.locator(".bg-base-white a").click() 
    
    
    expect(page).to_have_url(re.compile(r"engeto-v2\.eu\.auth0\.com/u/login"))
    
   
    page.locator("#username").fill(os.environ["ENGETO_EMAIL"])
    page.locator("#password").fill(os.environ["ENGETO_PASSWORD"])
    page.locator("button[type='submit']").click() 
    
   
    expect(page).to_have_url(re.compile(r"portal\.engeto\.com/study/"))



#ŠPATNÉ PŘIHLAŠOVACÍ UDAJE
def test_unsuccesful_flow(page: Page):
    page.goto("https://engeto.cz/prehled-kurzu/")
    page.locator("#cookiescript_reject").click()
    page.get_by_role("link", name="Výukový portál").click() 
     
    expect(page).to_have_url("https://portal.engeto.com/lobby/sign-in")
        
    page.locator(".bg-base-white a").click() 
        
    expect(page).to_have_url(re.compile(r"engeto-v2\.eu\.auth0\.com/u/login"))
    page.locator("#username").fill("špatnéjmeno")
    page.locator("#password").fill("špatnéheslo")
    page.locator("button[type='submit']").click() 

    #Ověření, že systém nepustil uživatele dál a zůstane na login page
    expect(page).to_have_url(re.compile(r"engeto-v2\.eu\.auth0\.com/u/login"))


# test prázdného formuláře, ověří, že odeslání prázdného přihlašovacího formuláře nepustí uživatele dál.
def test_login_with_empty_fields(page: Page):
    
    page.goto("https://engeto.cz/prehled-kurzu/")
    page.locator("#cookiescript_reject").click()
    page.get_by_role("link", name="Výukový portál").click()
    page.locator(".bg-base-white a").click()

    expect(page).to_have_url(re.compile(r"engeto-v2\.eu\.auth0\.com/u/login"))
    page.locator("button[type='submit']").click()

    # Ani s prázdnými poli by uživatel neměl projít dál
    expect(page).to_have_url(re.compile(r"engeto-v2\.eu\.auth0\.com/u/login"))