import pytest
from selene.support.shared import browser
@pytest.fixture(scope="session")
def browser_1():
    browser.config.window_width = 1200
    browser.config.window_height = 800
    return browser
