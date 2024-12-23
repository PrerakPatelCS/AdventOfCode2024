from collections import defaultdict

with open("Day23.txt", "r") as file:
    adj_list = defaultdict(set)
    for line in file:
        a, b = line.strip().split("-")
        adj_list[a].add(b)
        adj_list[b].add(a)


def puzzle1():
    """
    find 3 fully connected groups.
    1 of them needs to start with t.
    """
    visited = set()

    # start node
    for a in adj_list:
        # neighbor node
        for b in adj_list[a]:
            # both a and b need to be connected to the same node
            a_nodes, b_nodes = set(adj_list[a]), set(adj_list[b])
            c_nodes = a_nodes & b_nodes
            for c in c_nodes:
                x, y, z = sorted([a, b, c])
                if x[0] == "t" or y[0] == "t" or z[0] == "t":
                    visited.add((x, y, z))

    return len(visited)


def puzzle2():
    """
    find the biggest fully connected group.
    return the sorted names of them joined with , for the password
    520 nodes each with exactly 13 neighbors
    """

    ans = []
    for a in adj_list:
        connect = set(adj_list[a])
        connect.add(a)
        new_freq = defaultdict(int)
        for b in adj_list[a]:
            length = len(connect & (set(b) | adj_list[b]))
            new_freq[length] += 1

        if new_freq[12] == 12:
            ans.append(a)

    return ",".join(sorted(ans))


# print(puzzle1()) # 1173
print(puzzle2())  # cm,de,ez,gv,hg,iy,or,pw,qu,rs,sn,uc,wq
