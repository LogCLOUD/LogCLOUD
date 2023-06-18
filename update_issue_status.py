import requests
import json

# Configurações
repository_owner = "AndreLuizRibeiro"
repository_name = "Template"
github_token = "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"

# Faz a solicitação à API do GitHub para obter as issues em aberto
api_url = f"https://api.github.com/repos/{repository_owner}/{repository_name}/issues?state=open"
headers = {"Authorization": f"Token {github_token}"}
response = requests.get(api_url, headers=headers)

# Verifica se a resposta foi bem-sucedida e se os dados são uma lista ou dicionário
if response.status_code == 200:
    response_data = response.json()
    if isinstance(response_data, (list, dict)):
        # Extrai as issues dos dados da resposta
        if isinstance(response_data, dict):
            issues = [response_data]  # Se a resposta for um dicionário, convertemos para uma lista contendo o dicionário
        else:
            issues = response_data  # Se a resposta for uma lista, mantemos como está

        # Calcula as issues concluídas
        completed_issues = sum(1 for issue in issues if issue.get("state") == "closed")

        # Exibe as informações no README.md
        readme_content = f"""
        ## Status das Issues

        Atualmente, existem {len(issues)} issues em aberto, das quais {completed_issues} estão concluídas. Isso representa uma porcentagem de {(completed_issues / len(issues) * 100):.2f}% de issues em aberto.
        """

        # Salva as informações no arquivo README.md
        with open("README.md", "w") as readme_file:
            readme_file.write(readme_content)
    else:
        print("A resposta da API não contém uma lista ou dicionário de dados.")
else:
    print(f"A solicitação à API do GitHub falhou. Código de status: {response.status_code}")
