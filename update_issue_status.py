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
issues = json.loads(response.text)

# Calcula os valores dinamicamente
total_issues = len(issues)
completed_issues = sum(1 for issue in issues if issue("state") == "closed")
open_issues_percentage = (total_issues - completed_issues) / total_issues * 100

# Exibe as informações no README.md
readme_content = f"""
## Status das Issues

Atualmente, existem {total_issues} issues em aberto, das quais {completed_issues} estão concluídas. Isso representa uma porcentagem de {open_issues_percentage:.2f}% de issues em aberto.
"""

# Salva as informações no arquivo README.md
with open("README.md", "w") as readme_file:
    readme_file.write(readme_content)
