# Toteutusdokumentti

## Ohjelman yleisrakenne

Ohjelma toimii erilaisten komentoriviltä annettujen nimettyjen parametrien pohjalta. Komentorivitoiminnallisuuden toteutuksessa on käytetty Pythonin argparse-moduulia. Komentorivikäyttöliittymä on lisäksi kehystetty tiralabraRSA-skriptillä, jonka avulla ohjelman käyttö näyttää samalta kuin tavanomaisten Unix-työkalujen käyttö.

Ohjelman toiminnallisuus on jaoteltu eri moduuleihin, joista tärkeimmät ovat komentorivikäyttöliittymästä vastaava tiralabraRSA_CLI.py, algoritmit sisältävä algorithms.py, avainten luomisesta vastaava create_keys.py, sekä salaus- ja purkutoiminnallisuuden hoitava encryptions.py.

## Saavutetut aika- ja tilavaativuudet

Eukleideen algoritmin pahimman tapauksen aikavaatimus on O(h), missä h on tarkasteltavista kokonaisluvuista pienemmän sisältämien numeroiden lukumäärä.

Miller-Rabin testin pahimman tapauksen aikavaatimus on O(k log³ n), missä k on testissä käytettyjen iteraatioiden lukumäärä ja n on tarkasteltava kokonaisluku.

Koska ohjelman käyttämien algoritmien implementoinnissa on seurattu tarkkaan alla mainittuja lähteitä, ne saavuttavat nämä aikavaativuudet.

Aika- ja tilavaativuuksia merkittävämpää on kuitenkin RSA-salausavainten oikeellisuustestaus, johon testiautomaatio keskittyy.

## Työn parannusehdotukset

Määrittelydokumentissa kuvatusta ohjelmasta jäi ennen muuta puuttumaan upea graafinen käyttöliittymä. Tämän olisi voinut rakentaa esimerkiksi [Urwid](https://urwid.org)-kirjaston päälle.

## Lähteet

Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest ja Clifford Stein. _Introduction to Algorithms_ (3. laitos, 2009), ss. 968–971.
Alfred J. Menezes,  Paul C. van Oorschot ja Scott A. Vanstone. _Handbook of Applied Cryptography_ (5. laitos, 2001), s. 67.
[RFC 8017](https://www.rfc-editor.org/rfc/rfc8017#section-7.2).

Yleiskuva eri aiheista sekä linkit yllä mainittuihin lähteisiin ovat pääsääntöisesti löytyneet Wikipedian aihekohtaisilta sivuilta.

Kattavin yleisesitys aiheesta sekä lukuisia vinkkejä sen teknisen toteutuksen yksityiskohdista ovat löytyneet David Ireland'in luotsaaman [DI Management Services](https://www.di-mgt.com.au) -yrityksen kotisivuilta.