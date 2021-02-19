import requests
from bs4 import BeautifulSoup
import datetime


class Articolo:
    """Articolo con titolo, data, descrizione, immagine e link."""

    def __init__(
            self, titolo: str, data: str, descrizione: str, immagine: str, link: str
    ) -> None:
        self.titolo = titolo
        self.data = datetime.datetime.fromisoformat(data)
        self.descrizione = descrizione
        self.immagine = immagine
        self.link = link

    def __str__(self) -> str:
        return f'''Titolo: {self.titolo}
        Descrizione: {self.descrizione}
        Data: {self.data.date()}
        Immagine: {self.immagine}
        Link: {self.link}'''


def get_articoli() -> list[Articolo]:
    """Restituisce la lista degli articoli presenti sul sito di RomaTre, dal più recente al più vecchio."""

    # Scarica il sito
    result = requests.get(
        "https://ingegneria.uniroma3.it/it/archivi/channel/in-evidenza-14/",
        verify=False,
    )

    # Beautifulsuppa il sito
    soup = BeautifulSoup(result.content, features="html.parser")

    # Inizializza lista di articoli
    articoli = []

    # Aggiunge articoli alla lista
    for articolo in soup.find_all("article"):
        link = articolo.header.h2.a.attrs["href"]
        titolo = articolo.header.h2.a.text
        immagine = articolo.div.figure.a.img.attrs["src"]
        descrizione = articolo.find_all("div")[1].find_all("div")[1].text
        data = articolo.footer.span.time.attrs["datetime"]

        articoli.append(Articolo(titolo, data, descrizione, immagine, link))

    return articoli
