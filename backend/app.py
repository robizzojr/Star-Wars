from flask import Flask, request, jsonify
from flask_cors import CORS
from services.starship_service import StarshipService

app = Flask(__name__)
app.config.from_object(__name__)

get_all_starships_url = "https://swapi.dev/api/starships/"

CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/live', methods=['GET'])
def health_check():
    return jsonify('Star Wars app is up and running')

@app.route('/starships', methods=['GET'])
def get_all_starships():
    starship_service = StarshipService()

    return jsonify(
        {
            "starships": starship_service.get_list_of_all_starships(get_all_starships_url)
        }
    )

@app.route('/starships/<manufacturer>', methods=['GET'])
def get_starships_by_manufacturer(manufacturer = None):
    starship_service = StarshipService()

    list_of_all_starships = starship_service.get_list_of_all_starships(get_all_starships_url)

    return jsonify(
        {
            "starships": starship_service.get_starships_by_manufacturer(list_of_all_starships, manufacturer)
        }
    )

if __name__ == '__main__':
    app.run(debug=True)
