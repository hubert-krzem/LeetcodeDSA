class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # Using a stack Data structure

        # int n : record a new score of n
        # + : sum last two
        # D : Double previous score
        # C : Remove previous score

        ops = []

        for op in operations:
            if op == '+':
                ops.append(sum(ops[-2:]))
            elif op == 'D':
                ops.append(ops[-1] * 2)
            elif op == 'C':
                ops.pop(-1)
            else: # Not an operation
                # Converts string to int, allowing other operations
                ops.append(int(op))

        return sum(ops)
