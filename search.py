from requests_html import HTMLSession

class Search():
    def searchdata(self, title):
        url = f"https://gocdkeys.com/es/buscar/all/pc-cd-key/all?product={title}&order=&program=&tags="
        s = HTMLSession()
        r = s.get(url)
        enlace_original = "https://gocdkeys.com"
        print(r.status_code)

        busqueda = r.html.find("div.result-items", first=True)
        resultados = busqueda.find("div.media.product-result.row")
        searchList = []

        for resultado in resultados:
            titulo = resultado.find("h2.media-heading.truncate > a")
            img = resultado.find("img.media-object")
            for imagen in img:
                image = enlace_original + imagen.attrs["src"]
            for title in titulo:
                enlace = str(title.absolute_links).split("es/")
                nuevo_enlace = "https://game-price.herokuapp.com/"+ enlace[1]
                nuevo_nuevo_enlace = nuevo_enlace.replace("'}", "")

            game = {
                "Titulo": f"{title.text}",
                "Enlace": f"{nuevo_nuevo_enlace}",
                "Caratula": f"{image}"
            }

            searchList.append(game)

        return searchList
