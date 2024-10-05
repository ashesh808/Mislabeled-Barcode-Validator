class PartIDScanner:
    def __init__(self, valid_part_ids):
        self.valid_part_ids = valid_part_ids

    def scan_parts_id(self, part_id):
        # Check if the employee ID is valid
        if part_id in self.valid_part_ids:
            return 200
        return 400