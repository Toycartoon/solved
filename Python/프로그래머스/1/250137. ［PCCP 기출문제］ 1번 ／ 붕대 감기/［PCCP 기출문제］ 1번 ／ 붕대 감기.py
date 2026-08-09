def solution(bandage, health, attacks):
    success = 0
    hp = health
    idx = 0
    for i in range(attacks[-1][0]+1):
        if i == attacks[idx][0]:
            success = 0
            hp -= attacks[idx][1]
            idx += 1
            
            if hp <= 0:
                return -1
        else:
            success += 1
            hp += bandage[1]
            if success == bandage[0]:
                success = 0
                hp += bandage[2]
            hp = min(health, hp)

    return hp
