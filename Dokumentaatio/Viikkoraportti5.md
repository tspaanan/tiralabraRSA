# Viikkoraportti 5

Viidennellä viikolla onnistuin lukemaan [RFC 8017](https://www.rfc-editor.org/rfc/rfc8017) -dokumenttia siten, että RSAES-PKCS1-v1_5 -standardin mukainen satunnainen salattavan viestin täyttäminen (random padding) onnistuu sekä salaus- että purkuoperaatioiden kanssa. Koodi on vielä proof of concept -asteella, mutta koska perusidea toimii, pitäisi tämän toiminnallisuuden linkittäminen normaalien salaus- ja purkuoperaatioiden yhteyteen olla suhteellisen suoraviivaista. Tässä kohtaa on myös tarpeen pistää stoppi uusien ominaisuuksien lisäämiselle. Sovellus on nimittäin alkanut kallistua etupainotteiseksi siten, että kaikkia ominaisuuksia ei ole vielä ehditty kattavasti testata eikä dokumentaatiokaan ole pysynyt ajan tasalla: vertaisarvioitsija ei ollut saanut purkuoperaatiota toimimaan antamieni ohjeiden mukaisesti, koska olin unohtanut päivittää ne lisäämäni --output komentoriviparametrin implementoinnin jälkeen! Myös vertaisarviointi vei hyvän siivun tällä viikolla vapaasta, tähän kurssiin käytettävissä olevasta ajasta.

Kun uusia ominaisuuksia ei ole juuri nyt tulossa, on seuraavalla viikolla mahdollista keskittyä algoritmien oikeellisuustestaamiseen sekä olemassaolevien ominaisuuksien hiomiseen ohjelman käytön sujuvoittamiseksi. Oikeellisuustestaamiseen sain tällä viikolla perusteellista ohjausta, jota seuraten uskon asian olevan kunnossa. Perusperiaate testaamisessa on käyttää mahdollisimman "autenttista" testisyötettä, mikä tarkoittaa esim. Miller-Rabin -testin osalta hyvin suurien alkulukujen ja ei-alkulukujen käyttämistä sekä E2E-testauksen osalta lähes avaimen mittaisten merkkijonojen salaamisen ja purkamisen varmistamista.

Lisäksi seuraavalla viikolla olisi hyvä toteuttaa eräs quality of life -parannus eli GitHub Actions'in valjastaminen ajamaan testit ja laskemaan testikattavuusraportit automaattisesti aina uusien koodimuutosten myötä. Tähän sain erinomaisen vinkin oman projektini vertaisarvioijalta.

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