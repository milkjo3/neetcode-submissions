class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []

        for idx, op in enumerate(operations):
            match op:
                case "+":
                    y = record.pop() # pop
                    x = record[-1] # peek
                    add = int(x)+int(y) 
                    record.append(y) # push y
                    record.append(add) # push x+y
                case "D":
                    record.append(int(record[-1]) * 2) # peek and push double of last element
                case "C":
                    record.pop()
                case _:
                    record.append(int(operations[idx]))
        return sum(record)