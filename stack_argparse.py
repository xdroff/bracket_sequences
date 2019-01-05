import argparse

parser = argparse.ArgumentParser()
parser.add_argument("sequences", help="Input a bracket sequence")
args = parser.parse_args()


class Stack():
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def top(self):
        try:
            return self.items[-1]
        except IndexError:
            return False
    def is_empty(self):
        if not len(self.items):
            return True
        else:
            False

def main(bracket_sequences: str):
    brackets_closing = [')', '}', '>', ']']
    brackets_opening = ['(', '{', '<', '[']
    mapping = {brackets_opening[0]: brackets_closing[0],
               brackets_opening[1]: brackets_closing[1],
               brackets_opening[2]: brackets_closing[2],
               brackets_opening[3]: brackets_closing[3]}
    stack = Stack()
    for x in bracket_sequences:
        balanced_closing = True
        if x in brackets_opening:
            stack.push(x)
        elif x in brackets_closing:
            try:
                if mapping[stack.top()] == x:
                    stack.pop()
            except KeyError:
                balanced_closing = False
                break
    if stack.is_empty() and balanced_closing:
            print(f'Bracket sequences: "{bracket_sequences}" is correct')
    else:
        print(f'Bracket sequences: "{bracket_sequences}" is not correct')

if __name__ == "__main__":
    main(args.sequences)
