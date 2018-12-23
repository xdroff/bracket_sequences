def main(bracket_sequences: str):
    count = 0
    for x in bracket_sequences:
        if count == -1:
            break
        if x == '(':
            count += 1
        if x == ')':
            count -= 1
    if count == 0:
        print(f'Bracket sequences: "{bracket_sequences}" is correct')
    else:
        print(f'Bracket sequences: "{bracket_sequences}" is not correct')

if __name__ == "__main__":
    main('())')
