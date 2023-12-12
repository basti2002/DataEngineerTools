import scrapy
from projet_scrapy.items import PokemonItem

class PokemonSpider(scrapy.Spider):
    name = "pokemon"
    start_urls = ['https://www.pokepedia.fr/Liste_des_Pokémon_de_la_quatrième_génération']

    def parse(self, response):
        # XPath pour extraire toutes les lignes de la table
        pokemon_nodes = response.xpath('//table[2]/tbody/tr')

        for pokemon_node in pokemon_nodes:
            # Extraire le nom du Pokémon à partir de chaque ligne (tr)
            pokemon_name = pokemon_node.xpath('td[3]/a/text()').get()

            # Extraire le type du Pokémon à partir des span dans le lien a | td[8] premier type de la première forme et td[7] type des autres formes de ce pokemons
            type_nodes = pokemon_node.xpath('td[8]/span/a | td[7]/span/a')

            # Extraire le type de chaque forme du pokemon
            type_values = [t.xpath('@title').get() for t in type_nodes] if type_nodes else []

            print("Nom du Pokémon :", pokemon_name)
            print("Types du Pokémon :", type_values)

            yield {'nom': pokemon_name, 'types': type_values}
