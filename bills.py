
initialMoney = input('Type your money: ')


def get_initial_value():
    if(initialMoney.isnumeric()):
        return {"value": float(initialMoney), "isNumber": True}
    else:
        return {"value": initialMoney, "isNumber": False}


def get_result_value(percentage):
    return get_initial_value().get('value')*percentage


def get_results():
    percentages = (0.1, 0.1, 0.1, 0.6, 0.1)
    final_results = {
    "financial freedom": get_result_value(percentages[0]), 
    "saving long term": get_result_value(percentages[1]), 
    "personal development": get_result_value(percentages[2]), 
    "basic needs": get_result_value(percentages[3]), 
    "leisure": get_result_value(percentages[4])
    }
    print('_______ YOUR RESULTS _______')
    print('Initial amount of money: ', get_initial_value().get('value'))
    for result in final_results:
        print(result, ' ', final_results[result])


while(get_initial_value().get('isNumber') == False):
    print('Please type a number')
    initialMoney = input('Type your money: ')

get_results()
