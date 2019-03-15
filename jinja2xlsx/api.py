from openpyxl import Workbook
from requests_html import HTML


def render(html_str: str) -> Workbook:
    html = HTML(html=html_str)

    table = html.find("table", first=True)

    # columns = table.find("colgroup", first=True).find("col")
    # assert columns, "No colgroup with col defined"

    table_rows = table.find("tbody", first=True).find("tr")
    row_values = ((td.text for td in row.find("td")) for row in table_rows)

    wb = Workbook()
    ws = wb.active

    for row in row_values:
        ws.append(list(row))

    return wb
