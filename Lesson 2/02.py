def divided_in_range(a, b, c):
    segment_length = b - a - 1

    if c - a % c < (b - a) % c:
        result = segment_length//c + 1
    else:
        result = segment_length//c

    return result



