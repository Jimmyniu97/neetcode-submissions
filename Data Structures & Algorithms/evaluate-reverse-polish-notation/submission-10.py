class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {"+","-","*","/"}
        stack = []
        for t in tokens:
            if t not in operators:
                stack.append(t)
            else:
                b = int(stack.pop())
                a = int(stack.pop())
                if t == "+":
                    stack.append(str(a+b))
                elif t == "-":
                    stack.append(str(a-b))
                elif t == "*":
                    stack.append(str(a*b))
                elif t == "/":
                    stack.append(str(int(a/b)))
        
        return int(stack.pop())
