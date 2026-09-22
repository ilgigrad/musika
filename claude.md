Tu es producteur de mes projets de musique
Je voudrais enregistrer des éléments de guitare, de voix, les mixer et les associer à des séquences produites par des synthétiseurs en utilisant mon macbook
on se concentre dans un premier temps dans un projet de synthetiseur as code, en utilisant python si possible
trouver et décrire une architecture pour produire des sons à partir de code
installer les composants et les pousser vers le repository sur le github https://github.com/ilgigrad/musika
ecrire les evolutions dans claude.md
créer et maintenir un fichier musika.md qui log toutes les évolutions fonctionnelles et ce qui a été créé en terme de musique 

## Journal des évolutions

- 2026-09-22 : architecture retenue pour le synthétiseur as code (5 couches : composition, synthèse, audio I/O, mixage/effets, export). Détails dans musika.md. Pas encore de code installé ni de dépôt git initialisé.
- 2026-09-22 : scaffold installé (virtualenv, pas de Docker — pas d'accès CoreAudio depuis un conteneur macOS) et poussé sur https://github.com/ilgigrad/musika (branche main). Détails dans musika.md.
