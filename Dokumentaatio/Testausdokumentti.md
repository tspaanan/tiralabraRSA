# Testausdokumentti

| Name                |    Stmts |     Miss |   Branch |   BrPart |   Cover |
|-------------------- | -------: | -------: | -------: | -------: | ------: |
| Testit/unittests.py |       23 |        1 |        2 |        1 |     92% |
| algorithms.py       |       50 |        3 |       20 |        3 |     91% |
| create\_keys.py     |       25 |       25 |        8 |        0 |      0% |
| key\_objects.py     |        0 |        0 |        0 |        0 |    100% |
|           **TOTAL** |   **98** |   **29** |   **30** |    **4** | **68%** |

(Sama informaatio eri muodossa sisältyy myös [Testikattavuusraporttiin](https://github.com/tspaanan/tiralabraRSA/blob/main/Dokumentaatio/Coverage_report.html))

Ohjelman automaattiset yksikkötestit käynnistetään seuraavasti:

```
./run_unittests.sh
```

Yksikkötesteillä testataan ohjelman pienimpiä mahdollisia yksiköitä. Tällä hetkellä ohjelman hyödyntämiä algoritmeja testataan muutamilla erilaisilla testisyötteillä. Mielenkiintoisin yksikkötesti on create_keys.py -moduulin apufunktion _create_prime_number() testaus. prime_numbers -tiedostosta löytyvät ensimmäiset 2,262 alkulukua, joihin apufunktion luomaa alkulukua voidaan verrata, kun sitä pyydetään luomaan täsmälleen 14 bitin suuruinen alkuluku (lukualueelta 0 - 16,383).