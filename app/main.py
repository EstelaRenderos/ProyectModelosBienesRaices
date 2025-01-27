from pruebas.store import get_categories
from pruebas.Test_Modelo import generar_graficas
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
app = FastAPI()

# Define un endpoint que devuelve una lista.
@app.get('/')
def get_list():
    return [1, 2, 3]

# Define un endpoint HTML.
@app.get('/contact', response_class=HTMLResponse)
def get_contact():
    return """
        <h1>Hola, soy una página</h1>
        <p>Soy un párrafo</p>
    """

# Ejecuta las funciones necesarias al iniciar la aplicación.
def run():
    get_categories() 

if __name__ == '__main__':
    run()
    generar_graficas("pruebas/img/grafica_logaritmica.png", "pruebas/img/grafica_exponencial.png")

     
