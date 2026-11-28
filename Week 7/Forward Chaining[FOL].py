
facts = {
    ("American", "Robert"),
    ("Enemy", "A", "America"),
    ("Missile", "T1"),
    ("Owns", "A", "T1")
}

rules = [
    (
        [("Missile", "?x"), ("Owns", "A", "?x")],
        ("Sells", "Robert", "?x", "A")
    ),
    (
        [("Missile", "?x")],
        ("Weapon", "?x")
    ),
    (
        [("Enemy", "?x", "America")],
        ("Hostile", "?x")
    ),
    (
        [
            ("American", "?x"),
            ("Weapon", "?y"),
            ("Sells", "?x", "?y", "?z"),
            ("Hostile", "?z")
        ],
        ("Criminal", "?x")
    )
]

def is_variable(x):
    return isinstance(x, str) and x.startswith("?")

def unify(pattern, fact, substitution):
    if len(pattern) != len(fact):
        return None

    substitution = substitution.copy()

    for p, f in zip(pattern, fact):
        if is_variable(p):
            if p in substitution:
                if substitution[p] != f:
                    return None
            else:
                substitution[p] = f
        elif p != f:
            return None

    return substitution

def match_all(premises, facts, substitution=None):
    if substitution is None:
        substitution = {}

    if not premises:
        yield substitution
        return

    first = premises[0]
    remaining = premises[1:]

    for fact in facts:
        new_sub = unify(first, fact, substitution)

        if new_sub is not None:
            yield from match_all(remaining, facts, new_sub)

def substitute(sentence, sub):
    return tuple(sub.get(x, x) for x in sentence)

def forward_chaining(facts, rules, query):
    facts = set(facts)

    while True:
        new_facts = set()

        for premises, conclusion in rules:
            for sub in match_all(premises, facts):
                inferred = substitute(conclusion, sub)

                if inferred not in facts:
                    new_facts.add(inferred)
                    print("New Fact:", inferred)

                result = unify(query, inferred, {})

                if result is not None:
                    print("\nGoal Proved!")
                    return True

        if not new_facts:
            break

        facts.update(new_facts)

    print("\nGoal Cannot Be Proved!")
    return False

query = ("Criminal", "Robert")

forward_chaining(facts, rules, query)
