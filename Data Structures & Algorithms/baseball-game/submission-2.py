class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record: List[int] = []
        total = 0
        for op in operations:
            if op == "+":
                score = record[-1] + record[-2]
                record.append(score)
                total += score
            elif op == "D":
                score = record[-1] * 2
                record.append(score) 
                total += score
            elif op == "C":
                total -= record.pop()
            else:
                score = int(op)
                record.append(score)
                total += score
        return total