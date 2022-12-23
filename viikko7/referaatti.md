## Ohjelmistoarkkitehtuurin sisällyttäminen ketteriin ohjelmistotuotantomenetelmiin

Ketterän kehityksen yleistyminen on tuonut haasteita ohjelmistoarkkitehtuurin kehittämiseen: arkkitehtuurille ei enää varata omaa työskentelyjaksoa vesiputousmallin tavoin, vaan se syntyy pikkuhiljaa muun ohjelmiston lomassa.

Kritiikki ketterää kehitystä ja sen arkkitehtuurinkehitysmenetelmää vastaan kohdistuu pitkälti inkrementaalisen arkkitehtuurimallin työstämisen vaikeuteen. Arkkitehtuurin vähittäinen rakentaminen vaatii kokenutta ohjelmoijaa, mikäli halutaan välttää suuret määrät refaktorointia. Tämän lisäksi arkkitehtuurivetoisissa menetelmissä on ollut tapana selvittää ympäristön ja kohdelaitteiston rajoitteet, mille ketterät menetelmät eivät anna arvoa ennen kuin ohjelmointi on jo aloitettu.

Ketteriin ohjelmistotuotantomenetelmiin on kuitenkin kehitelty niihin soveltuvia toimintatapoja arkkitehtuurin suunnittelemiseksi. Esimerkiksi scrumissa usein hyödynnettävä *sprint 0* antaa vaihtoehdon karkean arkkitehtuurin suunnittelulle. Tämä ei olisi lopullinen ohjelmiston rakenne, mutta antaa ohjelmistonkehitysryhmälle pohjan, jolta lähteä toteuttamaan varsinaista ohjelmistoa.

Muita vaihtoehtoja on arkkitehtuurin eriyttäminen omaksi prosessikseen, jota edistetään muun työskentelyn tarpeiden mukaan asialle vihkiytyneiden arkkitehtien toimesta; *suunnittelupiikit* tai *arkkitehtuurijaksot*, joiden aikana työryhmä keskittyy ohjelmiston rakenteeseen ja laajennettavuuteen sekä viidentenä mallina *arkkitehtuuritarinat*, jotka kuvaavat ohjelmistonkehittäjien tarpeita ja auttavat estimoimaan ja käyttämään sovelluksen rakennetta vaativiin toimiin tarvittavaa työaikaa.

Ei ole olemassa yhtä selkeästi parasta menetelmää, eikä työryhmän tarvitse rajoittua vain yhteen edellisistä. Useamman menetelmän ottaminen osaksi työskentelytapoja voi kuitenkin tapahtua ketteryyden kustannuksella, mitä tulee varoa, jos aikoo pitää prosessinsa ketteränä. Toisaalta ketterän kehityksen julistus edellyttää prosessin mukauttamista työryhmän mukaan, minkä nojalla työryhmän kannattaakin harkita riittävän painoarvon antamista arkkitehtuurille.
