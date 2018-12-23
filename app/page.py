from flask import *
import requests
import json

configs = dict()
with open('config.txt') as file:
    for inputline in file:
        var, value = inputline.split(':')
        configs[var] = value.rstrip('\n')

app = Flask(__name__)
@app.route("/metrics")
def show_metrics(configs=configs):

    # https: // stackoverflow.com / questions /
    # 11774265 / how - do - you - get - a -
    #  query - string - on - flask
    code = request.args.get('code')
    state = request.args.get('state')

    # https: // cloud.ouraring.com / docs /
    url="https://api.ouraring.com/oauth/token"

    payload = {"grant_type": "authorization_code",
               "code": code,
               "redirect_uri": "http://localhost:5000/metrics",
               "client_id": configs['client_id'],
               "client_secret": configs['client_secret']}

    r = requests.post(url,
                      data=payload,
                      headers={'content-type': 'text/plain; charset=utf-8'})

    return render_template('view.html',
                           code=code,
                           state=state,
                           status_code=r.status_code,
                           reason=r.reason,
                           text=r.text[:300])

if __name__ == "__main__":
    app.run(debug=False)