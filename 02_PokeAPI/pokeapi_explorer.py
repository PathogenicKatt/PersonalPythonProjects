"""
PokeAPI Explorer - Learning HTTP Requests with Pokemon Data
"""

import requests

class PokeAPI:
    base_url = "https://pokeapi.co/api/v2/"

    def get_pokemon(self, name):
        """Fetches data for a specific Pokemon by name."""
        response = requests.get(f"{self.base_url}pokemon/{name.lower()}")
        if response.status_code == 200:
            return response.json()
        else:
            return None
        
def main():
    api = PokeAPI()
    pokemon_name = input("Enter the name of a Pokemon: ")
    data = api.get_pokemon(pokemon_name)
    
    if data:
        print(f"Name: {data['name'].title()}")
        print(f"ID: {data['id']}")
    else:
        print("Pokemon not found. Please check the name and try again.")

if __name__ == "__main__":
    main()