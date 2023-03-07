# Käyttöohje

Ohjelman komentorivikäyttöliittymä toimii samalla periaatteella kuin tavanomaiset Unix-työkalut. Sen toimintaa ohjataan komentoriviparametreilla, jotka ovat muotoa `--komentoriviparametri` (toistaiseksi näillä pitkillä muodoilla ei ole vaihtoehtoisia lyhyitä muotoja, kuten `-km`). *Huomaa shell-tulkkien rajoitteet*: esim. Bash vaatii välilyöntien yhteydessä lainausmerkkien käytön (muuten välilyönti tulkitaan parametrin loppumiseksi) eikä sen erikoismerkkejä (kuten '!') voi lainkaan käyttää esim. viestin osana, kun se annetaan suoraan komentoriviltä. Erikoisempia merkkejä sisältävät viestit voi kuitenkin kirjoittaa tiedostoon, josta viestin voi lukea `--input` parametrilla.

Shell-skripti _tiralabraRSA_ passaa annetut komentoriviparametrit edelleen varsinaiselle komentorivikäyttöliittymälle. Ellet halua kutsua tätä muodossa `./tiralabraRSA`, lisää ohjelman kansio väliaikaisesti PATH-muuttujaan: `export PATH="$PATH:."`. Shell-skripti on myös määritettävä ajettavaksi: `chmod +x tiralabraRSA`.

* Uusien RSA-avainten luominen
```
tiralabraRSA --create_keys --key_length 1024 --verify
```

Ohjelma luo satunnaisen RSA-avainparin, joka tallennetaan tiedostoihin _secret_key_ ja _public_key_. Parametri `--verify` varmistaa, että luodut avaimet toimivat, antaen muutoin virheilmoituksen. Avaimen pituus on bitteinä eikä sillä ole ylärajaa. 4096 bittiä pidetään kuitenkin yleisesti kvanttilaskennankestävänä valintana.

* Viestin salaaminen
```
tiralabraRSA --encrypt --key public_key --message "selväkielinen viesti" --output encrypted_message
```

Ohjelma salaa merkkijonon 'selväkielinen viesti' salausavaimella _public_key_. Salattu sisältö tallennetaan tiedostoon _encrypted_message_. Salattavan viestin voi antaa myös parametrilla `--input "tiedoston nimi"`, jolloin salattava viesti luetaan tiedostosta _tiedoston nimi_.

Salauksessa voi myös käyttää havainnollistamistarkoituksessa `--no_padding` komentoriviparametria, joka kytkee satunnaisen täytön pois päältä.

* Viestin purkaminen
```
tiralabraRSA --decrypt --key secret_key --input encrypted_message --output screen
```

Ohjelma purkaa tiedoston _encrypted_message_ tekstimuotoisen sisällön salausavaimella _secret_key_. Selväkielinen viesti tulostetaan näytölle. `--output` komentoriviparametrilla voi myös antaa halutun tiedoston nimen, jolloin purettu viesti kirjoitetaan tähän tiedostoon.
