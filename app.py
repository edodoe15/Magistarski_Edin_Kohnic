from flask import Flask, request, jsonify
from flasgger import Swagger
import pandas as pd

app = Flask(__name__)
Swagger(app)

pred_df = pd.read_csv('predikcije_2026_2045.csv')
pred_df.columns = pred_df.columns.str.strip()


@app.route('/predict', methods=['POST'])
def predict():
    """
    Predviđanje temperature za određeni mjesec i godinu
    ---
    consumes:
      - application/json
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            year:
              type: integer
              example: 2028
            month:
              type: integer
              example: 8
    responses:
      200:
        description: Predviđena temperatura
        schema:
          type: object
          properties:
            year:
              type: integer
            month:
              type: integer
            predicted_temperature:
              type: number
              format: float
      404:
        description: Predikcija nije pronađena
        schema:
          type: object
          properties:
            message:
              type: string
    """
    data = request.get_json()
    year = int(data.get('year'))
    month = int(data.get('month'))


    row = pred_df[(pred_df['Godina'] == year) & (pred_df['Mjesec'] == month)]

    if row.empty:
        return jsonify({
            'message': f'Prediction for year {year} and month {month} is not available.'
        }), 404

    prediction = float(row['Predikcija temperature'].values[0])
    return jsonify({
        'year': year,
        'month': month,
        'predicted_temperature': prediction
    })

if __name__ == '__main__':
    app.run(debug=True)
