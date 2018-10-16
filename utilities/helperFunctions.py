
def uniqueList(seq):
    if seq != []:
        if not isinstance(seq[0], list):
            seen = set()
            seen_add = seen.add
            return [x for x in seq if not (x in seen or seen_add(x))]
        else:
            seq = list(map(tuple, seq))
            seen = set()
            seen_add = seen.add
            return [x for x in seq if not (x in seen or seen_add(x))]
    else:
        return []
