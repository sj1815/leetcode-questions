class Spreadsheet:

    def __init__(self, rows: int):
        self.cells = defaultdict(int)

    def setCell(self, cell: str, value: int) -> None:
        self.cells[cell] = value
        
    def resetCell(self, cell: str) -> None:
        self.cells[cell] = 0
        
    def getValue(self, formula: str) -> int:
        x, y = formula[1:].split("+")

        try:
            x = int(x)
        except:
            x = self.cells[x]

        try:
            y = int(y)
        except:
            y = self.cells[y]
            
        return x + y        


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)