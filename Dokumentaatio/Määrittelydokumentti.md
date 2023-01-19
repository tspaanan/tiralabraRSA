#Määrittelydokumentti

Sovellus toteuttaa Ron Rivestin, Adi Shamirin ja Len Adlemanin RSA-salausalgoritmin. Sovellus on toteutettu Python-ohjelmointikielellä sellaisena kuin se esiteltiin ensimmäisen kerran vuonna 1977.

Vertaisarviointia varten: Pythonin lisäksi pystyn vertaisarvioimaan tarvittaessa myös Javaa ja Groovya.

Sovelluksessa ei ole tarpeen toteuttaa erityisiä tietorakenteita, mutta RSA-algoritmin toteutuksessa tarvitaan Rabin-Miller testiä alkuluvullisuuden varmentamiseksi, Eukleideen algoritmia kahden kokonaisluvun suurimman yhteisen tekijän löytämiseksi, laajennettua Eukleideen algoritmia kokonaislukujen kongruenssirelaation selvittämiseksi sekä potenssiinkorotusalgoritmia tehokkaiden salaus- ja purkuoperaatioiden suorittamiseksi.

RSA-salausalgoritmi on ensimmäinen julkisen avaimen salakirjoitusjärjestelmä. Valitsin tämän algoritmin sen historiallisen merkittävyyden vuoksi, osana henkilökohtaista kiinnostustani tietoturvaan liittyviin kysymyksiin. RSA-salausalgoritmin toteuttaminen juuri vuoden 1977 alkuperäisenä versiona on myös hivenen matemaattisesti suoraviivaisempaa, koska se ei vielä sisältänyt eräitä optimointeja, joita nykyiset RSA-salausalgoritmin toteutukset hyödyntävät.

Sovellus on komentorivityökalu, joka
* luo satunnaisen salausavainparin
* luo satunnaisen salausavainparin annettujen alkulukujen perusteella
* salaa annetun viestin salaisella avaimella ja purkaa julkisella
* salaa annetun viestin julkisella avaimella ja purkaa salaisella
* allekirjoittaa viestin salaisella avaimella ja varmentaa allekirjoituksen julkisella
* sisältää komentorivikäyttöliittymää laajentavan graafisen osion, joka avaa algoritmin toimintaa ja sallii sille annettujen arvojen muokkaamisen kesken algoritmin suorituksen

Sovellukselle voidaan antaa syötteinä halutut alkuluvut, joilla salausavainpari luodaan, selväkielinen viesti salattavaksi halutulla avaimella, salattu viesti purettavaksi halutulla avaimella sekä selväkielinen viesti allekirjoitettavaksi halutulla avaimella. Graafisen käyttöliittymän läpi sovelluksessa toteutetun algoritmin voi havainnoida etenevän osissa, ja algoritmin käyttämiä arvoja voidaan halutessa muuttaa kesken suorituksen.

RSA-salausalgoritmin toteutuksessa käytetyillä yllä mainituilla algoritmeilla on omat aikavaatimuksensa, joita tässä sovelluksessa pyritään saavuttamaan.

Perusteellinen esitys RSA-salausalgoritmista, etenkin sen tehokkaan toteutuksen osalta, löytyy [DI Management Services](https://www.di-mgt.com.au) -yrityksen kotisivuilta.

Opinto-ohjelma: tietojenkäsittelytieteen kandidaatti (TKT)
Projektin dokumentaatiossa käytetty kieli: suomi
