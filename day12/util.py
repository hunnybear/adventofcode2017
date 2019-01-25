def get_islands(pipes):

    islands = []

    for a, connections in pipes.items():
        proximal = set(connections)
        proximal.add(a)

        match_found = True

        while match_found:
            match_found = False

            for i in reversed(range(len(islands))):
                if islands[i] & proximal:
                    match_found = True
                    proximal.update(islands.pop(i))

        islands.append(proximal)

    return islands

    return set(frozenset(island) for island in islands.values())
