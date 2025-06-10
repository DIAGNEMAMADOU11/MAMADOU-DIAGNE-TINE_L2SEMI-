from flask import Flask, jsonify, send_from_directory
from scan import scan_reseau  

app = Flask(__name__)

# Route API pour récupérer les appareils scannés
@app.route('/api/devices')
def get_devices():
    devices = scan_reseau()
    return jsonify(devices)

# Route principale : page de la carte
@app.route('/')
def serve_frontend():
    return send_from_directory('frontend', 'index.html')

# Route pour tous les fichiers statiques (JS, CSS, images)
@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory('frontend', path)

if __name__ == '__main__':
    app.run(debug=True, port=3000)
