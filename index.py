from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/usuario/<nome_usuario>')
def index():
    return render_template("usuario.html", nome_usuario=nomeusuario)

if __name__ == "__main__":
	app.run(debug=True)

