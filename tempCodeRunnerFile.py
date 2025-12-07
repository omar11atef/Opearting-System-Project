# app.py
from flask import Flask, render_template, request, jsonify
from FSCS import FCFSAlgorithm
from Priority_NonPreemptive import PriorityNonPreemptive
from Priority_Preemptive import PriorityPreemptive
from SJF_Preemptive import SJFPreemptive
from SJF_NonPreemptive import SJFNonPreemptive

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    algorithm = data.get('algorithm')
    processes = data.get('processes')
    if not processes:
        return jsonify({"error": "No processes provided"}), 400

    try:
        if algorithm == "FCFS":
            solver = FCFSAlgorithm()
        elif algorithm == "SJF_Pre":
            solver = SJFPreemptive()
        elif algorithm == "SJF_NonPre":
            solver = SJFNonPreemptive()
        elif algorithm == "Priority_NonPreemptive":
            solver = PriorityNonPreemptive()
        elif algorithm == "Priority_Preemptive":
            solver = PriorityPreemptive()
        else:
            return jsonify({"error": "Invalid Algorithm Selection"}), 400

        result = solver.solve(processes)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

app.run(debug=True)
