"""
726. Number of Atoms

Given a chemical formula (given as a string), return the count of each atom.

The atomic element always starts with an uppercase character, then zero or more lowercase letters, representing the name.

One or more digits representing that element's count may follow if the count is greater than 1. If the count is 1, no digits will follow. For example, H2O and H2O2 are possible, but H1O2 is impossible.

Two formulas concatenated together to produce another formula. For example, H2O2He3Mg4 is also a formula.

A formula placed in parentheses, and a count (optionally added) is also a formula. For example, (H2O2) and (H2O2)3 are formulas.

Given a formula, return the count of all elements as a string in the following form: the first name (in sorted order), followed by its count (if that count is more than 1), followed by the second name (in sorted order), followed by its count (if that count is more than 1), and so on.

Example 1:

Input: formula = "H2O"
Output: "H2O"
Explanation: The count of elements are {'H': 2, 'O': 1}.
Example 2:

Input: formula = "Mg(OH)2"
Output: "H2MgO2"
Explanation: The count of elements are {'H': 2, 'Mg': 1, 'O': 2}.
Example 3:

Input: formula = "K4(ON(SO3)2)2"
Output: "K4N2O14S4"
Explanation: The count of elements are {'K': 4, 'N': 2, 'O': 14, 'S': 4}.
Example 4:

Input: formula = "Be32"
Output: "Be32"


Constraints:

1 <= formula.length <= 1000
formula consists of English letters, digits, '(', and ')'.
formula is always valid.

"""

"""
observation:
if '(' => push cur_str to stack, start new cur_str
elif ')' => recursive call on cur_str
    use recursive call to handle content inside parenthesis, for result of recursive call, apply multiplier (1 will be omitted) then append the result back into cur_str
else: append char to cur_str

"""


class Solution:
    def countOfAtoms(self, formula: str) -> str:

        def sub_formula(formula):
            """
            process formula without parenthesis
            """

            res = {}

            i = 0
            cur_ele = ''
            num = 0
            while i < len(formula):
                c = formula[i]
                if c.isdigit():
                    j = i + 1
                    while j < len(formula) and formula[j].isdigit():
                        j += 1
                    num = int(formula[i:j])
                    i = j - 1
                elif c.isalpha() and c.isupper():
                    if cur_ele:
                        if num:
                            res[cur_ele] = res.get(cur_ele, 0) + num
                        elif num == 0:  # default to 1
                            res[cur_ele] = res.get(cur_ele, 0) + 1
                    cur_ele = ''
                    num = 0
                    j = i + 1
                    while j < len(formula) and formula[j].isalpha and formula[j].islower():
                        j += 1
                    cur_ele = formula[i:j]
                    i = j - 1

                i += 1

            # last element (maybe with count)
            if cur_ele:
                if num:
                    res[cur_ele] = res.get(cur_ele, 0) + num
                elif num == 0:  # default to 1
                    res[cur_ele] = res.get(cur_ele, 0) + 1

            return res

        # process parenthesis
        cur_str = ''
        stack = []
        i = 0
        while i < len(formula):
            c = formula[i]
            if c == '(':
                stack.append(cur_str)
                cur_str = ''
            elif c == ')':
                # handle ) follows by number
                cur_res = sub_formula(cur_str)
                j = i + 1
                while j < len(formula) and formula[j].isdigit():
                    j += 1
                num = formula[i + 1:j]
                # multiple all counts in cur_res by num
                for k, v in cur_res.items():
                    cur_res[k] = cur_res[k] * (int(num) if num else 1)
                i = j - 1
                cur_str = stack.pop() + str(''.join([k + (str(v) if v > 1 else '') for k, v in cur_res.items()]))
            else:
                cur_str += c
            i += 1

        print('cur_str=%s' % cur_str)
        res = sub_formula(cur_str)

        output = ''
        for k in sorted(res.keys()):
            v = res[k]
            output += k + (str(v) if v > 1 else '')

        return output


def main():
    sol = Solution()
    assert sol.countOfAtoms("H2O") == "H2O", 'fails'

    assert sol.countOfAtoms("Mg(OH)2") == "H2MgO2", 'fails'

    assert sol.countOfAtoms("K4(ON(SO3)2)2") == "K4N2O14S4", 'fails'

    assert sol.countOfAtoms("Be32") == "Be32", 'fails'

if __name__ == '__main__':
   main()