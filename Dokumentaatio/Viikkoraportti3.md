# Viikkoraportti 3

Kolmannella viikolla toteutin Eukleideen laajennetun algoritmin, joka kahden kokonaisluvun yhteisten tekijöiden löytämisen lisäksi löytää sopivan salauseksponentin. Tällainen salauseksponentti d toteuttaa siis kongruenssirelaation d * e ≡ 1 (mod N_), missä e on aiemmin Eukleideen (laajentamattoman) algoritmin avulla sopivaksi havaittu purkueksponentti, ja N_ on kahden aivan alussa valittujen kokonaislukujen edeltävien parillisten lukujen tulo (eli kokonaisluvuilla p ja q -> (p-1) * (q-1)). Tämän toteuttamisessa hyödyin Alfred J. Menezes'in,  Paul C. van Oorschot'in ja Scott A. Vanstone'n esityksestä teoksessa _Handbook of Applied Cryptography_ (5. laitos, 2001), s. 67. Oman toteutukseni pitäisi toimia muuten oikein, mutta yhtä asiaa en vielä ymmärtänyt. Kun Eukleideen laajennettu algoritmi palauttaa aina kaksi Bézout'in koeffisienttia, miksi salauseksponentiksi sopii juuri oman toteutukseni palauttama jälkimmäinen luku? Entä silloin, kun tämä jälkimmäinen luku on negatiivinen? Nyt RSA-avainten luonnissa luon avaimet alusta lähtien uudestaan, jos tässä viimeisessä vaiheessa Eukleideen laajenettu algoritmi laskee minulle negatiivisen kokonaisluvun salauseksponentiksi. Mutta ehkäpä negatiivisesta kokonaisluvusta olisi mahdollista päästä sopivaan positiiviseen kokonaislukuun, joka sopii salauseksponentiksi, jollain tavalla?

Aloitin myös Testausdokumentin kirjoittamisen sekä kirjoitin laajennetulle Eukleideen algoritmille muutaman yksikkötestin. Mielenkiintoisin uusi yksikkötesti on create_keys.py -moduulin apufunktion _create_prime_number() testaus. Repon juuresta löytyvästä prime_numbers -tiedostosta löytyvät ensimmäiset 2,262 alkulukua, joihin apufunktion luomaa alkulukua voidaan verrata, kun sitä pyydetään luomaan täsmälleen 14 bitin suuruinen alkuluku (lukualueelta 0 - 16,383). Toinen uusi ominaisuus on siis käyttäjän komentoriviltä määrittelemä salausavaimen pituus bitteinä, jonka vaatima parametrisointi sopii näin näppärästi myös testiautomaation käyttöön. Käytössä on nyt myös pylint-tyylintarkistustyökalu, joka on myös integroitu käyttämääni IDE-kehitysympäristöön (Visua Studio Code).

Tulevalla viikolla on jo mahdollista kirjoittaa integraatiotestejä, kun RSA-avainten luominen on valmista. Integraatiotestissä tulen siis testaamaan create_key.py -moduulin ja algorithms.py -moduulin yhteispeliä: testi läpäistään, jos nämä moduulit pystyvät tuottamaan kelvollisen RSA-salausavainparin. Avainten tallennusta varten kirjoitin sisältöä jo aiemmin luomaani key_objects.py -moduuliin, jossa avaimet kuvataan olio-ohjelmoinnin mukaisesti luokkina. Seuraava toiminnallisuus on (ensi alkuun korkeintaan avaimen mittaisten) viestien salaaminen ja purkaminen. Tähän suunnittelen käyttäväni jotain yksinkertaista enkoodausmenetelmää, kenties viestin sisällön puristamista ASCII-merkistöön ja näiden numeroarvojen käyttämistä sellaisenaan.

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