# Viikkoraportti 6

Kuudennalla viikolla sain koko projektin taas tasapainoiseen tilaan, missä kaikkia toteutettuja toiminnallisuuksia myös testataan perusteellisesti. Erityisesti automaattisesti ajettavat yksikkötestit käyttävät nyt suuria kokonaislukuja ja koko ohjelmiston end2end-testit liki avaimen mittaisia merkkijonoja viestien salaamisen ja purkamisen testaamisessa. Koska tällä viikolla oli myös mahdollista käyttää muutama tunti enemmän projektin parissa, ehdin toteuttaa (ja testata) myös uusia toiminnallisuuksia. RSA-avainparien luonnin yhteydessä on nyt mahdollista --verify komentoriviparametrilla ajaa useita kierroksia E2E-testien tapaisia varmistuksia. Nämä varmistukset toteutin hyödyntämällä unittest-kirjastoa, jonka toiminnasta opin samalla uutta. Ylimääräiset tulostukset voi esimerkiksi kätevästi piilottaa käyttäjältä, kun automaattisten testien tulokset ohjataan io.StringIO -virtaan, jonka voi kadottaa bittiavaruuteen niin pian kuin unittest-moduulilta on käyty katsastamassa wasSuccessful() metodin antama tuomio.

Toinen uusi (perusteellisesti testattu) toiminnallisuus on RSAES-PKCS1-v1_5 -standardin mukainen satunnainen salattavan viestin täyttäminen (random padding), joka on nyt oletusarvoisesti käytössä ellei käyttäjä erikseen valitse käyttää --no_padding komentoriviparametria. Paljon muitakin pieniä tarkennuksia ehdittiin tehdä. Jopa kahden sekunnin suorituskykyparannus saatiin aikaan (1024-bittisten avainparien kanssa), kun Miller-Rabin testissä käytetään nyt esikarsintaa, jossa koetetaan jakaa alkulukukandidaattia korkeintaan 500. ensimmäisellä alkuluvulla.

Vertaisarvioinnin tekemistä varten varasin vielä kaksi ylimääräistä tuntia tällä viikolla. Toisen opiskelijan koodia lukemalla opin taas uutta ja hyödyllistä Pythonista (enumerate() metodi matriisien kätevään läpikäymiseen!).

Viimeiselle viikolla jäävät siten vertaisarvioitsijoiden ehdottamat parannukset mm. koodikattavuuden laskemisen automatisoimiseksi GitHub Actions'in avulla sekä dokumentaatioon tehtävät tarkennukset. Lähtökohtaisesti dokumentaatio on ollut ihan hyvällä mallilla, mutta erityisesti oikeellisuustestauksen avaaminen testausdokumentissa on hyvä saada kuntoon, kuten viimeisin vertaisarvioitsija oikein kehottikin tekemään. 

## Tuntikirjanpito

| Viikko 1 ||
|---|---|
| TI | 1,5 tuntia |
| KE | 4 tuntia |
| TO | 4 tuntia |
| SU | 2 tuntia |

| Viikko 2 ||
|---|---|
| KE | 3 tuntia |
| TO | 4 tuntia |
| SU | 2 tuntia |

| Viikko 3 ||
|---|---|
| KE | 3 tuntia |
| TO | 3 tuntia |
| SU | 1 tunti |

| Viikko 4 ||
|---|---|
| KE | 3 tuntia |
| TO | 3 tuntia |
| SU | 0,5 tuntia |

| Viikko 5 ||
|---|---|
| KE | 3 tuntia |
| TO | 4 tuntia |
| LA | 1 tunti |

| Viikko 6 ||
|---|---|
| KE | 4 tuntia |
| TO | 4 tuntia |
| LA | 2 tuntia |
| SU | 1 tunti |