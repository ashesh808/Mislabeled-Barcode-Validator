class JobIDScanner:
    def __init__(self, valid_jobs_ids):
        self.valid_jobs_ids = valid_jobs_ids

    def scan_job_id(self, job_id):
        if job_id in self.valid_jobs_ids:
            return True
        return False