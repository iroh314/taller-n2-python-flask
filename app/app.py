from flask import Flask, render_template
app = Flask(__name__) #Variable que lanzara el aplicativo

#decorador para ruta de inicio
@app.route('/')
def index():    
    return render_template('index.html')

@app.route('/quienesSomos')
def quienesSomos():
    return render_template('quienesSomos.html')

@app.route('/habitaciones')
def habitaciones():
    return render_template('habitaciones.html')

@app.route('/contactenos')
def contactenos():

    diccionario = [{'Ciudad':'Medellín', 'Dirección':'Calle 67 # 56-10', 'Nro Habitaciones':3, 'Precio':150000},{'Ciudad':'Cartagena', 'Dirección':'Carrera 34 # 23-10', 'Nro Habitaciones':2, 'Precio':180000},{'Ciudad':'Santa Marta', 'Dirección':'Calle 78 # 45-47', 'Nro Habitaciones':4, 'Precio':160000}]
    return render_template('contactenos.html')


if __name__ == "__main__":
    app.run(debug=True, port=1000)
