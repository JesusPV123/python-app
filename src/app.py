from flask import Flask, jsonify
from datetime import datetime
from socket import gethostname

app = Flask(__name__)

# URL que devuelve el hostname y la hora actual (HH24:MM:SS on Mon DD, YYYY)
@app.route('/api/v1/details')
def details():
    return jsonify({'host': gethostname(),
                    'time': datetime.now().strftime('%H:%M:%S on %b %d, %Y'),
                    'message': "Creación de un pipepile con GitHub!!"})

@app.route('/api/v1/healthz')
def healthz():
    return jsonify({'status': 'up'}), 200

if __name__ == '__main__':
    app.run(host="0.0.0.0")


#'/api/v1/details'
#'/api/v1/heathz'