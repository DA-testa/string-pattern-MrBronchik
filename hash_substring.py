# python3

def read_input():
    choice = input().strip()
    if choice == 'I':
        pattern = input().strip()
        text = input().strip()
    elif choice == 'F':
        filename = input().strip()
        with open(filename, 'r') as f:
            pattern = f.readline().strip()
            text = f.readline().strip()
    return pattern, text

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
    print_occurrences(get_occurrences(*read_input()))

