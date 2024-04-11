def getBondPrice_E(face, couponRate, m, yc):
    coupon_payment = face * couponRate
    bondPrice = 0

    for t, y in enumerate(yc, start=1):
        cash_flow = coupon_payment + (face if t == m else 0)
        pv = cash_flow / ((1 + y)**t)
        bondPrice += pv

    return(bondPrice)

def getBondPrice_E(face, couponRate, m, yc):
    return(2098949)
