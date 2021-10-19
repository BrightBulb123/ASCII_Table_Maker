"""Generate a nice and neat table out of text"""

class Table():
    def __init__(self, rows, columns, data, data_table) -> None or str:
        self.rows = rows
        self.columns = columns
        self.data = data
        self.data_table = data_table


def table_printer(data):
    if type(data) != list:
        return "Please enter a valid list for the data."

    rows = len(data)

    # figuring out how many columns there are
    all_entries = []
    for row in data:
        for item in row:
            all_entries.append(item)

    columns = int(round(len(all_entries)/rows))

    # Finding the max width of each column
    maxWidths = []
    for x in range(columns):
        temp = [str(y) for y in all_entries[x::columns]]
        maxWidths.append(len(max(temp, key=len)))
    
    # Generating the horizontal lines for the table
    dividorLine = '+'

    for lineWidth in maxWidths:
        for _ in range(lineWidth+2):
            dividorLine += '-'
        dividorLine += '+'

    # Generating the actual table
    table = ''
    for x in range(rows):
        table += dividorLine + '\n'
        table += '| ' + ' | '.join(str(data[x][y]) for y in range(columns)) + ' |' + '\n'
    table += dividorLine

    return Table(rows, columns, data, table)


print(table_printer(
                    [['column 1', 'column 2'],
                    [1, 2],
                    ['row 1', 'row 2']]).data_table)
