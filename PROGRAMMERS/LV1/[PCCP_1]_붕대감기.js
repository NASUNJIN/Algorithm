function solution(bandage, health, attacks) {
    // t: 시전 시간 
    // x: 초당 회복량 
    // y: 추가 회복량
    const [t, x, y] = bandage
    const maxHP = health  // 최대 체력
    let HP = health // 현재 체력
    let continueHeal = 0 // 연속 힐 횟수
    let turn = 0
    

    while (attact.length) {
        turn++  // 턴 증가
        const [attackTime, damage] = attacks[0]

        // 몬스터에게 공격 받은 턴은 회복 불가
        if (attackTime === turn) {
            attacks = attacks.slice(1)  // 처리된 공격 정보를 배열에서 제거
            HP -= damage
            continueHeal = 0
            print("몬스터 공격 HP:", HP)

            if(HP <= 0) return -1  // 만약 현재 피가 0보다 작을 경우 사망
        } else {
            HP += x
            continueHeal ++
            // 최대 체력 이상 회복 불가
            if(HP >= maxHP) {
                HP = maxHP
            }
            // 연속 회복 성공 시 추가 회복
            if(continueHeal >= t) {
                HP += y
                continueHeal = 0
                print("연속 회복 성공 HP:", HP)
            }
        }
    }

    return HP
}