# fileparse.py
#
# Exercise 3.3

import csv

def parse_csv(filename, select=None, types=None, has_headers=True, delimiter=',', silence_errors=False) -> list:
    '''
    Parse a CSV file into a list of records
    '''
    if select and not has_headers:
        raise RuntimeError('select requires column headers')

    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)
        records = []
        row_num = 0

        # Read the file headers
        if has_headers:
            headers = next(rows)

            # If a column selector was given, find indices of the specified columns.
            # Also narrow the set of headers used for resulting dictionaries
            if select:
                indices = [headers.index(colname) for colname in select]
                headers = select
            else:
                indices = []

            for row in rows:
                row_num += 1
                
                if not row:    # Skip rows with no data
                    continue
                # Filter the row if specific columns were selected
                if indices:
                    row = [ row[index] for index in indices ]

                # Convert the types
                if types:
                    try:
                        row = [func(val) for func, val in zip(types, row)]
                    except ValueError as e:
                        if not silence_errors:
                            print(f'Row {row_num}: Couldn\'t convert {row}')
                            print(f'Row {row_num}:', e)
                        continue

                # Make a dictionary
                record = dict(zip(headers, row))
                records.append(record)
        else:
            for row in rows:
                if not row:
                    continue
                if types:
                    try:
                        row = [func(val) for func, val in zip(types, row)]
                    except ValueError as e:
                        if not silence_errors:
                            print(f'Row {row_num}: Couldn\'t convert {row}')
                            print(f'Row {row_num}:', 'Reason', e)
                        continue
                record = tuple(row)
                records.append(record)

    return records