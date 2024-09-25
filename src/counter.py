from flask import Flask
from src import status

app = Flask(__name__)

# Dictionary to hold counters
COUNTERS = {}

@app.route('/counters/<name>', methods=['POST'])
def create_counter(name):
    """Creating the counter"""
    app.logger.info(f"Request to create counter: {name}")
    global COUNTERS
    if name in COUNTERS:
        return {"Message": f"Counter {name} already exists"}, status.HTTP_409_CONFLICT
    COUNTERS[name] = 0
    return {name: COUNTERS[name]}, status.HTTP_201_CREATED


@app.route('/counters/<name>', methods=['PUT'])
def update_counter(name):
    """Updating the counter by incrementing by 1"""
    app.logger.info(f"Request to update counter: {name}")
    if name not in COUNTERS:
        return {"Message": f"Counter {name} does not exist"}, status.HTTP_404_NOT_FOUND
    COUNTERS[name] += 1
    return {name: COUNTERS[name]}, status.HTTP_200_OK


@app.route('/counters/<name>', methods=['GET'])
def read_counter(name):
    """Read the value of a counter"""
    app.logger.info(f"Request to read counter: {name}")
    if name not in COUNTERS:
        return {"Message": f"Counter {name} does not exist"}, status.HTTP_404_NOT_FOUND
    return {name: COUNTERS[name]}, status.HTTP_200_OK

@app.route('/counters/<name>', methods=['DELETE'])
def delete_counter(name):
    """Delete the counter"""
    app.logger.info(f"Request to delete counter: {name}")
    global COUNTERS
    if name not in COUNTERS:
        return {"Message": f"Counter {name} does not exist"}, status.HTTP_404_NOT_FOUND
    del COUNTERS[name]
    return '', status.HTTP_204_NO_CONTENT