import sys

HEB = set('אבגדהוזחטיככלמנסעפצקרשתךםןףץ')

def fix_line(line):
    if '<title>' in line:
        return line
    heb_inds = [i for i, c in enumerate(line) if c in HEB]
    if not heb_inds:
        return line
    start = heb_inds[0]
    end = heb_inds[-1] + 1
    return line[:start] + line[start:end][::-1] + line[end:]

lines = list(open(sys.argv[1]))
lines = map(fix_line, lines)
open(sys.argv[1], 'w').write(''.join(lines))
