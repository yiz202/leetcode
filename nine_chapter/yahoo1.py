def findrepeating(a,b):
    int_part = a/b
    quotient_part = a%b
    quotient_seen = {}
    num = []
    if a%b == 0: return str(a/b)
    while quotient_part not in quotient_seen:
        quotient_part = quotient_part*10
        quotient_seen[quotient_part] = len(num)
        nextQuo = (quotient_part) % b
        num.append(quotient_part/b)
        quotient_part = nextQuo

    repeating = ''.join([str(i) for i in num[quotient_seen[quotient_part]:]])




