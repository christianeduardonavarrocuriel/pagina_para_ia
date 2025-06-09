import web

urls = (
    '/', 'Mi_IA'
)

render = web.template.render('templates')
app = web.application(urls, globals())

class Mi_IA:

    def __init__(self):
        pass

    def GET(self):
        return render.generate()
    
    def POST(Self):
        formulario= web.input()
        print(formulario)

        numero1 = int(formulario.inp_numero1)
        numero2 = int(formulario.inp_numero2)

        resultado = numero1 + numero2
        return render.generate(resultado)

if __name__ == "__main__":
    app.run()