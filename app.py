from flask import Flask
app = Flask(__name__)

# RUTAS

@app.route('/')
def index():
    return '¡Hola! Bienvenido a mi aplicación Flask.'

@app.route('/usuario/<nombre>')
def usuario(nombre):
    return f'Bienvenido, {nombre}!'
#RUTA Servicio
@app.route('/servicios')
def servicios():
    return "Servicios disponibles en la Tienda Paola:"

if __name__ == '__main__':
    app.run(debug=True)

#Realizado por Denisis Portillla