# Dans le fichier items.py
import scrapy

class PokemonItem(scrapy.Item):
    nom = scrapy.Field()
