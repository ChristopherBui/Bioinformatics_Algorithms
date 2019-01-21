# note the returned locations will be based on python's 0-based index
def substring_locations(string, sub):
    start = 0
    end = len(sub)

    locations = []

    while end <= len(string):
        if string[start:end] == sub:
            locations.append(start)
        else:
            pass

        start += 1
        end += 1

    return locations
