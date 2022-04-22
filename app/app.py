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
    diccionario = [{'ciudad':'Medellín', 'direccion':'Calle 67 # 56-10', 'nroHabitaciones':3, 'precio':150000},{'ciudad':'Cartagena', 'dirección':'Carrera 34 # 23-10', 'nroHabitaciones':2, 'precio':180000},{'ciudad':'Santa Marta', 'dirección':'Calle 78 # 45-47', 'nroHabitaciones':4, 'precio':160000}]
    return render_template('habitaciones.html', datos = diccionario)

@app.route('/contactenos')
def contactenos():    
    return render_template('contactenos.html')


if __name__ == "__main__":
    app.run(debug=True, port=1000)
