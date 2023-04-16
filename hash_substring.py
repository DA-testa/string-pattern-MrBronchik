import sys

def read_input():
    choice = input().strip().lower()
    if choice == 'i':
        pattern = input().strip()
        text = input().strip()
    elif choice == 'f':
        filename = input().strip()
        try:
            with open(filename, 'r') as f:
                pattern = f.readline().strip()
                text = f.readline().strip()
        except FileNotFoundError:
            print('Error: file not found', file=sys.stderr)
            sys.exit(1)
        except Exception as e:
            print(f'Error: could not read file: {e}', file=sys.stderr)
            sys.exit(1)
    else:
        print('Error: invalid input choice', file=sys.stderr)
        sys.exit(1)
    return pattern, text


def print_occurrences(output):
    print(' '.join(map(str, output)))


def get_occurrences(pattern, text):
    p = 31
    m, n = len(pattern), len(text)
    p_pow = [pow(p, i) for i in range(m)]
    pattern_hash = sum([ord(pattern[i]) * p_pow[m - 1 - i] for i in range(m)])
    text_hash = sum([ord(text[i]) * p_pow[m - 1 - i] for i in range(m)])
    matches = []
    for i in range(n - m + 1):
        if pattern_hash == text_hash:
            if pattern == text[i:i + m]:
                matches.append(i)
        if i < n - m:
            text_hash = (text_hash - ord(text[i]) * p_pow[m - 1]) * p + ord(text[i + m])
    return matches


if __name__ == '__main__':
    input_data = read_input()
    if input_data is None:
        print('Error: could not read input')
    else:
        print_occurrences(get_occurrences(*input_data))
