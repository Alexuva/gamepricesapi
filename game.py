from requests_html import HTMLSession

class Game():

    def titledata(self, url):
        s = HTMLSession()
        urlfinal = "https://gocdkeys.com/es/"+url
        r = s.get(urlfinal)
        print(r.status_code)

        lista_tiendas = r.html.find(".p-store-list > tbody > tr")

        shop_list = []

        for tienda in lista_tiendas:
            tiendaAttr = tienda.attrs
            if "itemprop" in tiendaAttr:
                local = tienda.find("meta", first=True)
                nombre_local = local.attrs["content"]
                region = tienda.find(".p-store-region", first=True).text
                precios = tienda.find(".p-store-price", first=True)
                precio = precios.find("b", first=True).text
                enlaces = tienda.absolute_links
                enlace_compra = ""
                for enlace in enlaces:
                    if "https://gocdkeys.com/es/ir/" in enlace:
                        enlace_compra = enlace

                juego = {
                    "Tiendas": [
                        {
                            "Nombre": f"{nombre_local}",
                            "Region": f"{region}",
                            "Precio": f"{precio}",
                            "Enlace": f"{enlace_compra}"
                        }
                    ]
                }

                shop_list.append(juego)

        return shop_list

juego = Game()

juego.titledata("comprar-victoria-3-pc-cd-key")