# MySinglyLinkedList – Einfach verkettete Liste in Python

## 📌 Beschreibung

Dieses Projekt implementiert eine **einfach verkettete Liste (Singly Linked List)** in Python.
Die Liste speichert Elemente in sogenannten **Knoten (Nodes)**, die jeweils auf ihren Nachfolger zeigen.

Zusätzlich wird ein **Tail-Zeiger** verwendet, um Operationen am Listenende effizient zu machen.

---

## 🧠 Datenstruktur

Jeder Knoten besteht aus:

* `element` → gespeicherter Wert
* `next` → Verweis auf den nächsten Knoten

Die Liste verwaltet:

* `_head` → erstes Element
* `_tail` → letztes Element
* `_size` → Anzahl der Elemente

---

## ⚙️ Implementierte Methoden

### Basisfunktionen

| Methode      | Beschreibung                    | Laufzeit |
| ------------ | ------------------------------- | -------- |
| `size()`     | Gibt Anzahl der Elemente zurück | O(1)     |
| `is_empty()` | Prüft, ob die Liste leer ist    | O(1)     |
| `first()`    | Gibt das erste Element zurück   | O(1)     |

---

### Operationen am Anfang

| Methode          | Beschreibung               | Laufzeit |
| ---------------- | -------------------------- | -------- |
| `add_first(e)`   | Fügt Element am Anfang ein | O(1)     |
| `remove_first()` | Entfernt erstes Element    | O(1)     |

---

### Operationen am Ende

| Methode       | Beschreibung                | Laufzeit |
| ------------- | --------------------------- | -------- |
| `last()`      | Gibt letztes Element zurück | O(1)     |
| `add_last(e)` | Fügt Element am Ende ein    | O(1)     |

---

## 🚀 Besonderheit: Tail-Zeiger

Durch die Verwendung von `_tail` können Operationen am Ende der Liste effizient ausgeführt werden.

Ohne Tail:

* `add_last()` → O(n)
* `last()` → O(n)

Mit Tail:

* `add_last()` → O(1)
* `last()` → O(1)

---

## 🧪 Beispiel

```python
lst = MySinglyLinkedList()

lst.add_first(10)
lst.add_last(20)
lst.add_first(5)

print(lst.first())  # 5
print(lst.last())   # 20
print(lst.size())   # 3

lst.remove_first()
print(lst.first())  # 10
```

---

## ⚠️ Wichtige Spezialfälle

* Wenn die Liste leer ist:

  * `_head = None`
  * `_tail = None`

* Beim ersten Einfügen:

  * `head` und `tail` zeigen auf dasselbe Element

* Beim Entfernen des letzten Elements:

  * `_tail` muss wieder auf `None` gesetzt werden

---

## 🎯 Fazit

Diese Implementierung zeigt eine effiziente verkettete Liste mit:

* konstanten Laufzeiten für Einfügen und Zugriff
* sauberer Speicherstruktur
* optimaler Nutzung eines zusätzlichen Tail-Zeigers

---

## 📚 Lernziel

* Verständnis von verketteten Listen
* Zeigerlogik (`next`)
* Laufzeitanalyse (Big-O)
* Umgang mit Spezialfällen in Datenstrukturen
