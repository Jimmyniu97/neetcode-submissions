class Solution:
    def helper(self, token):
        try:
            int(token)
            return True
        except:
            return False

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if self.helper(token):
                stack.append(int(token))
            else:
                n2 = stack.pop()
                n1 = stack.pop()
                if token == "+":
                    stack.append(n1+n2)
                elif token == "-":
                    stack.append(n1-n2)
                elif token == "*":
                    stack.append(n1*n2)
                elif token == "/":
                    stack.append(int(n1/n2))
        
        return stack[0]