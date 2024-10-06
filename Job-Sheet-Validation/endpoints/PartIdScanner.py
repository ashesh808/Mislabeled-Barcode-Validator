from flask import jsonify, redirect, url_for


class PartIDScanner:
    def __init__(self, valid_part_ids):
        self.valid_part_ids = valid_part_ids

    def scan_parts_id(self, part_id):
        if part_id in self.valid_part_ids:
            return jsonify({"redirect_url": "/Scan/BoxLabel"})