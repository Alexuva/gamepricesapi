from fastapi import FastAPI
from search import Search
from game import Game

app = FastAPI()

look = Search()

juego = Game()

@app.get("/")
async def bienvenido:
    return [
        {
            "Bienvenido": "Introduce 'search/EL JUEGO QUE QUIERAS BUSCAR'"
        }
    ]


@app.get("/search/{title}")
async def read_item(title):
    try:
        return look.searchdata(title)
    except:
        return [
            {
                "Error": "No se ha encontrado ningún título"
            }
        ]


@app.get("/{url}")
async def read_item(url):
    try:
        return juego.titledata(url)
    except:
        return [
            {
                "Error" : "No se han encontrado tiendas"
            }
        ]

