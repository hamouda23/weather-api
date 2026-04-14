#!/usr/bin/env python3
"""
Weather API - Étape 1
Apprendre à faire des requêtes HTTP et parser du JSON
"""

import requests
import json

# API Open-Meteo (gratuite, pas besoin de clé API !)
# Documentation: https://open-meteo.com/

def get_weather(latitude, longitude):
    """
    Récupère la météo actuelle pour une position donnée
    
    Args:
        latitude (float): Latitude de la position
        longitude (float): Longitude de la position
    
    Returns:
        dict: Données météo ou None en cas d'erreur
    """
    
    # URL de l'API avec les paramètres
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current_weather": True  # On veut juste la météo actuelle
    }
    
    print(f"📡 Appel API: {url}")
    print(f"📍 Position: {latitude}, {longitude}")
    
    try:
        # FAIRE LA REQUÊTE HTTP GET
        response = requests.get(url, params=params, timeout=10)
        
        # Vérifier si la requête a réussi (code 200)
        response.raise_for_status()
        
        # PARSER LE JSON
        data = response.json()
        
        print("✅ Requête réussie !\n")
        return data
        
    except requests.exceptions.RequestException as e:
        print(f"❌ Erreur de requête: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"❌ Erreur de parsing JSON: {e}")
        return None


def display_weather(data):
    """
    Affiche les données météo de façon lisible
    
    Args:
        data (dict): Données JSON de l'API
    """
    
    if not data or "current_weather" not in data:
        print("⚠️  Pas de données météo disponibles")
        return
    
    weather = data["current_weather"]
    
    print("=" * 40)
    print("🌤️  MÉTÉO ACTUELLE")
    print("=" * 40)
    print(f"🌡️  Température: {weather.get('temperature', 'N/A')}°C")
    print(f"💨 Vent: {weather.get('windspeed', 'N/A')} km/h")
    print(f"🧭 Direction: {weather.get('winddirection', 'N/A')}°")
    print(f"🕐 Heure: {weather.get('time', 'N/A')}")
    print(f"🌤️  Code météo: {weather.get('weathercode', 'N/A')}")
    print("=" * 40)


def main():
    """Fonction principale"""
    
    print("🌤️  Weather API - Étape 1\n")
    print("Apprendre les bases des APIs HTTP\n")
    
    # Coordonnées de Montréal (tu peux changer !)
    lat = 45.50884  #45.5017
    lon = -73.58781 #-73.5673
    
    # 1. Appeler l'API
    data = get_weather(lat, lon)
    
    # 2. Afficher les résultats
    if data:
        display_weather(data)
        
        # 3. (Optionnel) Voir le JSON brut
        print("\n📄 JSON brut (premières lignes):")
        print(json.dumps(data, indent=2)[:500] + "...")


if __name__ == "__main__":
    main()
