"""Generate a nice and neat table out of text"""

class TableClass():
    def __init__(self, rows: int, columns: int, data: list, data_table: str) -> None:
        self.rows = rows
        self.columns = columns
        self.data = data
        self.data_table = data_table


def table_printer(data: list) -> TableClass:
    if type(data) != list:
        return TableClass(None, None, data, "Please enter a valid list for the data.")

    rows, all_entries, columns = rowsColumnsAll_entries(data)

    # Finding the max width of each column
    maxWidths = findMaxWidth(all_entries, columns)

    # Generating the horizontal lines for the table
    dividorLine = dividorLineMaker(maxWidths)

    # Generating the actual table
    table = ''
    for x in range(rows):
        table += dividorLine + '\n'
        separatorLine = '| ' + ' | '.join(str(data[x][y]) for y in range(columns)) + ' |' + '\n'
        if len(separatorLine) != len(dividorLine):
            separatorLine = separatorLine.split('|')
            separatorLine.remove('')
            separatorLine.remove('\n')
            for segment in separatorLine:
                temp = str(segment)
                lengthWanted = (int(maxWidths[separatorLine.index(temp)])+2)
                while len(segment) != lengthWanted:
                    segment += ' '
                    segment = ' ' + segment

                    segment = segmentShortener(segment, lengthWanted)
                separatorLine[separatorLine.index(temp)] = segment
            temp = '|'
            temp += '|'.join(separatorLine) + '|' + '\n'
            separatorLine = str(temp)
            table += separatorLine
    table += dividorLine

    return TableClass(rows, columns, data, table)

def dividorLineMaker(maxWidths):
    dividorLine = '+'

    for lineWidth in maxWidths:
        for _ in range(lineWidth+2):
            dividorLine += '-'
        dividorLine += '+'
    return dividorLine

def findMaxWidth(all_entries, columns):
    maxWidths = []
    for x in range(columns):
        temp = [str(y) for y in all_entries[x::columns]]
        maxWidths.append(len(max(temp, key=len)))
    return maxWidths

def rowsColumnsAll_entries(data):
    rows = len(data)

    # figuring out how many columns there are
    all_entries = []
    for row in data:
        for item in row:
            all_entries.append(item)

    columns = int(round(len(all_entries)/rows))
    return rows,all_entries,columns

def segmentShortener(segment, lengthWanted):
    if len(segment) > lengthWanted:
        lOrR = justificationAsker(segment)
        while len(segment) > lengthWanted:
            segment = segment[1:] if lOrR in ("left", "l") else segment[0:-1]
    return segment

def justificationAsker(segment):
    lOrR = input(f"One of your values' ({segment.strip()}) length is uneven compared to the column it's in. Would you like it more to the left or right? (left, l, right, r)\n").lower().strip()
    while lOrR not in ("left", "l", "right" , "r"):
        print("Please enter one of the following values: 'left', 'l', 'right', or 'r' (without the quotation marks).")
        lOrR = input(f"One of your values' ({segment.strip()}) length is uneven compared to the column it's in. Would you like it more to the left or right? (left, l, right, r)\n").lower().strip()
    return lOrR


print(table_printer(
    [
        ["C1R1", "C1R2-Uneven"],
        ["C2R1-Uneven", "C2R2"]
    ]
).data_table)

print("\n\n")

print(table_printer(
        [
          ["C1R1", "C2R1", "C3R1"],
          ["C1R2", "C2R2", "C3R2"],
          ["C1R3", "C2R3", "C3R3"],
      ]
).data_table)
