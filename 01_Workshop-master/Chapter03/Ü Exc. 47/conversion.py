def convert_usd_to_aus(amount,rate=0.75): 
    return amount/rate

#define a nother function
def convert_and_sum_list (usd_list, rate=0.75):
    sum = 0
    for amount in usd_list: 
        sum += convert_usd_to_aus(amount, rate=rate)
    return sum

print(convert_and_sum_list([1,3]))


#additional function

def convert_and_sum_list_kwargs(usd_list, **kwargs):
    total = 0
    for amount in usd_list:
        total += convert_usd_to_aud(amount, **kwargs)
    return total

print(convert_and_sum_list_kwargs([1, 3], rate=0.8))

