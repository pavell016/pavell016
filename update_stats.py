from github import Github
import os
import json
import pandas as pd

# Tu token personal de GitHub (configura esto como un secreto en GitHub Actions)
token = os.getenv('GITHUB_TOKEN')
username = "TU_USUARIO_DE_GITHUB"

g = Github(token)
user = g.get_user(username)

# Obtiene todos los repositorios del usuario
repos = user.get_repos()

language_data = {}

for repo in repos:
    if not repo.fork:  # Ignorar repositorios que son forks
        languages = repo.get_languages()
        for lang, count in languages.items():
            language_data[lang] = language_data.get(lang, 0) + count

# Calcular el porcentaje de cada lenguaje
total = sum(language_data.values())
language_percentages = {lang: (count / total) * 100 for lang, count in language_data.items()}

# Crear una tabla Markdown
df = pd.DataFrame(language_percentages.items(), columns=['Language', 'Percentage'])
df = df.sort_values(by='Percentage', ascending=False)
table = df.to_markdown(index=False)

# Actualizar el archivo README o una tabla en otro archivo
with open('LANGUAGE_STATS.md', 'w') as f:
    f.write("# Language Usage Statistics\n\n")
    f.write(table)
