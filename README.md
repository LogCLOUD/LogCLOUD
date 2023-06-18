# Projeto Template

Irei demonstrar como funciona e como montar um template para os projetos do curso de graduação em Gestão da Produção Industrial, ensinando na utilização correta da ferramenta GitHub e Gira. 

# Badges

owner="AndreLuizRibeiro"
repo="Template"

response=$(curl -s "https://api.github.com/repos/$owner/$repo")

total_issues=$(echo "$response" | jq '.open_issues_count')
total_pulls=$(echo "$response" | jq '.open_pull_issues_count')

closed_issues=$(echo "$response" | jq '.closed_issues')
closed_pulls=$(echo "$response" | jq '.closed_pull_issues')

progresso_issues=$(bc <<< "scale=2; ($closed_issues / ($closed_issues + $total_issues)) * 100")
progresso_pulls=$(bc <<< "scale=2; ($closed_pulls / ($closed_pulls + $total_pulls)) * 100")

echo "Progresso de Issues: $progresso_issues%"
echo "Progresso de Pull Requests: $progresso_pulls%"name: Atualizar Badge de Progresso
![example workflow](https://github.com/github/docs/actions/workflows/main.yml/badge.svg)

# Índice

* [Projeto](#projeto-template)
* [Badges](#badges)
* [Índice](#índice)
* [Equipe](#equipe)
* [Objetivo do Projeto](#objetivo-do-projeto)
* [Funcionalidades](#funcionalidades)
* [Demonstração da Aplicação](#demonstração-da-aplicação)
* [Tecnologias Utilizadas](#tecnologias-utilizadas)
* [Plano de Entrega](#plano-de-entrega)
* [Disciplinas relacionadas](#disciplinas-relacionadas)
* [Competências desenvolvidas](#competências-desenvolvidas)
* [Referências Bibliográficas](#referências-bibliográficas)
* [Autores](#autores)

# Equipe

# Objetivo do Projeto

# Funcionalidades

# Demonstração da Aplicação

# Tecnologias Utilizadas

  - GitHub
  - Power Point
  - Excel
  - Gira
  - Power BI

# Plano de Entregas

## Cronograma

definir as datas das atividades a serem desenvolvidas e adiciona-las aqui

## Sprint 1. Desenvolvimento
- [x] Defina o propósito do template;
- [x] Identifique os elementos principais;
- [] Esboce o layout;
- [] Escolha cores e fontes;
- [] Desenvolva o design;
- [] Teste e revise;
- [] Documente instruções de uso;
- [] Criação do vídeo;
- [] Finalize e aprovação.

## Sprint 2. Divulgação
- [] Documento passo a passo;
- [] Vídeo passo a passo;
- [] Treinamento com os professores;
- [] Treinamento com os alunos;
- [] Monitoramento e ajustes.


# Disciplinas relacionadas


# Competências desenvolvidas

## Hard Skill
<details>
<ul>◻️<summary>Hard Skills desenvolvidas</summary></ul>

- Item 1
- Item 2
- Item 3

</details>

## Soft Skill
<details>
<ul>◻️<summary>Soft Skills desenvolvidas</summary></ul>

- Item 1
- Item 2
- Item 3

</details>
# Referências Bibliográficas


# Autores
