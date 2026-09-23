"""
Zebra Puzzle (Einstein's Riddle) - solved with traditional nested loops.
Only library used: itertools.permutations, purely to generate the 120
possible orderings of 5 elements (no constraint-solver).
"""

from itertools import permutations

# Houses are numbered 1 through 5 (left to right)
HOUSES = [1, 2, 3, 4, 5]

# Precompute all 120 permutations as an array, so we can loop through
# them with an index i instead of iterating directly over the
# permutations object.
ALL_PERMS = list(permutations(HOUSES))
NUM_PERMS = len(ALL_PERMS)

def right_of(a, b):
    """a is directly to the right of b"""
    return a == b + 1

def next_to(a, b):
    """a is directly next to b (left or right)"""
    return abs(a - b) == 1

def solve():
    solutions = []

    # We assign each category a permutation of house numbers.
    # Each variable (e.g. red) is simply an integer: the house number
    # (1 through 5) that value has been assigned to.
    for i1 in range(NUM_PERMS):
        perm = ALL_PERMS[i1]
        red, green, ivory, yellow, blue = perm[0], perm[1], perm[2], perm[3], perm[4]

        # 6. The green house is directly to the right of the ivory house
        if not right_of(green, ivory):
            continue

        for i2 in range(NUM_PERMS):
            perm = ALL_PERMS[i2]
            englishman, spaniard, ukrainian, norwegian, japanese = perm[0], perm[1], perm[2], perm[3], perm[4]

            # 2. The Englishman lives in the red house
            if englishman != red:
                continue
            # 10. The Norwegian lives in the first house
            if norwegian != 1:
                continue
            # 15. The Norwegian lives next to the blue house
            if not next_to(norwegian, blue):
                continue

            for i3 in range(NUM_PERMS):
                perm = ALL_PERMS[i3]
                coffee, tea, milk, oj, water = perm[0], perm[1], perm[2], perm[3], perm[4]

                # 4. Coffee is drunk in the green house
                if coffee != green:
                    continue
                # 5. The Ukrainian drinks tea
                if tea != ukrainian:
                    continue
                # 9. Milk is drunk in the middle house
                if milk != 3:
                    continue

                for i4 in range(NUM_PERMS):
                    perm = ALL_PERMS[i4]
                    old_gold, kools, chesterfields, lucky_strike, parliaments = perm[0], perm[1], perm[2], perm[3], perm[4]

                    # 8. Kools are smoked in the yellow house
                    if kools != yellow:
                        continue
                    # 13. The Lucky Strike smoker drinks orange juice
                    if lucky_strike != oj:
                        continue
                    # 14. The Japanese man smokes Parliaments
                    if parliaments != japanese:
                        continue

                    for i5 in range(NUM_PERMS):
                        perm = ALL_PERMS[i5]
                        dog, snails, fox, horse, zebra = perm[0], perm[1], perm[2], perm[3], perm[4]

                        # 3. The Spaniard owns a dog
                        if dog != spaniard:
                            continue
                        # 7. The Old Gold smoker owns snails
                        if snails != old_gold:
                            continue
                        # 11. The Chesterfield smoker lives next to the man with the fox
                        if not next_to(chesterfields, fox):
                            continue
                        # 12. Kools are smoked next to the house with the horse
                        if not next_to(kools, horse):
                            continue

                        # All 15 clues have now been checked -> valid solution
                        solution = {
                            'house': HOUSES,
                            'red': red, 'green': green, 'ivory': ivory,
                            'yellow': yellow, 'blue': blue,
                            'englishman': englishman, 'spaniard': spaniard,
                            'ukrainian': ukrainian, 'norwegian': norwegian,
                            'japanese': japanese,
                            'coffee': coffee, 'tea': tea, 'milk': milk,
                            'oj': oj, 'water': water,
                            'old_gold': old_gold, 'kools': kools,
                            'chesterfields': chesterfields,
                            'lucky_strike': lucky_strike,
                            'parliaments': parliaments,
                            'dog': dog, 'snails': snails, 'fox': fox,
                            'horse': horse, 'zebra': zebra,
                        }
                        solutions.append(solution)

    return solutions


def print_solution(sol):
    colors = {v: k for k, v in [('red', sol['red']), ('green', sol['green']),
                                  ('ivory', sol['ivory']), ('yellow', sol['yellow']),
                                  ('blue', sol['blue'])]}
    nationalities = {v: k for k, v in [('Englishman', sol['englishman']),
                                        ('Spaniard', sol['spaniard']),
                                        ('Ukrainian', sol['ukrainian']),
                                        ('Norwegian', sol['norwegian']),
                                        ('Japanese', sol['japanese'])]}
    drinks = {v: k for k, v in [('coffee', sol['coffee']), ('tea', sol['tea']),
                                  ('milk', sol['milk']), ('orange juice', sol['oj']),
                                  ('water', sol['water'])]}
    smokes = {v: k for k, v in [('Old Gold', sol['old_gold']), ('Kools', sol['kools']),
                                  ('Chesterfields', sol['chesterfields']),
                                  ('Lucky Strike', sol['lucky_strike']),
                                  ('Parliaments', sol['parliaments'])]}
    pets = {v: k for k, v in [('dog', sol['dog']), ('snails', sol['snails']),
                                ('fox', sol['fox']), ('horse', sol['horse']),
                                ('zebra', sol['zebra'])]}

    print(f"{'House':<7}{'Color':<8}{'Nationality':<13}{'Drink':<14}{'Smoke':<15}{'Pet':<8}")
    for h in HOUSES:
        print(f"{h:<7}{colors[h]:<8}{nationalities[h]:<13}{drinks[h]:<14}{smokes[h]:<15}{pets[h]:<8}")

    zebra_house = sol['zebra']
    nationality = nationalities[zebra_house]
    print(f"\n>>> The {nationality} owns the zebra, in house {zebra_house}.")


if __name__ == "__main__":
    solutions = solve()
    print(f"Number of solutions found: {len(solutions)}\n")
    for sol in solutions:
        print_solution(sol)
