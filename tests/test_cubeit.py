from playwright.sync_api import Page, expect
import pytest


BASE_URL = "http://127.0.0.1:8000/"

@pytest.mark.parametrize(
    ("num", "num_cube"),
    (
    (2, 8),
    (3, 27),
    (5, 125)
    )
)
def test_cube(page: Page, num, num_cube):
    page.goto(BASE_URL)

    page.get_by_placeholder("enter number...").fill(num)
    page.get_by_role("button", name="Cube").click()

    result = page.locator("css=p#result")

    expect(result).to_contain_text(num_cube)

def test_empty_input(page: Page):
    page.goto(BASE_URL)

    page.get_by_placeholder("enter number...").fill("")
    page.get_by_role("button", name="Cube").click()

    result = page.locator("css=p#result")

    expect(result).to_have_text("Enter something!")
