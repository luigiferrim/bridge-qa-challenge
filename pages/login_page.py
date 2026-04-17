from playwright.sync_api import Page


class LoginPage:
    def __init__(self, page: Page):
        self.page = page

        self.input_usuario = page.locator("input#usuario")
        self.input_senha = page.locator("input#password")
        self.checkbox_termos = page.locator("input#termos-de-uso")
        self.btn_acessar = page.locator("button.btn-acessar")

    def acessar_pagina(self, url: str):
        self.page.goto(url)

    def realizar_login(self, usuario: str, senha: str):
        self.input_usuario.fill(usuario)
        self.input_senha.fill(senha)
        self.checkbox_termos.check()
        self.btn_acessar.click()
        self.page.wait_for_url("**/orientacoes", timeout=15000)
