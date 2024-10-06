from flask import Flask, request,render_template, jsonify

from endpoints.BoxIdScanner import BoxIDScanner
from endpoints.EmployeeIdScanner import EmployeeIDScanner
from endpoints.JobIdScanner import JobIDScanner
from endpoints.PartIdScanner import PartIDScanner


app = Flask(__name__)

validEmployeeIds = {
    '20102913120564',
    '20102913016762',
    '1119802303369'
}

validJobs = {
    '169345'
}

validBoxLabels = {
    '103-6402-S',
    '103-6402-S',
}

validPartLabels = {
    '021038595344'
}

@app.route("/")
def emp_scan_page():
    return render_template('index.html')

@app.route("/ScanJobCode")
def job_scan_page():
    return render_template('scanJobCode.html')

@app.route("/ValidateBoxLabel")
def parts_scan_page():
    return render_template('validateBoxLabel.html')

@app.route("/ValidatePartsLabel")
def box_scan_page():
    return render_template('validatePartsLabel.html')

@app.route("/Scan/EmployeeId", methods=['GET'])
def scan_id():
    employeeId = request.args.get('id')
    emp_scanner = EmployeeIDScanner(validEmployeeIds)
    if emp_scanner.scan_employee_id(employeeId):
        return jsonify({"redirect_url": "/ScanJobCode"})
    return "404"

@app.route("/Scan/Jobsheet", methods=['GET'])
def scan_jobsheet():
    jobId = request.args.get('id')
    job_scanner = JobIDScanner(validJobs)
    if job_scanner.scan_job_id(jobId):
        return jsonify({"redirect_url": "/ValidatePartsLabel"})
    return "404"

    
@app.route("/Scan/PartLabel", methods=['GET'])
def scan_part():
    partLabel = request.args.get('id')
    parts_scanner = PartIDScanner(validPartLabels)
    if parts_scanner.scan_parts_id(partLabel):
        return jsonify({"redirect_url": "/ValidateBoxLabel"})
    return "404"

@app.route("/Scan/BoxLabel", methods=['GET'])
def scan_box():
    boxLabel = request.args.get('id')
    box_scanner = BoxIDScanner(boxLabel)
    if box_scanner.scan_box_id(boxLabel):
        return jsonify({"redirect_url": "/ScanJobCode"})
    return "404"

@app.route("/Job/Start", methods=['POST'])
def start_job():
    return "200"

@app.route("/Job/End", methods=['POST'])
def end_job():
    return "200"

if __name__ == '__main__':
    app.run(debug=True)