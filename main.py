# Importar
from flask import Flask, render_template


app = Flask(__name__)

# La primera página
@app.route('/')
def index():
    return render_template('index.html')

# La segunda página
@app.route('/form')
def form():
    return render_template('form.html')

# La tercera página: resultado del formulario
@app.route('/result', methods=['POST'])
def result():
    consumo_electrico = float(request.form['consumo-electrico'])
    consumo_agua = float(request.form['consumo-agua'])
    transporte = float(request.form['transporte'])
    comida = float(request.form['comida'])

    factor_electricidad = 0.58  # kg CO2/kWh
    factor_agua = 0.0015  # kg CO2/L
    factor_transporte = 1.0  # kg CO2/km
    factor_comida = 15  # kg CO2/kg

    emisiones = (
        consumo_electrico * factor_electricidad
        + consumo_agua * factor_agua
        + transporte * factor_transporte
        + comida * factor_comida
    )

    porcentaje = emisiones / 1000000 * 100  # Calcular el porcentaje

    return render_template('result.html', consumo_electrico=consumo_electrico, consumo_agua=consumo_agua,
                           transporte=transporte, comida=comida, porcentaje=porcentaje)

app.run(debug=True)
