import re

class StringCalculator:

    def add(self, numbers: str) -> int:
        if not numbers:
            return 0


        num_list = self.delimiter_escape(numbers)

        negatives = [n for n in num_list if n < 0]
        if negatives:
            raise ValueError(f"Negative numbers not allowed: {','.join(map(str, negatives))}")
        
        return sum(num_list)

    def delimiter_escape(self, numbers):
        delimiter = ",|\n"
        if numbers.startswith("//"):
            match = re.match(r"//(.+)\n(.*)", numbers)
            if match:
                delimiter = match.group(1)
                numbers = match.group(2)

        num_list = [int(n) for n in re.split(delimiter, numbers) if n]
        return num_list
    def substract(self, numbers: str) -> int:
        if not numbers:
            return 0

        num_list = self.delimiter_escape(numbers)

        pos = [n for n in num_list if n > 0]
        if pos:
            raise ValueError(f"positives numbers not allowed: {','.join(map(str, pos))}")
        
        return sum(num_list)
        

s = StringCalculator()
s.substract("-1,-2")
