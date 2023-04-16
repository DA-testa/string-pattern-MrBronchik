import sys

def read_input():
    # read the input choice
    print("Enter input choice (i for keyboard input, f for file input):")
    choice = input().strip().lower()
    print(f"Input choice: {choice}")
    if choice == 'i':
        # read from keyboard
        print("Enter pattern:")
        pattern = input().strip()
        print(f"Pattern: {pattern}")
        print("Enter text:")
        text = input().strip()
        print(f"Text: {text}")
    elif choice == 'f':
        # read from file
        print("Enter filename:")
        filename = input().strip()
        print(f"Filename: {filename}")
        try:
            with open(filename, 'r') as f:
                pattern = f.readline().strip()
                text = f.readline().strip()
                print(f"Pattern: {pattern}")
                print(f"Text: {text}")
        except FileNotFoundError:
            print(f"Error: file '{filename}' not found", file=sys.stderr)
            sys.exit(1)
        except Exception as e:
            print(f"Error: could not read file '{filename}': {e}", file=sys.stderr)
            sys.exit(1)
    else:
        print(f"Error: invalid input choice '{choice}'", file=sys.stderr)
        sys.exit(1)
    return pattern, text


def print_occurrences(output):
    print(' '.join(map(str, output)))


def get_occurrences(pattern, text):
    p = 31  # choose a prime number to avoid collisions
    m, n = len(pattern), len(text)
    p_pow = [pow(p, i) for i in range(m)]  # precompute powers of p
    pattern_hash = sum([ord(pattern[i]) * p_pow[m - 1 - i] for i in range(m)])  # compute pattern hash
    text_hash = sum([ord(text[i]) * p_pow[m - 1 - i] for i in range(m)])  # compute initial text hash
    matches = []
    for i in range(n - m + 1):
        if pattern_hash == text_hash:  # compare hashes
            if pattern == text[i:i + m]:  # compare strings
                matches.append(i)
        if i < n - m:  # compute new text hash
            text_hash = (text_hash - ord(text[i]) * p_pow[m - 1]) * p + ord(text[i + m])
    return matches


if __name__ == '__main__':
    input_data = read_input()
    if input_data is None:
        print('Error: could not read input')
    else:
        print_occurrences(get_occurrences(*input_data))
