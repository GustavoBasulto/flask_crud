from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.user import User


@app.route("/usuarios")
def usuarios():
    users = User.get_all()
    return render_template("index.html", users=users)

@app.route("/usuarios/<id>")
def usuario_detalle(id):
    return render_template("usuario.html", usuario=User.get_by_id(id))

@app.route("/usuarios/<id>/editar")
def usuario_modificar(id):
    return render_template("modificar.html", usuario=User.get_by_id(id))

@app.route("/usuarios/agregar")
def agregar():
    return render_template("agregar.html")

@app.route("/eliminar/<id>")
def eliminar(id):
    User.delete(id)
    flash("exito al eliminar usuario","success")
    return redirect("/usuarios")
    

@app.route("/actualizar/procesar/<id>", methods=["POST"])
def actualizar_procesar(id):
    data = {
        "id":id,
        "nombre": request.form["nombre"],
        "apellido" : request.form["apellido"],
        "mail" : request.form["mail"]
    }
    User.update(data)
    flash(f"exito al actualizar el usuario {data['nombre']}","success")
    return redirect(f"/usuarios/{data['id']}")

@app.route("/agregar/procesar", methods=["POST"])
def agregar_procesar():
    data = {
        "nombre": request.form["nombre"],
        "apellido" : request.form["apellido"],
        "mail" : request.form["mail"]
    }
    User.save(data)
    flash(f"exito al agregar el usuario {data['nombre']}", "success")
    newid=User.get_last()
    return redirect(f"/usuarios/{newid}")