
from selene.support.shared import browser
from selene import be, have
import pytest

@pytest.fixture()
def browser_size():
    browser.open('https://duckduckgo.com/').driver.maximize_window()


def test_open(browser_size):
   browser.open('https://duckduckgo.com/')

def test_search():
   browser.element('[name="q"]').should(be.blank).type('Selene - User-oriented Web UI browser tests in Python').press_enter()

def test_text():
   browser.element('[id="links_wrapper"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


#негативный тест на поиск, чтобы он не выдавал результатов

def test_text_negative():
   browser.element('[id="links_wrapper"]').should(have.text('Apple'))


