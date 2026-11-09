# Desafio Tecnico QA - Laboratorio Bridge

**Candidato:** Luigi Ferri Maines

Automacao de testes criada como bonus para o desafio tecnico do Laboratorio Bridge. O foco dos testes esta no modulo de prescricao de medicamentos, com apoio do login apenas para acessar a area autenticada do sistema.

**Resultado:** fui aprovado no processo e desde junho de 2026 trabalho como QA Automation Engineer no Laboratorio Bridge, na Jornada do Estudante (plataforma do MEC).

## Tecnologias

- Python
- Pytest
- Playwright
- Page Object Model

## Cenarios automatizados

1. **Caminho feliz da prescricao**

   Valida o cadastro de uma prescricao com dados validos de paciente, medicamento Amoxicilina, via Oral e periodo de dose de 8h. Apos salvar, verifica se o receituario foi exibido na tela com o medicamento correto. Em seguida, navega para a pagina de listagem ("Ver todas as receitas") e confirma que o cadastro mais recente contem o nome do paciente, o CPF e o principio ativo informados, validando a persistencia real do dado.

2. **Regressao do Bug 02**

   Reproduz a entrada `e10` no campo de periodo da dose e verifica se o erro tecnico `Prescricao validation failed: periodoDose` nao aparece para o usuario.

   Observacao: enquanto o bug estiver presente no sistema, este teste deve falhar. A falha indica que a aplicacao ainda esta exibindo uma mensagem tecnica de validacao para o usuario.

## Como executar

Crie e ative o ambiente virtual:

```powershell
python -m venv venv
venv\Scripts\activate
```

Instale as dependencias:

```powershell
pip install -r requirements.txt
playwright install
```

Crie um arquivo `.env` na raiz do projeto:

```env
BRIDGE_USER=seu_usuario
BRIDGE_PASSWORD=sua_senha
```

Rode os testes em modo headless:

```powershell
pytest
```

Ou com o navegador visivel:

```powershell
pytest --headed
```
