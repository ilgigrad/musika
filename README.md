# Musika

Synthétiseur as code : composer, synthétiser et mixer des sons en Python, pour les associer ensuite à des enregistrements guitare/voix.

Voir `claude.md` et `musika.md` pour le contexte du projet et le journal des évolutions.

## Architecture

- `src/musika/sequencer/` — composition : décrire un morceau en code (notes, patterns).
- `src/musika/synth/` — synthèse : oscillateurs, enveloppes ADSR, voix.
- `src/musika/audio_io/` — enregistrement/lecture audio (nécessite un accès direct au matériel : à exécuter en natif sur le Mac, pas dans un conteneur).
- `src/musika/mixing/` — mixage de pistes et export WAV.

## Installation

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

## Utilisation

Rendre un exemple :

```bash
source .venv/bin/activate
python examples/simple_note.py
```

Le fichier est exporté dans `audio/example.wav` (dossier non versionné, voir `.gitignore`).

## Tests

```bash
source .venv/bin/activate
pytest
```
