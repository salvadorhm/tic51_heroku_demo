import web

urls = (
    '/', 'Index'
)
app = web.application(urls, globals())
wsgiapp = app.wsgifunc() # Prepara la webapp para funcionar con Gunicorn

class Index:
    def GET(self):
        return 'Hola desde Heroku!'

if __name__ == "__main__":
    app.run()
