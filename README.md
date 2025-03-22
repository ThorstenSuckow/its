# its
Solutions to tasks and implementation of exercises for the module 'its' in the summer semester 2025 in the distance learning program Computer Science (M.C.Sc.) at Hochschule Trier.


## src/its1
### chiffre 
Lösung zu Aufgabe ITS1 - 1.2 e.
Basierend auf der absoluten Häufigkeit der Vorkommen der Buchstaben in dem Beispieltext
findet ein einfacher Abgleich mit dem häufigsten Buchstaben im dt. Alphabet 
("E", s. https://de.wikipedia.org/wiki/Buchstabenh%C3%A4ufigkeit) statt, und die Buchstaben
werden entsprechend ihrer Position zu "E" verschoben. 

### buffer_overflow
C-Programm zur Demonstration eines Bufferoverflows.

```c
    int ok = 0;
    char target[4] = "olds";  

    printf("ok address: %d\n", &ok);
    printf("ok contents: %d\n", ok);

    strcpy(target, "Hello");
```

Auch wenn die meisten Compiler mittlerweile zumindest eine Warnung generieren, wie bspw. `gcc v14.2.0` unter Windows

```
'__builtin_memcpy' writing 6 bytes into a region of size 4 overflows the destination [-Wstringop-overflow=]gcc
```

führt das Kompilat dazu, dass zur Laufzeit die Zeichenkette `Hello` (6 Zeichen inkl. Null-Terminator `\0`) in das `char`-Array `target` der Größe 4 kopiert wird.

Da für `target` nur 4 Bytes reserviert wurden, `strcpy` aber eine Zeichenkette der Größe 5 Bytes (ohne Nullterminator) kopieren soll, wird `o` als letztes Zeichen in den Speicherbereich des Stacks geschrieben, der eigentlich für `int ok` reserviert wurde.

`ok` erhält nun den Wert `111`  - was der ASCII-Wert des lateinischen Buchstabens `o` ist. Und der Ausdruck `if (ok)` evaluiert den truthy Wert `111` zu `true`: Der Wert `0` wurde also durch den `Overflow` überschrieben. 