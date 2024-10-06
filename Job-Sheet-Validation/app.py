from flask import Flask, request,render_template
from endpoints.BoxIdScanner import BoxIDScanner
from endpoints.EmployeeIdScanner import EmployeeIDScanner
from endpoints.JobIdScanner import JobIDScanner
from endpoints.PartIdScanner import PartIDScanner


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
    return EmployeeIDScanner.scan_employee_id(employeeId)

@app.route("/Scan/Jobsheet", methods=['GET'])
def scan_jobsheet():
    jobId = request.args.get('id')
    return JobIDScanner.scan_job_id(jobId)
    
@app.route("/Scan/PartLabel", methods=['GET'])
def scan_part():
    partLabel = request.args.get('id')
    return PartIDScanner.scan_parts_id(partLabel)


@app.route("/Scan/BoxLabel", methods=['GET'])
def scan_box():
    boxLabel = request.args.get('id')
    return BoxIDScanner.scan_box_id(boxLabel)

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