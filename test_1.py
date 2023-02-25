from selene.support.shared import browser
from selene import be, have

def test(browser_1):
    browser.open('https://www.google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))