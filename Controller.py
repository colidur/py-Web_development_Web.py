import web
from Models import RegisterModel

urls = ('/', 'Home',
        '/register', 'Register',
        '/postregistration', 'PostRegistration'
)

render = web.template.render("Views/Templates", base = "MainLayout")
app = web.application(urls, globals())

#Classes/Routes

class Home:
    def GET(self):
        return render.Home()
    
class Register:
    def GET(self):
        return render.Register()

class PostRegistration:
    def POST(self):
        data = web.input()
        print(data)
        RegisterModel.ToRegister.insert_user(data)
        return data.username   
    def GET(self):
        return render.PostRegistration()

if __name__ == "__main__":
    app.run()
