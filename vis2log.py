import sys

HEB = set('אבגדהוזחטיככלמנסעפצקרשתךםןףץ')

def fix_line(line):
    if '<title>' in line:
        return line
    heb_inds = [i for i, c in enumerate(line) if c in HEB]
    if not heb_inds:
        return line
    start = heb_inds[0]
    return line[:start] + '&lrm;' + line[start:]

lines = list(open(sys.argv[1]))
lines = map(fix_line, lines)
open(sys.argv[1], 'w').write(''.join(lines))
