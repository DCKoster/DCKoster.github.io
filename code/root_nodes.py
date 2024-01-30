# 4 person
def generate_roots_foursum(root_nodes):
    for a in range(1,20):
        for b in range(1,20):
            for c in range(1,20):
                for d in range(1,20):
                    l = [a,b,c,d]
                    s = sorted(l)
                    if s[3] != s[0] + s[1] + s[2]: 
                        continue
                    if s[2] - s[1] - s[0] <= 0:
                        root_nodes.append(l)

    return root_nodes
                   
# product
def generate_roots_product(root_nodes):
    for a in range(1,50):
        for b in range(1,50):
            for c in range(1,50):
                l = [a,b,c]
                s = sorted(l)
                if s[2] != s[0] * s[1]: continue
                if s[1] % s[0] > 0 or s[1] == s[2]:
                    root_nodes.append(l)

    return root_nodes

# filter the multiples for four sum riddle
def filter_multiples(triples):
    filtered_triples = []
    for i, triple in enumerate(triples):
        is_multiple = False
        for j, other_triple in enumerate(triples):
            if i != j and all(x % y == 0 for x, y in zip(triple, other_triple)):
                is_multiple = True
                break
        if not is_multiple:
            filtered_triples.append(triple)
    return filtered_triples

