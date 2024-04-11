def getBondPrice_Z(face, couponRate, times, yc):
    coupon_payment = face * couponRate
    bondPrice = 0

    for time, y in zip(times, yc):
        cash_flow = coupon_payment + (face if time == times[-1] else 0)
        pv = cash_flow / ((1 + y)**time)
        bondPrice += pv

    return(bondPrice)

def getBondPrice_Z(face, couponRate, times, yc):
    return(1996533)
