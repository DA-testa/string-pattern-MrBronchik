# python3

import sys

def read_input():
    try:
        # this function needs to acquire input both from keyboard and file
        # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow

        input_type = input().strip()
        if input_type == 'F':
            filename = input().strip()
            with open(filename, 'r') as f:
                pattern = f.readline().strip()
                text = f.readline().strip()
        elif input_type == 'I':
            pattern = input().strip()
            text = input().strip()
        else:
            return None

        # return both lines in one return
        return pattern, text

    except EOFError:
        return None

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    p = 31  # choose a prime number to avoid collisions
    m, n = len(pattern), len(text)
    p_pow = [pow(p, i) for i in range(m)]  # precompute powers of p
    pattern_hash = sum([ord(pattern[i]) * p_pow[m-1-i] for i in range(m)])  # compute pattern hash
    text_hash = sum([ord(text[i]) * p_pow[m-1-i] for i in range(m)])  # compute initial text hash
    matches = []
    for i in range(n-m+1):
        if pattern_hash == text_hash:  # compare hashes
            if pattern == text[i:i+m]:  # compare strings
                matches.append(i)
        if i < n-m:  # compute new text hash
            text_hash = (text_hash - ord(text[i]) * p_pow[m-1]) * p + ord(text[i+m])
    return matches


if __name__ == '__main__':
    input_data = read_input()
    if input_data is None:
        print('Error: could not read input')
    else:
        print_occurrences(get_occurrences(*input_data))
