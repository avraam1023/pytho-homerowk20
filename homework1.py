#დავალება N1

import requests
import json

BASE_URL = "https://rickandmortyapi.com/api"

def fetch_characters():
    characters = []
    url = f"{BASE_URL}/character"
    
    while url:
        response = requests.get(url)
        data = response.json()
        characters.extend(data["results"])
        url = data["info"]["next"]
    
    return characters

def fetch_episode_names(episode_urls):
    episode_names = []
    for url in episode_urls:
        response = requests.get(url)
        if response.status_code == 200:
            episode_data = response.json()
            episode_names.append(episode_data["name"])
    return episode_names

def main():
    characters = fetch_characters()
    character_episodes = {}
    
    for character in characters:
        name = character["name"]
        episode_urls = character["episode"]
        print(f"Fetching episodes for: {name}")
        episode_names = fetch_episode_names(episode_urls)
        character_episodes[name] = episode_names
    
    with open("rick_and_morty_characters.json", "w", encoding="utf-8") as file:
        json.dump(character_episodes, file, ensure_ascii=False, indent=4)
    print("Data saved to rick_and_morty_characters.json")

if __name__ == "__main__":
    main()
