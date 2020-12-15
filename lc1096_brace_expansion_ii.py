"""
1096. Brace Expansion II
Hard

Under a grammar given below, strings can represent a set of lowercase words.  Let's use R(expr) to denote the set of words the expression represents.

Grammar can best be understood through simple examples:

Single letters represent a singleton set containing that word.
R("a") = {"a"}
R("w") = {"w"}
When we take a comma delimited list of 2 or more expressions, we take the union of possibilities.
R("{a,b,c}") = {"a","b","c"}
R("{{a,b},{b,c}}") = {"a","b","c"} (notice the final set only contains each word at most once)
When we concatenate two expressions, we take the set of possible concatenations between two words where the first word comes from the first expression and the second word comes from the second expression.
R("{a,b}{c,d}") = {"ac","ad","bc","bd"}
R("a{b,c}{d,e}f{g,h}") = {"abdfg", "abdfh", "abefg", "abefh", "acdfg", "acdfh", "acefg", "acefh"}
Formally, the 3 rules for our grammar:

For every lowercase letter x, we have R(x) = {x}
For expressions e_1, e_2, ... , e_k with k >= 2, we have R({e_1,e_2,...}) = R(e_1) ∪ R(e_2) ∪ ...
For expressions e_1 and e_2, we have R(e_1 + e_2) = {a + b for (a, b) in R(e_1) × R(e_2)}, where + denotes concatenation, and × denotes the cartesian product.
Given an expression representing a set of words under the given grammar, return the sorted list of words that the expression represents.



Example 1:

Input: "{a,b}{c,{d,e}}"
Output: ["ac","ad","ae","bc","bd","be"]
Example 2:

Input: "{{a,z},a{b,c},{ab,z}}"
Output: ["a","ab","ac","z"]
Explanation: Each distinct word is written only once in the final answer.


Constraints:

1 <= expression.length <= 60
expression[i] consists of '{', '}', ','or lowercase English letters.
The given expression represents a set of words based on the grammar given in the description.

"""
"""
generic infix to prefix expression

observation:
i) , -> + (concatenation)
ii) three different operators, priority cartesion product(*) > concatenation(,) > {
}{ a{ a}-> * cartesion product, when opening braces follows closing brace, or letter followed by opening or closing braces
iii) a-z -> operand (letters)
iv) when pushing one operator to stack, always process all operators on stack that has high precedence, store the result back into operand, before storing this lower precedence operator
v) for closing brace, process all operators on operator stack until opening brace is met, and push processing result back to operand stack

"""


class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        priority = {'{': 0, ',': 1, '*': 2}  # priority * > , > {

        # preprocess, insert * in front of opening { if before it is value (alphabet) closing brace }, or alphabest value in front of closing brace
        new_expression = expression[0]
        for i in range(1, len(expression)):
            if expression[i] == '{' and (expression[i - 1].isalpha() or expression[i - 1] == '}'):
                new_expression += '*' + expression[i]
            elif expression[i].isalpha() and expression[i - 1] == '}':
                new_expression += '*' + expression[i]
            else:
                new_expression += expression[i]

        expression = new_expression

        # print(expression)

        def applyop(operand1, operand2, operator):
            if operator == ',':
                return operand1 + operand2
            else:  # *
                return [o1 + o2 for o1 in operand1 for o2 in operand2]

        result = []
        operators = []
        operands = []
        i = 0

        while i < len(expression):
            c = expression[i]
            # print('i=%s c=%s' % (i, c))
            if c == '{':
                operators.append(c)
            elif c.isalpha():
                val = c
                i += 1
                while i < len(expression) and expression[i].isalpha():
                    c = expression[i]
                    i += 1
                    val += c
                # not a-z anymore
                operands.append([val])
                i -= 1  # we increase i at end of loop
            elif c in ',*':
                while operators and priority[operators[-1]] > priority[
                    c]:  # high precedence needs to be processed first
                    operator = operators.pop()
                    operand2 = operands.pop()
                    operand1 = operands.pop()
                    operands.append(applyop(operand1, operand2, operator))
                operators.append(c)
            elif c == '}':
                while operators and operators[-1] != '{':
                    operand2 = operands.pop()
                    operand1 = operands.pop()
                    operator = operators.pop()
                    operands.append(applyop(operand1, operand2, operator))
                if operators and operators[-1] == '{':
                    operators.pop()  # remove corresponding opening brace
            # print('operators=%s operands=%s' % (str(operators), str(operands)))
            i += 1

        # process all remaining operators
        while operators:
            operator = operators.pop()
            operand2 = operands.pop()
            operand1 = operands.pop()
            operands.append(applyop(operand1, operand2, operator))

        # print('operands=%s' % str(operands))
        return sorted(set(operands[-1]))

def main():
    sol = Solution()
    assert sol.braceExpansionII("{a,b}{c,{d,e}}") == ["ac","ad","ae","bc","bd","be"], 'fails'

    assert sol.braceExpansionII("{{a,z},a{b,c},{ab,z}}") == ["a","ab","ac","z"], 'fails'


if __name__ == '__main__':
   main()