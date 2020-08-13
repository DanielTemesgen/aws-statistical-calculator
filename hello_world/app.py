import json
from flask_lambda import FlaskLambda
from flask import request
import numpy_financial as npf
import numpy as np

app = FlaskLambda(__name__)


@app.route('/ipmt')
def index():
    principal = float(request.args.get('principal', 2500))

    per = np.arange(1 * 12) + 1

    ipmt: np.ndarray = npf.ipmt(0.0824 / 12, per, 1 * 12, principal).tolist()


    return_dict = (
        json.dumps(ipmt),
        200,
        {"Content-Type": "application/json"}
    )

    return return_dict
