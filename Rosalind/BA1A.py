def count(text, pattern):
    start = 0
    end = len(pattern)

    count = 0

    for i in range(len(text) - len(pattern) + 1):
        if text[start:end] == pattern:
            count += 1
        else:
            pass

        start += 1
        end += 1

    return count
