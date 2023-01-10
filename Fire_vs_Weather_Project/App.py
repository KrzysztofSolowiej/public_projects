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
        <title>Simple prediction model based on linear regression algorithm</title>
        <h1>Simple prediction model based on linear regression algorithm</h1>
        <p>Prediction results</p> 
        <p>Average monthly temperature: {}</p>
        <p>Estimated number of fire department deployments: {} </p>
        '''.format(escape(avr_temp_C), escape(np.round(np.exp(label_pred))))

        
    return '''
    <!doctype html>
    <title>Simple prediction model based on linear regression algorithm</title>
    <h1>Simple prediction model based on linear regression algorithm</h1>
    <p>Enter the average monthly temperature</p>
    <form method=post enctype=multipart/form-data>
      <p><input type="number" name="avr_temp_C">
         <input type=submit value="OK">
    </form>
    '''
if __name__ == "__main__":
    app.run(debug=True)