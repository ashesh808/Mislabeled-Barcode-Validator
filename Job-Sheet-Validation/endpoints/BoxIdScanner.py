class BoxIDScanner:
    def __init__(self, box_part_ids):
        self.box_part_ids = box_part_ids

    def scan_box_id(self, box_id):
        if box_id in self.box_part_ids:
            return True
        return False