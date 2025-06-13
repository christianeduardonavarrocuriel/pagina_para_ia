import web
import requests

urls = (
    '/', 'IA'
)

render = web.template.render('templates')

app = web.application(urls, globals())

class IA:

    def GET(self):
        return render.generate()

    def POST (self):
        formulario = web.input()
        prompt = formulario.inp_prompt
        url = "http://localhost:11434/api/generate"
        data = {
            "model": "gemma3:1b",
            "prompt": "hola",
            "stream": False
        }

        response = requests.post(url, json=data)
        print(response.text)
    
if __name__ == "__main__":
    app.run()

    