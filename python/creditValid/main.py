def getBIN(digit,valid):
    try:
        if valid:
            if digit[0] == '4':
                return 'Visa'
            elif digit == '5':
                return 'Mastercard'
            else:
                return 'Unknown'
                
        else:
            return '-'
    except Exception:
        return 'Unknown'

def creditChecker(ccn):
    evenNum = [int(ccn[num]) for num in range(len(ccn)) if int(num)%2==0]
    oddNum = [int(ccn[num]) for num in range(len(ccn)) if int(num)%2==1]
    timeCard = [num*2 for num in evenNum]
    for i in range(len(timeCard)-1):
        str(evenNum[i])
        if len(str(timeCard[i])) > 1:
            timeCard[i] = int(str(timeCard[i])[0])+int(str(timeCard[i])[1])
    return (sum(oddNum)+sum(timeCard))%10==0
    
cc='3566002020360505'
valid = creditChecker(cc.replace(' ',''))
company = getBIN(cc,valid)
print(f'{cc}|{valid}|{company}')
