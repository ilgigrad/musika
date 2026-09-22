# Musika — journal des évolutions

Ce fichier log les décisions fonctionnelles et les éléments musicaux/techniques créés au fil du projet.

## 2026-09-22 — Architecture retenue pour le "synthétiseur as code"

**Décision** : architecture en 5 couches, tout en Python pour la partie "as code", avec des libs spécialisées pour l'audio bas niveau.

1. **Composition** (`sequencer/`) — décrire un morceau en code : notes, patterns, structure. C'est la couche "partition".
2. **Synthèse** (`synth/`) — moteur de rendu audio en Python/NumPy (oscillateurs, enveloppes ADSR, filtres). Rendu hors temps réel (bounce en buffer), pas de contrainte de latence live pour l'instant.
3. **Entrées/sorties audio** (`audio_io/`) — enregistrement guitare/voix via `sounddevice` sur l'interface audio du MacBook, export WAV via `soundfile`.
4. **Mixage & effets** (`mixing/`) — assemblage des pistes enregistrées + séquences synthé, effets et mastering léger via `pedalboard`.
5. **Export** — bounce stéréo final en WAV.

**Pourquoi** : garde la composition et la synthèse 100 % lisibles/versionnables en Python (conforme à la demande "python si possible"), tout en s'appuyant sur des libs matures (`sounddevice`, `soundfile`, `pedalboard`) pour l'I/O audio réel plutôt que de réinventer ces couches.

**Évolution possible** : si besoin de jeu en temps réel plus tard, déléguer la synthèse à un moteur externe (SuperCollider) piloté par Python via OSC — non retenu pour la v1.

**Statut** : proposition d'architecture uniquement, pas encore de code installé ni de dépôt git initialisé.

## 2026-09-22 — Scaffold installé et poussé sur GitHub

**Décision** : pas de Docker (Docker Desktop sur macOS n'a pas d'accès direct à CoreAudio, donc l'enregistrement audio ne peut pas tourner dans un conteneur). Mise en place d'un virtualenv Python natif à la place.

**Ce qui a été créé** :
- Structure du projet en `src/musika/` : `sequencer/` (Note, Pattern), `synth/` (oscillateurs sine/saw/square/bruit blanc, enveloppe ADSR, Voice), `audio_io/` (enregistrement natif via `sounddevice`), `mixing/` (Track, mix, export WAV via `soundfile`).
- `examples/simple_note.py` : rend un petit arpège (C4-E4-G4-C5, onde en dents de scie) et l'exporte en WAV.
- 15 tests unitaires (`pytest`), tous verts.
- Virtualenv `.venv` créé avec Python 3.14.3, dépendances installées sans problème (numpy, scipy, soundfile, sounddevice, attrs, pytest).
- Dépôt git initialisé, commit initial poussé sur `https://github.com/ilgigrad/musika` (branche `main`), via SSH (le remote HTTPS ne fonctionnait pas sans credentials, `gh` était déjà authentifié en SSH).

**Non retenu pour l'instant** : `pedalboard` pour les effets/mixage avancé — le mixage v1 se limite à une sommation de buffers avec gain (`mixing/mixer.py`). À ajouter quand le besoin d'effets (reverb, compression) se présentera.

**Prochaines étapes possibles** : brancher `audio_io/recorder.py` sur un vrai enregistrement guitare/voix, enrichir le sequencer (tempo, mesures), ajouter des effets.
