import os

import pytest
from dotenv import load_dotenv
from playwright.sync_api import expect

from pages.login_page import LoginPage
from pages.prescricao_page import PrescricaoPage


load_dotenv()

USUARIO = os.getenv("BRIDGE_USER")
SENHA = os.getenv("BRIDGE_PASSWORD")

LOGIN_URL = "https://desafio-ps-qa.bridge.ufsc.tech"
PRESCRICAO_URL = "https://desafio-ps-qa.bridge.ufsc.tech/preescrever/medicamento"
ERRO_TECNICO_MONGOOSE = "Prescricao validation failed: periodoDose"


@pytest.fixture
def prescricao_logada(page):
    assert USUARIO, "Configure BRIDGE_USER no arquivo .env antes de rodar os testes."
    assert SENHA, "Configure BRIDGE_PASSWORD no arquivo .env antes de rodar os testes."

    login_page = LoginPage(page)
    login_page.acessar_pagina(LOGIN_URL)
    login_page.realizar_login(USUARIO, SENHA)

    prescricao_page = PrescricaoPage(page)
    prescricao_page.acessar_sistema(PRESCRICAO_URL)
    expect(prescricao_page.input_nome).to_be_visible(timeout=10000)

    return prescricao_page


def test_fluxo_feliz_prescricao(prescricao_logada):
    prescricao_page = prescricao_logada

    prescricao_page.preencher_dados_paciente(
        "Luigi Ferri Maines",
        "529.982.247-25",
        "2000-01-01",
    )
    prescricao_page.preencher_medicamento("Amoxicilina", "Oral")
    prescricao_page.selecionar_periodo_botao()
    prescricao_page.salvar_prescricao()

    expect(prescricao_page.card_receituario).to_be_visible(timeout=15000)
    expect(prescricao_page.card_receituario).to_contain_text("Amoxicilina", timeout=15000)


def test_bug_exposicao_banco_de_dados(page, prescricao_logada):
    prescricao_page = prescricao_logada

    prescricao_page.preencher_dados_paciente(
        "Paciente Teste",
        "390.533.447-05",
        "1990-05-15",
    )
    prescricao_page.preencher_medicamento("Dipirona", "Oral")

    prescricao_page.input_periodo_livre.press_sequentially("e10")
    prescricao_page.salvar_prescricao()

    expect(page.locator("body")).not_to_contain_text(
        ERRO_TECNICO_MONGOOSE,
        timeout=3000,
    )
