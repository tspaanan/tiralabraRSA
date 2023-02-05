# Testausdokumentti

| Name                |    Stmts |     Miss |   Branch |   BrPart |   Cover |
|-------------------- | -------: | -------: | -------: | -------: | ------: |
| Testit/unittests.py |       29 |        1 |        6 |        1 |     94% |
| algorithms.py       |       50 |        2 |       20 |        2 |     94% |
| create\_keys.py     |       30 |       21 |        8 |        0 |     29% |
| key\_objects.py     |       20 |        8 |        0 |        0 |     60% |
|           **TOTAL** |  **129** |   **32** |   **34** |    **3** | **75%** |

(Sama informaatio eri muodossa sisältyy myös [Testikattavuusraporttiin](https://github.com/tspaanan/tiralabraRSA/blob/main/Dokumentaatio/Coverage_report.html))

Ohjelman automaattiset yksikkötestit käynnistetään seuraavasti:

```
./run_unittests.sh
```

Yksikkötesteillä testataan ohjelman pienimpiä mahdollisia yksiköitä. Tällä hetkellä ohjelman hyödyntämiä algoritmeja testataan muutamilla erilaisilla testisyötteillä. Mielenkiintoisin yksikkötesti on create_keys.py -moduulin apufunktion _create_prime_number() testaus. prime_numbers -tiedostosta löytyvät ensimmäiset 2,262 alkulukua, joihin apufunktion luomaa alkulukua voidaan verrata, kun sitä pyydetään luomaan täsmälleen 14 bitin suuruinen alkuluku (lukualueelta 0 - 16,383).