import random

plist=[
    [0,0,"NPC","First"],
    [0,0,"NPC","Second"],
    [0,0,"NPC","Third"],
    [0,0,"PC","First"],
    [0,0,"PC","Second"],
    [0,0,"PC","Third"],
    ]

cointoss_victor="NPC"
sortlist = sorted(
    plist, key=lambda x: (
        x[0], x[1], x[2]==cointoss_victor
        ), reverse=True
    )

print(sortlist)
