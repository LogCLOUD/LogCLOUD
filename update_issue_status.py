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
response_data = response.json()

# Ensure response_data is a list or dictionary
if isinstance(response_data, str):
    response_data = json.loads(response_data)

# Extract the issues from the response_data
issues = response_data

# Calculate the completed issues
completed_issues = sum(1 for issue in issues if issue.get("state") == "closed")

# Exibe as informações no README.md
readme_content = f"""
## Status das Issues

Atualmente, existem {len(issues)} issues em aberto, das quais {completed_issues} estão concluídas. Isso representa uma porcentagem de {(completed_issues / len(issues) * 100):.2f}% de issues em aberto.
"""

# Salva as informações no arquivo README.md
with open("README.md", "w") as readme_file:
    readme_file.write(readme_content)
