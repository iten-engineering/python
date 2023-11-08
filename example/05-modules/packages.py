# =============================================================================
# Python examples - packages
# =============================================================================

# -----------------------------------------------------------------------------
# Packages
# -----------------------------------------------------------------------------

# - Mit Hilfe von Packages werden Python Module organisiert.
# - Dabei kommt eine Punkt Notation zum Einsatz.
# - Mit dem Ausdruck A.B wird zum Beispiel das Modul B innerhalb vom Pakage A referenziert.
# - Jedes Modul hat seinen eigenen Namensraum, dadurch werden Namenskonflikte (von Variablen und Klassen) verhindert

# - Packages sind Verzeichnisse, die Modoule der Packages sind in entsprechenden Unterverzeichnissen.
# - Innerhalb vom Package Verzeichnis muss zwingend eine Datei __init__.py vorhanden sein, damit Python das Verzeichnis als
#   Package identifiziert
# - Wenn ein Package importiert wird, durchsucht Python die Verzeichnisse der sys.path Variable, um das entsprechende Package
#   Verzeichis zu lokalisiern

# -----------------------------------------------------------------------------
# Beispiel
# -----------------------------------------------------------------------------

#   sound/                      Top-level package
#       __init__.py             Initialize the sound package
#
#       formats/                Subpackage for file format conversions
#            __init__.py
#           wavread.py          - Module wavread
#           wavwrite.py         - Module wavwrite
#           ...
#
#       effects/                Subpackage for sound effects
#           __init__.py
#           echo.py             - Module echo
#           surround.py
#           reverse.py
#           ...
#
#       filters/                Subpackage for filters
#           __init__.py
#           equalizer.py
#           vocoder.py
#           karaoke.py

# -----------------------------------------------------------------------------
# Imports
# -----------------------------------------------------------------------------

# Import Modul und Referenzierung mit vollen Namen
# import sound.effects.echo
# sound.effects.echo.echofilter(input, output, delay=0.7, atten=4)

# Import Modul ohne Package Prefix und Referenzierung mit einfachem Modulnamen
# from sound.effects import echo
# echo.echofilter(input, output, delay=0.7, atten=4)

# Direkter Import einer Funktion oder Variablen eines Moduls
# from sound.effects.echo import echofilter
# echofilter(input, output, delay=0.7, atten=4)

# -----------------------------------------------------------------------------
# Imports mit *
# -----------------------------------------------------------------------------

# - Bei einem Import mit * werden die Module importiert, welche im Package entsprechend angegeben werden
# - Die Angabe erfolgt in der Datei "__init__.py" mit Hilfe der Variable "__all__"
# - Diese definiert eine Liste der Module, die das Package zur Verfügung stellt, wie zum Beispiel:
#   __all__ = ["echo", "surround", "reverse"]
# - Mit dem folgenden Import Statment würden somit die obigen Module auf einmal importiert:
#   sound.effects import *

# - Es ist in der Verantwortung der Package Entwickler bei neuen Package Release, die Liste "up-to-date" zu halten
# - Es ist auch möglich keine Angaben zu machen (falls man keine Verwendung für den Import mit * hat)
# - Falls __all__ nicht definiert ist, werden mit dem Statement "sound.effects import *" die Module von "sound.effects" nicht importiert
#   - Es wird nur sichergestellt dass das Package sound.effects importiert wird
#   - Der Initialisierungs Code der Datei __init__.py ausgeführt wird sowie die dort definierten Namen importiert werden
# > Generell werden Imports mit expliziter Angabe der Module empfohlen

# -----------------------------------------------------------------------------
# Further details
# -----------------------------------------------------------------------------

# Links:
# - https://docs.python.org/3/tutorial/modules.html
# - https://realpython.com/python-modules-packages/

# =============================================================================
# The end.
