import re
from collections import defaultdict

with open("Day3input.txt") as f:
    data = f.readlines()
    f.close()

# PART1    
#1295 @ 965,933: 10x15
REGEX = r'#([0-9]+) @ ([0-9]+),([0-9]+): ([0-9]+)x([0-9]+)'
    
input = []

for line in data:
    match = re.match(REGEX, line)
    input.append({
        'id': int(match.group(1)),
        'x': int(match.group(2)),
        'y': int(match.group(3)),
        'w': int(match.group(4)),
        'h': int(match.group(5))
    })

board = defaultdict(list)
for line in input:
    squares = [(x+line['x'], line['y']) for x in range(line['w'])]
    claim_squares = [(x, y+i) for x, y in squares for i in range(line['h'])]
    for square in claim_squares:
        board[square].append(line['id'])

overlapping_squares = sum([1 for key, value in board.items() if len(value) > 1])
print("There are {} square inches of fabric are within two or more claims".format(overlapping_squares))

# PART 2
claims = set(x['id'] for x in input)
overlapping_claims = set()
for key, value in board.items():
    if len(value) > 1:
        for v in value:
            overlapping_claims.add(v)

valid_claim = claims - overlapping_claims
id = valid_claim.pop()
print("There only claim that does not overlap has {} as id".format(id))