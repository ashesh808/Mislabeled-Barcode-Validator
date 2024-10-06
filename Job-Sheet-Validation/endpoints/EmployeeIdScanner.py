

class EmployeeIDScanner:
    def __init__(self, valid_employee_ids):
        self.valid_employee_ids = valid_employee_ids

    def scan_employee_id(self, employee_id):
        if employee_id in self.valid_employee_ids:
            return 200
        return 400