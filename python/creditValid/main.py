def getBIN(digit,valid):
    try:
        if valid:
            if digit[0] == '4':
                return 'Visa'
            elif digit[0] == '5':
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
    timeCard = [num * 2 if num * 2 < 10 else num * 2 - 9 for num in evenNum]
    return (sum(oddNum)+sum(timeCard))%10==0
    
cc='4012888888881881'
valid = creditChecker(cc.replace(' ',''))
company = getBIN(cc,valid)
print(f'{cc}|{valid}|{company}')
