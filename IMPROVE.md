# Software Assistants Demo - Qualitätsverbesserung

Dieses Projekt demonstriert verschiedene Ebenen von Software-Assistenten, von einfachen Syntax-Checks bis hin zu KI-gestützter Entwicklung.

## Voraussetzungen
- Cursor AI 
- Python 3.10 oder höher

## Schritt 1:  Syntaxprüfung
- Öffne das Projekt in CursorAI
- Aktiviere Python Language Support (Python Extension)
- Installiere die requirements
  ```bash
  pip install -r requirements.txt
  ```
- Identifiziere grundlegende Syntax-Fehler in:
  - app/utils.py (fehlende Klammern)
  - app/models.py (falsche Einrückung)
  - app/main.py (fehlende Imports)

## Schritt 2: Linter

Option 1: Pylint pip
- Installiere den Linter:
  ```bash
  pip install pylint
  ```
Option 2: Pylint VSCode Extension
- Installiere die Pylint VSCode Extension

Weitere Schritte:
- Führe den Linter aus:
  ```bash
  pylint app
  ```
- Behebe die gefundenen Style-Probleme


## Schritt 3: Container-Sicherheit (Trivy)
**OPTIONAL, nur wenn genug Zeit ist!**
- Installiere Docker (z.B. Docker Desktop)
- Baue das Docker Image:
  ```bash
  docker build -t demo-app .
  ```
- Scanne das Image:
  ```bash
  docker run --rm -v /var/run/docker.sock:/var/run/docker.sock \
    -v $HOME/Library/Caches:/root/.cache/ aquasec/trivy:0.18.3 demo-app
  ```
  (Dieser Befehlt analysiert das eben gebaute Docker Image demo-app im fertigen trivy Docker Image aquasec/trivy:0.18.3, damit trivy nicht lokal installiert werden muss)
- Behebe die Sicherheitslücken im Dockerfile

## Schritt 4: KI-Assistenz (CursorAI)
### Teil A: Auto-Complete
- Vervollständige die TODO-Kommentare in:
  - app/utils.py
  - app/main.py

### Teil B: Chat-Assistenz
- Optimiere den Code mit CursorAI Chat:
  - Verbessere die Error-Handling in app/main.py
  - Füge Input-Validierung in app/models.py hinzu
  - Generiere Tests für app/utils.py
- Denke dir coole neue Funktionen aus und implementiere sie!

## Erfolgskriterien
- Keine Syntax-Fehler in VSCode
- Linter zeigen keine Warnungen
- (SonarCloud Quality Gate bestanden)
- (Trivy zeigt keine HIGH/CRITICAL Schwachstellen)
- Alle Funktionen implementiert und getestet
