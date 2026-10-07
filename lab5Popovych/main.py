import sys
import traceback
import unittest


class ValidationError(ValueError): #not final code
    def __init__(self, message: str, index: list[int] = None):
        self.index = index or []
        if self.index:
            pos = ", ".join(f"at {i}" for i in self.index)
            super().__init__(f"{message}: ({pos})")
        else:
            super().__init__(message)



def validateString(s):
    stack = []
    errors = []
    for i, char in enumerate(s):
        if char == '(' or char == '<' or char == '[' or char == '{':
            stack.append((char, i))
        elif char ==')' or char == ']' or char == '>' or char == '}':
            if not stack:
                errors.append(i)
                continue
            top_char, top_index = stack[-1]
            if(char == ')' and top_char != '(') or (char == ']' and top_char != '[') or (char == '>' and top_char != '<') or (char == '}' and top_char != '{'):
                errors.append(i)
            else:
                stack.pop()
    while stack:
        char, index = stack.pop()
        errors.append(index)

    if(errors):
        errors.sort()
        highlight = [' '] * len(s)
        for index in errors:
            if 0 <= index < len(s):
                highlight[index] = '^'
        print(s, file=sys.stderr)
        print(''.join(highlight), file=sys.stderr)
        raise ValidationError("is not a valid expression", index=errors)
    return True
def run():
    running = True
    while running:
        string = input('Enter a string: ')
        try:
            if validateString(string):
                print('The expression is valid')
        except ValidationError:
            traceback.print_exc()
        finally:
            answer = input('Do you want to enter another string? (y/n): ')
            if answer != 'y':
                running = False


if __name__ == '__main__':
    run()