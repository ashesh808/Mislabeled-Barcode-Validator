from flask import redirect, url_for


class BoxIDScanner:
    def __init__(self, box_part_ids):
        self.box_part_ids = box_part_ids

    def scan_box_id(self, box_id):
        if box_id in self.box_part_ids:
            return redirect(url_for("/ScanJobCode"))
        return 400