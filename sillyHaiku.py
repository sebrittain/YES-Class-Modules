import random

def make_haiku(part1, part2, part3):
    p1 = part1.split('\n')
    p2 = part2.split('\n')
    p3 = part3.split('\n')
    random.shuffle(p1)
    random.shuffle(p2)
    random.shuffle(p3)

    haiku = []
    h = p1[0] + '\n' + p2[0] + '\n' +p3[0]
    haiku.append(h)
    
    return haiku

part1 = """\
A silly sailor
A giggling goose
The obese ostrich
The strange sister
The hungry T-Rex
This little piggy"""

part2 = """\
Has trouble seeing the sky
Is wearing red pajamas
Is singing Yankee Doodle
Was skipping along the way
Was sailing to Jupiter
Ate a watermelon cake"""

part3 = """\
With a crooked eye
When we said goodbye
While the cat ran away
While I fly a kite
In a stranger place
With a slight scowl
To grandmother's house"""



haiku = make_haiku(part1, part2, part3)
for item in haiku:
    print(item)
