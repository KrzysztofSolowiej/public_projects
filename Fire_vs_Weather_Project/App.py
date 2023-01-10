import joblib
from flask import Flask, request, escape
import numpy as np

app = Flask(__name__)

def get_pred(avr_temp_C=None):
    model = joblib.load('linear_regression')
    y_pred = model.predict( [[avr_temp_C]] )
    
    return y_pred

@app.route('/', methods=['GET', 'POST'])
def upload_data():
    if request.method == 'POST':
        avr_temp_C = request.values['avr_temp_C']    
        label_pred = get_pred(np.array(avr_temp_C, dtype=float))
        return '''
        <!doctype html>
        <title>Prosta predykcja z wykorzystaniem algorytmu regresji liniowej</title>
        <h1>Prosta predykcja z wykorzystaniem algorytmu regresji liniowej</h1>
        <p>Wyniki predykcji</p> 
        <p>Średnia miesięczna temperatura: {}</p>
        <p>Przewidywana liczba interwencji straży pożarnej: {} </p>
        '''.format(escape(avr_temp_C), escape(np.round(np.exp(label_pred))))

        
    return '''
    <!doctype html>
    <title>Prosta predykcja z wykorzystaniem algorytmu regresji liniowej</title>
    <h1>Prosta predykcja z wykorzystaniem algorytmu regresji liniowej</h1>
    <p>Wprowadź średnią miesięczną temperaturę</p>
    <form method=post enctype=multipart/form-data>
      <p><input type="number" name="avr_temp_C">
         <input type=submit value="OK">
    </form>
    '''
if __name__ == "__main__":
    app.run(debug=True)