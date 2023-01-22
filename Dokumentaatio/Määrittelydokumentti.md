# Määrittelydokumentti

Sovellus toteuttaa Ron Rivestin, Adi Shamirin ja Len Adlemanin RSA-salausalgoritmin. Sovellus on toteutettu Python-ohjelmointikielellä ja implementoi RSA-salausalgoritmin sellaisena kuin se esiteltiin ensimmäisen kerran vuonna 1977.

Vertaisarviointia varten: Pythonin lisäksi pystyn vertaisarvioimaan tarvittaessa myös Javaa ja Groovya.

Sovelluksessa ei ole tarpeen toteuttaa erityisiä tietorakenteita, mutta RSA-algoritmin mukaisesti julkisen avaimen salausjäjestelmän avainparin luomisessa tarvitaan Miller-Rabin testiä alkuluvullisuuden varmentamiseksi, Eukleideen algoritmia kahden kokonaisluvun suurimman yhteisen tekijän löytämiseksi sekä laajennettua Eukleideen algoritmia kokonaislukujen kongruenssirelaation selvittämiseksi. Varsinaisissa salaus- ja purkuoperaatioissa käytetään Pythonin standardikirjaston valmiita suurten lukujen laskuoperaatioita, erityisesti modulaarista eksponenttifunktiota (joka on tehokas potenssiinkorotusalgoritmi tehokkaaseen salaus- ja purkuoperaatioiden suorittamiseen).

RSA-salausalgoritmi on ensimmäinen julkisen avaimen salakirjoitusjärjestelmä. Valitsin tämän algoritmin sen historiallisen merkittävyyden vuoksi, osana henkilökohtaista kiinnostustani tietoturvaan liittyviin kysymyksiin. RSA-salausalgoritmin toteuttaminen juuri vuoden 1977 alkuperäisenä versiona on myös hivenen matemaattisesti suoraviivaisempaa, koska se ei vielä sisältänyt eräitä optimointeja, joita nykyiset RSA-salausalgoritmin toteutukset hyödyntävät.

Sovellus on komentorivityökalu, joka
* luo satunnaisen salausavainparin, joka on pituudeltaan käyttäjän määrittelemä (esim. 1024 bittiä)
* luo satunnaisen salausavainparin käyttäjän syöttämien alkulukujen perusteella
* salaa annetun viestin salaisella avaimella ja purkaa julkisella
* salaa annetun viestin julkisella avaimella ja purkaa salaisella
* allekirjoittaa viestin salaisella avaimella ja varmentaa allekirjoituksen julkisella
* sisältää komentorivikäyttöliittymää laajentavan graafisen osion, joka avaa algoritmin toimintaa ja sallii sille annettujen arvojen muokkaamisen kesken algoritmin suorituksen

Sovellukselle voidaan antaa syötteinä haluttu avaimen pituus, halutut alkuluvut, joilla salausavainpari luodaan, selväkielinen viesti salattavaksi halutulla avaimella, salattu viesti purettavaksi halutulla avaimella sekä selväkielinen viesti allekirjoitettavaksi halutulla avaimella sekä allekirjoituksen varmentaminen. Graafisen käyttöliittymän läpi sovelluksessa toteutetun algoritmin voi havainnoida etenevän osissa, ja algoritmin käyttämiä arvoja voidaan halutessa muuttaa kesken suorituksen.

RSA-salausalgoritmin toteutuksessa käytetyillä yllä mainituilla algoritmeilla on omat aikavaatimuksensa, joita tässä sovelluksessa pyritään saavuttamaan. Esimerkiksi Eukleideen algoritmin pahimman tapauksen aikavaatimus on O(h), missä h on tarkasteltavista kokonaisluvuista pienemmän sisältämien numeroiden lukumäärä. Miller-Rabin testin aikavaatimus on puolestaan O(k log³ n), missä k on testissä käytettyjen iteraatioiden lukumäärä (Miller-Rabin testi on probabilistinen) ja n on tarkasteltava kokonaisluku.

Perusteellinen esitys RSA-salausalgoritmista, etenkin sen tehokkaan toteutuksen osalta, löytyy [DI Management Services](https://www.di-mgt.com.au) -yrityksen kotisivuilta.

Opinto-ohjelma: tietojenkäsittelytieteen kandidaatti (TKT)
Projektin dokumentaatiossa käytetty kieli: suomi
