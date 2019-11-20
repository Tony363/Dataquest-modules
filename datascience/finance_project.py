def Compute_investment(income,dependants,filer):
    tax_amount = 0
    if (income >= 0 and income <= 9700) and filer =='Single':
        income *= 0.1
        tax_amount += income
    elif (income >= 9701 and income <= 39475) and filer =='Single':
        income *= 0.12
        tax_amount += income
    elif (income >= 84201 and income <= 160725) and filer =='Single':
        income *= 0.24
        tax_amount += income
    elif (income >= 160726 and income <= 204100) and filer =='Single':
        income *= 0.32
        tax_amount += income
    elif (income >= 204101 and income <= 510300) and filer =='Single':
        income *= 0.35
        tax_amount += income
    elif (income > 510301) and filer =='Single':
        income *= 0.37
        tax_amount += income
        pass
        
    
    return tax_amount

print(Compute_investment(6000000,0, 'Single'))
        
