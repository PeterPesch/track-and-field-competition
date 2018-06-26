# Subpackage table

Subpackage table handles HTML tables.

The table structure is designed to gather information from the HTML table in a standardised way.

Whenever many parts of the tfcompetition package extract some sort of special information from a tag in the same way, that information should be handled within this module.

This subpackage contains the following main objects:
- Table: Implements a HTML table, consisting of a header and a body
  - Header: Implements the Header of a Table, consisting of header rows
    - HeaderRow(Row): Implements a row in a table header, consisting of cells
  - Body: Implements the Body of a Table, consisting of rows
    - Row: Implements a row in a table body, consisting of cells
      - Cell: Implements a cell in a row