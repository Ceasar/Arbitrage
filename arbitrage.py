from collections import defaultdict
import csv
import fractions
from pprint import pprint as pp


if __name__ == '__main__':
    with open('trades.csv') as fp:
        csvreader = csv.reader(fp, delimiter=',', quotechar="'")
        trades = defaultdict(dict)
        for line in csvreader:
            wants, wants_n, gives, gives_n = line
            wants_n = fractions.Fraction(wants_n)
            gives_n = fractions.Fraction(gives_n)
            # TODO: Use some min or max
            trades[wants][gives] = gives_n / wants_n
            trades[gives][wants] = wants_n / gives_n
    trades = dict(trades)
    for _ in range(20):
        for a, a_b in trades.items():
            a_c = {}
            for b, b_n in a_b.items():
                try:
                    b_c = trades[b]
                except KeyError:
                    pass
                else:
                    for c, c_n in b_c.items():
                        a_c[c] = b_n * c_n
            trades[a].update(a_c)
    pp(trades)


CROPS = [
    'Wheat',
    'Carrot',
    'Potato',
    'Netherwart',
    'Beetroot',
    'Cocoa',
]
for crop in CROPS:
    # print "SC of {} = {} XP Bottle".format(crop, 3456 * trades[crop]['XP Bottle'])
    print "DC of {} = {} Stamina".format(crop, 3456 * trades[crop]['Stamina'])
