def printTable(headers: list, data: list, columnSpacing=5, includeStatement=True):
    """Table format printing based on input headers and data"""
    rowError = []
    _form = lambda h: f"{{:<{len(h) + columnSpacing}}}"
    _row = ''.join([_form(h) for h in headers])
    print(_row.format(*headers))
    for idx, row in enumerate(data):
        if len(row) != len(headers):
            rowError.append(str(idx))
            row.append('')
        print(_row.format(*row))
    if includeStatement:
        rowError = ', '.join(rowError) if rowError else 'None'
        print(f"\nTable Size: {len(data)}x{len(headers)}, Row Error Index: {rowError}")
    return None