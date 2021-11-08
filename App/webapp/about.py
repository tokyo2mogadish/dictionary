import justpy as jp

class About:
    path = '/about' #path je class variable jer ce biti ista kod svih instanci nema smisla da bude u initu
    def serve(self):
        wp = jp.QuasarPage(tailwind = True)
        div = jp.Div(a = wp, classes = 'bg-gray-200 h-screen')
        jp.Div(a=div, text='This is About page', classes = 'text-4xl m-2')
        jp.Div(a=div, text = """
        Lorem ipsum dolor sit amet, consectetur adipiscing elit,
        sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
        Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris 
        nisi ut aliquip ex ea commodo consequat. 
        Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
        Excepteur sint occaecat cupidatat non proident,
        sunt in culpa qui officia deserunt mollit anim id est laborum.
        """, classes= "text-lg")
        return wp

#rout this class to that path
# jp.Route(About.path, About.serv)# ovo smo zakomentarisali jer ne zelim dve zasebne akcije vec jednu, to cemo vrapovati mejnom 
# jp.justpy(port=8001)
