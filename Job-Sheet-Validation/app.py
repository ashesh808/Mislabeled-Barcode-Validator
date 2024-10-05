from flask import Flask, request

app = Flask(__name__)

validEmployeeIds = {
    'placeholder' # todo
}

validPartLabels = {
    'placeholder' # todo
}

validBoxLabels = {
    'placeholder' # todo
}

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/Scan/EmployeeId", methods=['GET'])
def scan_id():
    # Get the ID 
    employeeId = request.args.get('id')
    
    # Check validity
    if validEmployeeIds.contains(employeeId):
        return 200;
    
    # If the valid ID isn't in our hard-coded acceptable IDs, then we return 400 to indicate this was invalid
    return 400;

@app.route("/Scan/Jobsheet", methods=['GET'])
def scan_jobsheet():
    # TODO: We want to return the URI for next page to redirect to. TBD?
    return 501;
    
@app.route("/Scan/PartLabel", methods=['GET'])
def scan_part():
    partLabel = request.args.get('id')
    
    if validPartLabels.contains(partLabel):
        return 200
    return 400


@app.route("/Scan/BoxLabel", methods=['GET'])
def scan_box():
    boxLabel = request.args.get('id')
    
    if validBoxLabels.contains(boxLabel):
        return 200
    return 400

@app.route("/Job/Start", methods=['POST'])
def start_job():
    # Mark job as started
    
    return 200

@app.route("/Job/End", methods=['POST'])
def end_job():
    # Mark job as ended
    
    return 200


if __name__ == '__main__':
    app.run(debug=True)