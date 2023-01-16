def is_operand(x):
    return x.isdigit()


def postfix_to_infix(exp):
    s = []
    for i in exp:
        if (is_operand(i)) or i == " ":
            if i != " ":
                s.insert(0, i)
        else:
            op1 = s[0]
            s.pop(0)
            op2 = s[0]
            s.pop(0)
            s.insert(0, "(" + op2 + i + op1 + ")")

    return s[0]


exp = input().strip()
print(eval(postfix_to_infix(exp)))
