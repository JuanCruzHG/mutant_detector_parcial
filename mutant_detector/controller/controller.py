from flask import Flask, request, jsonify
from service.service import is_mutant

app = Flask(__name__)

@app.route('/mutant/', methods=['POST'])
def detect_mutant():
    data = request.json
    dna = data.get("dna")
    if is_mutant(dna):
        return jsonify({"message": "Mutant detected"}), 200
    else:
        return jsonify({"message": "Not a mutant"}), 403
