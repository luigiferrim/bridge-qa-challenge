# Desafio Tecnico QA - Laboratorio Bridge

**Candidato:** Luigi Ferri Maines

Automacao de testes criada como bonus para o desafio tecnico do Laboratorio Bridge. O foco dos testes esta no modulo de prescricao de medicamentos, com apoio do login apenas para acessar a area autenticada do sistema.

## Tecnologias

- Python
- Pytest
- Playwright
- Page Object Model

## Cenarios automatizados

1. **Caminho feliz da prescricao**

   Valida o cadastro de uma prescricao com dados validos de paciente, medicamento Amoxicilina, via Oral e periodo de dose de 8h. Ao final, verifica se o receituario foi exibido e se contem o medicamento cadastrado.

2. **Regressao do Bug 02**

   Reproduz a entrada `e10` no campo de periodo da dose e verifica se o erro tecnico `Prescricao validation failed: periodoDose` nao aparece para o usuario.

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
