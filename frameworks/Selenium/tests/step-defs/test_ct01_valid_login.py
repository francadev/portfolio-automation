import pytest
from pytest_bdd import given, scenario, then, when

from pages.login_page import LoginPage


@pytest.fixture
def lp(driver):
    return LoginPage(driver)


@scenario("../features/ct01_valid_login.feature", "Usuário realiza login com credenciais válidas")
def test_ct01_valid_login():
    pass


@given("que o usuário está na página de login do Orange HRM")
def go_to_login_page(lp):
    lp.verify_login_page()


@when('ele insere um usuário válido "admin" e uma senha válida "admin123"')
def enter_valid_credentials(lp):
    lp.enter_credentials("admin", "admin123")
    # breakpoint()


@when('clica no botão "Login"')
def click_login(lp):
    lp.click_login()


@then("ele deve ser redirecionado para o dashboard do sistema")
def verify_dashboard_access(lp):
    lp.verify_dashboard_access()
