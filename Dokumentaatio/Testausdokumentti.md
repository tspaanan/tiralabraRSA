# Testausdokumentti

| Name                |    Stmts |     Miss |   Branch |   BrPart |   Cover |
|-------------------- | -------: | -------: | -------: | -------: | ------: |
| algorithms.py       |       58 |        2 |       31 |        2 |     96% |
| create\_keys.py     |       34 |        0 |       12 |        0 |    100% |
| encryptions.py      |       30 |        0 |       10 |        2 |     95% |
| key\_objects.py     |       20 |        0 |        0 |        0 |    100% |
| message\_objects.py |        6 |        1 |        0 |        0 |     83% |
|           **TOTAL** |  **148** |    **3** |   **53** |    **4** | **97%** |

(Sama informaatio eri muodossa sisältyy myös [Testikattavuusraporttiin](https://github.com/tspaanan/tiralabraRSA/blob/main/Dokumentaatio/Coverage_report.html))

Ohjelman testiautomaatiossa käytetään unittest-kirjastoa.

Ohjelman automaattiset yksikkötestit käynnistetään seuraavasti`(Shell-skripti on ensin määritettävä ajettavaksi: `chmod +x run_unittests.sh`):

```
./run_unittests.sh
```

Yksikkötesteillä testataan ohjelman pienimpiä mahdollisia yksiköitä. Tällä hetkellä ohjelman hyödyntämiä algoritmeja testataan sekä pienillä että suurilla kokonaisluvuilla että merkkijonoilla, joiden pituus on liki testissä käytetyn avaimen mittainen. Mielenkiintoisin yksikkötesti on create_keys.py -moduulin apufunktion _create_prime_number() testaus. prime_numbers -tiedostosta löytyvät ensimmäiset 2,262 alkulukua, joihin apufunktion luomaa alkulukua voidaan verrata, kun sitä pyydetään luomaan täsmälleen 14 bitin suuruinen alkuluku (lukualueelta 0 - 16,383). Lisäksi Miller-Rabin testiä testataan Bellin alkuluvuilla sekä näiden tulolla (joka ei ole alkuluku).

Kaikki ohjelman testiautomaatio ajetaan seuraavasti (Shell-skripti on ensin määritettävä ajettavaksi: `chmod +x run_alltests.sh`):

```
./run_alltests.sh
```

Merkittävin pitkä testi on koko ydintoiminnallisuuden end-to-end testaus, jossa testataan avainten luomista ja näin luotujen avainten käyttämistä testiviestin salaamiseen ja purkamiseen. Testit/endtoendtests.py -moduuliin eriytetyt testit luovat satunnaisen 1024-bittisen RSA-salausavainparin, ja selvittävät sitten niiden soveltuvuuden testiviestin salaamiseen ja purkamiseen: ensin salataan salatulla avaimella ja puretaan julkisella, sitten toisinpäin. Testaamisessa käytetyt merkkijonot ovat liki avaimen mittaisia.

Lisäksi avainten luomisen yhteydessä voidaan `--verify` komentoriviparametrilla ajaa erityiset verifikaatiotestit, joissa hyödynnetään unittest-kirjastoa myös ohjelman käytön aikana, vastaluotujen RSA-avainten toiminnallisuuden varmistamiseksi.

Nämä end-to-end testit varmistavat RSA-avainparin oikeellisuuden: sen, että avainparin muodostavilla kolmella kokonaisluvulla (modulus, ensimmäisen avaimen eksponentti, toisen avaimen eksponentti) on se modulaariaritmeettinen ominaisuus, että kokonaisluku x korotettuna ensimmäisen avaimen eksponenttiin, josta otetaan jakojäännös moduluksella, voidaan palauttaa takaisin kokonaisluvuksi x korottamalla edellisen laskutoimituksen vastaus toisen avaimen eksponenttiin, josta otetaan jakojäännös moduluksella.