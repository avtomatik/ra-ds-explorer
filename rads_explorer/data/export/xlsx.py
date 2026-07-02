from dataclasses import asdict
from pathlib import Path

from openpyxl import Workbook

from rads_explorer.data.reports import Report


class XLSXExporter:
    def export(self, report: Report, output: Path):
        wb = Workbook()
        ws = wb.active
        ws.title = report.name

        data = report.data

        # =====================================================================
        # LIST REPORTS
        # =====================================================================
        if isinstance(data, list):
            if len(data) == 0:
                ws.append(["empty"])
            else:
                first = data[0]

                ws.append(list(asdict(first).keys()))

                for item in data:
                    ws.append(list(asdict(item).values()))

        # =====================================================================
        # DICT REPORTS
        # =====================================================================
        elif isinstance(data, dict):
            ws.append(["key", "value"])
            for k, v in data.items():
                ws.append([k, v])

        wb.save(output)
