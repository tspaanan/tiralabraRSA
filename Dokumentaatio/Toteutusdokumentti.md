# Toteutusdokumentti

## Ohjelman yleisrakenne

Ohjelma toimii erilaisten komentoriviltä annettujen nimettyjen parametrien pohjalta. Komentorivitoiminnallisuuden toteutuksessa on käytetty Pythonin argparse-moduulia.

Ohjelman toiminnallisuus on jaoteltu eri moduuleihin, joista tärkeimmät ovat komentorivikäyttöliittymästä vastaava tiralabraRSA_CLI.py, algoritmit sisältävä algorithms.py, avainten luomisesta vastaava create_keys.py, sekä salaus- ja purkutoiminnallisuuden hoitava encryptions.py.

## Saavutetut aika- ja tilavaativuudet

Eukleideen algoritmin pahimman tapauksen aikavaatimus on O(h), missä h on tarkasteltavista kokonaisluvuista pienemmän sisältämien numeroiden lukumäärä.

Miller-Rabin testin pahimman tapauksen aikavaatimus on O(k log³ n), missä k on testissä käytettyjen iteraatioiden lukumäärä ja n on tarkasteltava kokonaisluku.

## Lähteet

Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest ja Clifford Stein. _Introduction to Algorithms_ (3. laitos, 2009), ss. 968–971.
Alfred J. Menezes,  Paul C. van Oorschot ja Scott A. Vanstone. _Handbook of Applied Cryptography_ (5. laitos, 2001), s. 67.