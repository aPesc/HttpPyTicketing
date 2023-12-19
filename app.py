import json
from flask import Flask, request, redirect, render_template

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template("index.html")
    
    if request.method == 'POST':

        nombre = request.form.get("nombre")
        asunto = request.form.get("asunto")
        fecha = request.form.get("fecha")

        data = {
            'date': fecha,
            'name': nombre,
            'asunto': asunto,
            'sqluser': "admin",
            'pwd': "passw0rd"
        }

        with open('output.json', "w") as jfile:
            json.dump(data, jfile, indent=2)
        
        #return make_response(f"<p>La incidencia en la fecha {fecha} a nombre de {nombre} con el siguiente asunto: {asunto}</p> <br> <p>Sera procesado</p>", 201)
        return "Incidencia enviada, para consultar incidencias ve a su respectivo apartado"




@app.route('/profile', methods=["GET"])
def profile():
    devices = ["iphone", "android"]

    #print(request.headers["User-Agent"])
    agent = request.headers.get("User-Agent")

    if devices[0] in agent.lower():
        return '''<p>Listado de perfiles</p>
                    <ul>
                        <li>Admin</li>
                        <li>Root</li>
                    </ul>
                '''
    else:
        return redirect("\\")



@app.errorhandler(401)
def err401(error):
    return render_template("errcode.html")

@app.errorhandler(403)
def err403(error):
    return render_template("errcode.html")

@app.errorhandler(404)
def err404(error):
    return render_template("errcode.html")


if __name__ == "__main__" :
    app.run(host='0.0.0.0')