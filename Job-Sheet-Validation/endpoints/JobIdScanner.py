class JobIDScanner:
    def __init__(self, valid_jobs_ids):
        self.valid_jobs_ids = valid_jobs_ids

    def scan_job_id(self, job_id):
        # Check if the employee ID is valid
        if job_id in self.valid_jobs_ids:
            return 200
        return 400