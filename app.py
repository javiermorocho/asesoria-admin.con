from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route("/")
def index():
    with open("index.html", "r", encoding="utf-8") as f:
        html = f.read()
    return render_template_string(html)

@app.route("/enviar", methods=["POST"])
def enviar():
    nombre = request.form["nombre"]
    correo = request.form["correo"]
    mensaje = request.form["mensaje"]
    
    # Aquí se podría guardar en una base de datos o enviar por correo
    print(f"Mensaje recibido de {nombre} ({correo}): {mensaje}")
    
    return f"<h1>Gracias {nombre}, hemos recibido tu mensaje.</h1>"

if __name__ == "__main__":
    app.run(debug=True)
