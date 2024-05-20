from flask import Flask, request, jsonify
import threading

app = Flask(__name__)
controller = None

@app.route('/start', methods=['POST'])
def start():
    global controller
    controller.print("Received request to start processing a .prompts file")
    data = request.json
    prompt_file = data.get('prompt_file')
    if prompt_file:
        prompt_file = "c:\\Users\\vesperknight\\dream-factory\\prompts\\" + prompt_file
        controller.print(prompt_file)
        controller.new_prompt_file(prompt_file)
        
        return jsonify({"status": "started", "prompt_file": prompt_file}), 200
    return jsonify({"error": "prompt_file not provided"}), 400

@app.route('/pause', methods=['POST'])
def pause():
    global controller
    controller.print("Received request to pause processing")
    controller.pause()
    return jsonify({"status": "paused"}), 200

@app.route('/resume', methods=['POST'])
def resume():
    global controller
    controller.print("Received request to resume processing")
    controller.unpause()
    return jsonify({"status": "resumed"}), 200

@app.route('/shutdown', methods=['POST'])
def shutdown():
    global controller
    controller.print("Received request to shutdown the server")
    def shutdown_server():
        controller.shutdown()
        func = request.environ.get('werkzeug.server.shutdown')
        if func is None:
            raise RuntimeError('Not running with the Werkzeug Server')
        func()
    threading.Thread(target=shutdown_server).start()
    return jsonify({"status": "shutting down"}), 200

def start_api(ctrl):
    ctrl.print('starting custom api')
    ctrl.print('starting custom api')
    ctrl.print('starting custom api')
    global controller
    controller = ctrl
    ctrl.print('houston we have visual')
    app.run(host='0.0.0.0', port=5000)
