# Toteutusdokumentti

## Ohjelman yleisrakenne

Ohjelma toimii erilaisten komentoriviltä annettujen nimettyjen parametrien pohjalta. Komentorivitoiminnallisuuden toteutuksessa on käytetty Pythonin argparse-moduulia.

* Uusien RSA-avainten luominen
```
python3 tiralabraRSA_CLI.py --create_keys --key_length 1024
```

Ohjelma luo satunnaisen RSA-avainparin, joka tallennetaan tiedostoihin secret_key ja public_key.

* Viestin salaaminen
```
python3 tiralabraRSA_CLI.py --encrypt --key public_key --message clear_text_message --output encrypted_message
```

Ohjelma salaa merkkijonon 'clear_text_message' salausavaimella public_key. Salattu sisältö tallennetaan tiedostoon encrypted_message.

* Viestin purkaminen
```
python3 tiralabraRSA_CLI.py --decrypt --key secret_key --input encrypted_message --output decrypted_message
```

Ohjelma purkaa tiedoston encrypted_message tekstimuotoisen sisällön salausavaimella secret_key. Selväkielinen viesti tulostetaan näytölle.

Ohjelman toiminnallisuus on jaoteltu eri moduuleihin, joista tärkeimmät ovat komentorivikäyttöliittymästä vastaava tiralabraRSA_CLI.py, algoritmit sisältävä algorithms.py, avainten luomisesta vastaava create_keys.py, sekä salaus- ja purkutoiminnallisuuden hoitava encryptions.py.

## Saavutetut aika- ja tilavaativuudet

Eukleideen algoritmin pahimman tapauksen aikavaatimus on O(h), missä h on tarkasteltavista kokonaisluvuista pienemmän sisältämien numeroiden lukumäärä.

Miller-Rabin testin pahimman tapauksen aikavaatimus on O(k log³ n), missä k on testissä käytettyjen iteraatioiden lukumäärä ja n on tarkasteltava kokonaisluku.

## Lähteet

Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest ja Clifford Stein. _Introduction to Algorithms_ (3. laitos, 2009), ss. 968–971.
Alfred J. Menezes,  Paul C. van Oorschot ja Scott A. Vanstone. _Handbook of Applied Cryptography_ (5. laitos, 2001), s. 67.