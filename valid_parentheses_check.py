def is_valid_parentheses(text):

    # to store opening brackets
    stack = []

    # which opening bracket belongs to each closing bracket
    pairs = {
        ")": "(",
        "]": "[",
        "}": "{"
    }

    for char in text:

        # If it is an opening bracket remember it by pushing onto the stack
        if char in "([{":
            stack.append(char)

        # closing bracket
        else:

            # no opening bracket to match it
            if not stack:
                return False
            
            # Get the latest opening bracket
            top = stack.pop()

            # Check if they belong together
            if top != pairs[char]:
                return False

    # If the stack is empty,
    # every opening bracket had a matching closing bracket
    return not stack

print(is_valid_parentheses("({}{}[{()}()])"))