# app.py
from flask import Flask, render_template, request, jsonify
from FSCS import FCFSAlgorithm
from MLQ import MultilevelQueueAlgorithm
from Priority_NonPreemptive import PriorityNonPreemptive
from Priority_Preemptive import PriorityPreemptive
from RR import RoundRobinAlgorithm
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
    quantum = data.get('quantum')  
    
    if not processes:
        return jsonify({"error": "No processes provided"}), 400

    try:
        if algorithm == "FCFS":
            solver = FCFSAlgorithm()
            result = solver.solve(processes)
            
        elif algorithm == "SJF_Pre":
            solver = SJFPreemptive()
            result = solver.solve(processes)
            
        elif algorithm == "SJF_NonPre":
            solver = SJFNonPreemptive()
            result = solver.solve(processes)
            
        elif algorithm == "Priority_NonPreemptive":
            solver = PriorityNonPreemptive()
            result = solver.solve(processes)
            
        elif algorithm == "Priority_Preemptive":
            solver = PriorityPreemptive()
            result = solver.solve(processes)
            
        elif algorithm == "Round_Robin":
            solver = RoundRobinAlgorithm()
            if not quantum:
                quantum = 2  
            result = solver.solve(processes, quantum)
            
        elif algorithm == "Multilevel_Queue":
            solver = MultilevelQueueAlgorithm()
            result = solver.solve(processes, quantum)
            
        else:
            return jsonify({"error": "Invalid Algorithm Selection"}), 400

        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

app.run(debug=True)