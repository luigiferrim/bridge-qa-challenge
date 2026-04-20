from playwright.sync_api import Page


class PrescricaoPage:
    def __init__(self, page: Page):
        self.page = page

        self.input_nome = page.locator("input#nomeCompleto")
        self.input_cpf = page.locator("input#cpf")
        self.input_data_nascimento = page.locator("input#dataNascimento")
        self.input_principio_ativo = page.locator("input#principioAtivo")
        self.input_via_administracao = page.locator("input#viaAdministracao")
        self.btn_periodo_8h = page.locator("button.periodo-btn", has_text="8h")
        self.input_periodo_livre = page.locator("input#periodo-input")
        self.btn_salvar = page.locator("button", has_text="Salvar")
        self.mensagem_erro = page.locator(".mensagem-erro")
        self.card_receituario = page.locator(".card-medicamento")
        self.btn_ver_todas_receitas = page.locator("a[href='/visualizar/receitas']")
        self.cards_cadastro = page.locator("div.cadastro")

    def acessar_sistema(self, url: str):
        self.page.goto(url)

    def preencher_dados_paciente(self, nome: str, cpf: str, data_nasc: str):
        self.input_nome.fill(nome)
        self.input_cpf.fill("")
        self.input_cpf.press_sequentially("".join(filter(str.isdigit, cpf)))
        self.input_data_nascimento.fill(data_nasc)

    def preencher_medicamento(self, principio: str, via: str):
        self.input_principio_ativo.fill(principio)
        self.input_via_administracao.fill(via)

    def selecionar_periodo_botao(self):
        self.btn_periodo_8h.click()

    def salvar_prescricao(self):
        self.btn_salvar.click()

    def clicar_ver_todas_receitas(self):
        self.btn_ver_todas_receitas.click()
