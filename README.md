[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=19348147)
# Python: Import
In Python kannst du Module importieren und deren Funktionen nutzen, um deinen Code zu organisieren und wiederverwendbar zu machen. Ein Modul ist eigentlich nur eine Python Datei, so wie wir sie in den vorherigen Übungen bereits geschrieben haben. Hier ist eine einfache Anleitung, wie du so eine Datei (Modul) importieren und nutzen kannst.

## Gesamtes Modul importieren
Du kannst ein Modul mit dem import-Schlüsselwort importieren.

**Beispiel**:
```
import math
```

### Funktion aus einem Modul nutzen
Nachdem du das Modul importiert hast, kannst du seine Funktionen verwenden. 

**Beispiel**:
```
import math

result = math.sqrt(16)  # SQuare RooT => Quadratwurzel
print(result)  # Ausgabe: 4.0
```

## Nur bestimmte Funktionen importieren
Du kannst auch nur bestimmte Funktionen aus einem Modul importieren, um den Code übersichtlicher zu gestalten. 

**Beispiel**:
```
from math import sqrt

result = sqrt(16)
print(result)  # Ausgabe: 4.0
```

## Alias für ein Modul oder eine Funktion erstellen
Manchmal ist es hilfreich, ein Alias für ein Modul oder eine Funktion zu erstellen, um den Code kürzer zu machen. 

**Beispiel für ein Alias des Moduls**:
```
import math as m

result = m.sqrt(16)
print(result)  # Ausgabe: 4.0
```

**Beispiel für ein Alias einer Funktion**:
```
from math import sqrt as s

result = s(16)
print(result)  # Ausgabe: 4.0
```


## Aufgabe
Es soll eine Funktion zum Validieren eines Datums erstellt werden: 
```
def validateDate(day, month, year)
    ...
```

Die Funktion soll `true` zurückgeben, wenn das Datum valide (also ein gültiges Datum) ist und `false` zurück geben, wenn das Datum nicht valide (also ein ungültiges Datum) ist. 

**Beispiele für valide und unvalide Daten**  
| Datum | Validität |
|-----------|------------|
| 32.01.2025 | nicht valide, da der Minat Januar nur 31 Tage hat |
| 29.02.2024 | valide, da 2024 ein Schaltjahr ist |
| 29.02.2025 | nicht valide, da 2025 kein Schaltjahr ist  |
| 31.04.899 | nicht valide, da der Monat April nur 30 Tage hat |
| -12.06.800 | nicht valide, da eine negative ahl als Tag ungültig ist	|
| 12.14.16  | nicht valide, da es keinen Monat 14 gibt |

**Tipp**: Es liegt bereits eine Musterlösung zum Prüfen auf Schaltjahr vor (siehe Datei *leapYear.py*). Sie können den Quellcode in dieser Datei aber auch durch Ihre Lösung aus der letzten Aufgabe zum Schaltjahr ersetzen.

**WICHTIG:** Ändere **NICHT** die anderen Dateien
