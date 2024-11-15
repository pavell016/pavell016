# Wellcome to my personal repository


## Studies

  ASIX (2022 - 2024)
  
    📍 La Salle Gràcia (Plaça del Nord, 14, Gràcia, 08024 Barcelona)
    web - https://gracia.lasalle.cat/es/

  DAM (2024 - ongoing)
  
    📍 La Salle Gràcia (Plaça del Nord, 14, Gràcia, 08024 Barcelona)
    web - https://gracia.lasalle.cat/es/  

name: Update readme with Language Stats

on:
  schedule:
    - cron: '0 0 * * *'  # Runs at midnight every day
  push:
    branches:
      - main  # Adjust to match your default branch

jobs:
  update-readme:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2

      - name: Update README Language Statistics
        uses: DimaTc/readme-stats-updater@main
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}

      - name: Commit changes
        run: |
          git config --global user.name 'GitHub Actions Bot'
          git config --global user.email 'actions@github.com'
          git add README.md
          git commit -m "Update README with language statistics and last update date" || echo "No changes to commit"
          git push

# ![pavell016's Stats](https://github-readme-stats.vercel.app/api?username=pavell016&theme=vue-dark&show_icons=true&hide_border=false&count_private=true)

<!--
**pavell016/pavell016** is a ✨ _special_ ✨ repository because its `README.md` (this file) appears on your GitHub profile.

Here are some ideas to get you started:

- 🔭 I’m currently working on ...
- 🌱 I’m currently learning ...
- 👯 I’m looking to collaborate on ...
- 🤔 I’m looking for help with ...
- 💬 Ask me about ...
- 📫 How to reach me: ...
- 😄 Pronouns: ...
- ⚡ Fun fact: ...
-->
