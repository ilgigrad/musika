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
