from test_framework import generic_test

legal_bytes = {str(i) for i in range(256)}


def get_valid_ip_address(s):
    options = []
    for pref in eightbit_prefixes(s):
        options.append([pref])

    for _ in range(3):
        grown_options = []
        for option in options:
            opt_len = sum(len(w) for w in option)
            for pref in eightbit_prefixes(s[opt_len:]):
                grown_option = list(option)
                grown_option.append(pref)
                grown_options.append(grown_option)
        options = grown_options
    return ['.'.join(opt) for opt in options if sum(len(w) for w in opt) == len(s)]


def eightbit_prefixes(s):
    if not s:
        return
    for i in range(1, min(4, len(s) + 1)):
        pref = s[:i]
        if pref in legal_bytes:
            yield pref


def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "valid_ip_addresses.py",
            'valid_ip_addresses.tsv',
            get_valid_ip_address,
            comparator=comp))
