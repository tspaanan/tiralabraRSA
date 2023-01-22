# Viikkoraportti 1

Ensimmäisellä viikolla aloitin työskentelyn tiistai-illasta tutustumalla alustavasti aiheeseen. Kokeilin lähteä toteuttamaan RSA-salausalgoritmiin olennaisesti kuuluvaa salausavainparien luomista kurssivuston Aiheita-sivulla linkitetyn RSA:n Wikipedia-sivun pohjalta. Tiistai-illan ja keskiviikkoaamupäivän aikana kirjoitin key-generaattorin, joka osaa laskea RSA-avaimien muodostamiseksi sopivia kokonaislukuja. Tarkalleen ottaen selvitin kaksi alkulukua sekä salauseksponentin ja purkueksponentin, joista RSA-salausalgoritmia käyttävä avainpari muodostuu. Myös GitHub-repository luotiin versiohallintaa varten.

Tässä vaiheessa toki oioin mutkia käyttämällä esimerkiksi valmista listaa alkuluvuista (ensimmäiset 2262 alkulukua), jotka ovat lähtökohtaisesti liian pieniä pätevien salausavainten muodostamiseen. Jotkin ratkaisuni tulevat kuitenkin todennäköisesti säilymään aina valmiiseen ohjelmaan asti. Päätin kokeilla luoda todellista satunnaisuutta käyttämällä Pythonin standardikirjaston secrets-moduulia itselleni tutumman pseudosatunnaisia lukuja tuottavan random-moduulin sijaan. Lisäksi toteuttamani Eukleideen algoritmi, joka pystyy etsimään kahden kokonaisluvun suurimman yhteisen tekijän, vaikuttaa sikäli valmiilta, että se toimii oikein.

Torstaina aamupäivästä jatkoin työtä tutustumalla tarkemmin RSA-salausalgoritmin toiminnallisuuteen. Löysin erinomaisen [referenssisivuston](https://www.di-mgt.com.au/rsa_alg.html), David Ireland'in luotsaaman DI Management Services -yrityksen sivuilta. Ireland keskustelee esityksessään lukuisista RSA:n implementaation yksityiskohdista, esimerkiksi erinomaisesta lähestymistavasta alkulukukandidaattien valintaan: jos halutaan lopuksi 1024 bittiä pitkä avain, arvotaan ensin 512-bittinen alkuluku ja sitten toinen, joka on pituudeltaan 512–1024 bittiä.

Lisäksi kävin kurssin ohjaajan kanssa keskustelun, jossa sain erinomaisia vinkkejä mm. Miller-Rabin testin tehostamiseksi branch-and-bound -optimoinnilla sekä varmistuksen sille, että potenssiinkorotusalgoritmien osalta tehokkaaseen salaukseen ja purkamiseen voin hyödyntää Pythonin standardikirjaston valmiita suurten lukujen laskuoperaatioita, erityisesti modulaarista eksponenttifunktiota. Lisäksi testasin niin ikään Pythonin standardikirjastoon kuuluvan argparse-moduulin toiminnallisuutta, koska sovellukseni on lähtökohtaisesti komentorivisovellus. Myös ensimmäinen versio määrittelydokumentista valmistui.

Sunnuntaina kirjoitin määrittelydokumentin uudestaan, rekisteröidyin labtoolissa sekä pohdin lisää sovelluksen arkkitehtuurista rakennetta. Suunnittelen ainakin erottavani toisistaan ohjelman toiminnan ja käyttöliittymän sekä eriyttämällä loogiset kokonaisuudet omiin moduuleihinsa. Mahdollista graafista algoritmin toiminnallisuutta havainnollistavaa käyttöliittymää varten on tärkeää, että kaikkeen ohjelman toiminnallisuuteen pääsee kätevästi käsiksi ilman komentorivikäyttöliittymää. Tästä on hyvä jatkaa seuraavaksi Miller-Rabin testin toteuttamiseen. Myös sovelluskehys testaamiseen tulisi valita, mutta aion tämän osalta hyödyntää Ohjelmistotekniikka-kurssin materiaaleja—vaikka suoritinkin sen puolitoista vuotta sitten Javalla, muistan myös Pythonin osalta kurssin sisältäneen tärkeää tehokkaaseen testausautomaatioon liittyvää materiaalia.

Suurin huolenaiheeni liittyy sen varmistamiseen, että olen ymmärtänyt RSA-salausalgoritmin toiminnan oikein. Tässä onneksi auttaa se, että avainten luonti on mahdollista jakaa selkeisiin osa-alueisiin, joita voi testata erikseen ja näin varmistaa niiden toimivan oikein. Toinen huolenaihe koskee tämän opintojakson suorittamista osittain työn ohella. Ainakin nyt ensimmäisellä viikolla pystyin käyttämään tähän sovellukseen mielestäni riittävästi työtunteja.

## Tuntikirjanpito

TI: 1,5 tuntia
KE: 4 tuntia
TO: 4 tuntia
SU: 2 tuntia
