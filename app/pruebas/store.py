import requests

def get_categories():
    try:
        r = requests.get('https://api.escuelajs.co/api/v1/categories')
        
        # Verifica si la respuesta fue exitosa (código 200)
        if r.status_code == 200:
            categories = r.json()
            for category in categories:
                print(category['name'])
        else:
            print(f"Error: {r.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error en la solicitud: {e}")
