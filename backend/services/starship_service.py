from flask import jsonify
import requests

class StarshipService:

    def get_list_of_all_starships(self, starships_url):
        first_page_of_starship_data = self.get_starships_response(starships_url)
        list_of_sharships = first_page_of_starship_data["results"]
        next_page_url = first_page_of_starship_data["next"]

        while next_page_url is not None:
            next_page_of_starship_data = self.get_starships_response(next_page_url)

            list_of_sharships += next_page_of_starship_data["results"]

            next_page_url = next_page_of_starship_data["next"]

        return list_of_sharships
 
    def get_starships_response(self, starships_url):
        return requests.get(starships_url).json()

    def get_starships_by_manufacturer(self, list_of_all_starships, manufacturer):
        return [starship for starship in list_of_all_starships if starship["manufacturer"] == manufacturer]
