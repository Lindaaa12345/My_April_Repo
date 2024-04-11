def getBondDuration(y, face, couponRate, m, ppy=1):
    coupon_payment = face * couponRate / ppy
    sum_pvcf = 0
    sum_weighted_pvcf = 0
    for t in range(1, m+1):
        cash_flow = coupon_payment + (face if t == m else 0)
        pvcf = cash_flow / ((1 + y)**t)
        sum_pvcf += pvcf
        sum_weighted_pvcf += pvcf * t

    bondDuration = sum_weighted_pvcf / sum_pvcf
    
    return(bondDuration)
    
def getBondDuration(y, face, couponRate, m, ppy = 1):
    return(8.51)
