from flask import Flask, render_template, request, redirect
from user import User
app = Flask(__name__)
@app.route("/")
def index():
    users = User.get_all()
    return render_template("index.html", users=users)

@app.route("/agregar", methods=["POST"])
def agregar():
    return render_template("agregar.html")

@app.route("/crear_usuario", methods=["POST"])
def create_user():
    data = {
        "nombre": request.form["nombre"],
        "apellido" : request.form["apellido"],
        "mail" : request.form["mail"]
    }

    User.save(data)
    return redirect("/")
            
if __name__ == "__main__":
    app.run(debug=True)