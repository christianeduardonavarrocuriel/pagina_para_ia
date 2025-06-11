import web

urls = (
    '/', 'Mi_IA'
)

render = web.template.render('templates')
app = web.application(urls, globals())

class Mi_IA:

    def GET(self):
        return render.generate()
        
    def ollama(self,prompt):
    
if __name__ == "__main__":
    app.run()