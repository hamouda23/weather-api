#!/usr/bin/env python3
"""
Explorer les données disponibles dans l'API
"""

import requests
import json

def explore_api():
    """Affiche toutes les clés disponibles dans la réponse API"""
    
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": 45.5017,
        "longitude": -73.5673,
        "current_weather": True,
        "hourly": ["temperature_2m", "relative_humidity_2m", "precipitation"]
    }
    
    response = requests.get(url, params=params, timeout=10)
    data = response.json()
    
    print("=" * 50)
    print("🔍 EXPLORATION DE L'API")
    print("=" * 50)
    
    # 1. Voir toutes les clés principales
    print("\n📁 CLÉS PRINCIPALES:")
    for key in data.keys():
        print(f"  - {key}")
    
    # 2. Explorer chaque section
    print("\n" + "=" * 50)
    print("📊 DÉTAIL PAR SECTION")
    print("=" * 50)
    
    for key, value in data.items():
        print(f"\n🔹 {key}:")
        if isinstance(value, dict):
            print(f"   Type: dictionnaire")
            print(f"   Clés: {list(value.keys())}")
        elif isinstance(value, list):
            print(f"   Type: liste ({len(value)} éléments)")
            if len(value) > 0:
                print(f"   Exemple: {value[:3]}...")  # Montre les 3 premiers
        else:
            print(f"   Valeur: {value}")
    
    # 3. JSON complet (optionnel, commenté)
    # print("\n📄 JSON COMPLET:")
    # print(json.dumps(data, indent=2))
    
    print("\n" + "=" * 50)

if __name__ == "__main__":
    explore_api()
