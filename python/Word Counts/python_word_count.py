def token(string_input):
    token_list = string_input.lower().split(' ')
    dict_unique = {}
    for each_token in token_list:
        if each_token in dict_unique:
            dict_unique[each_token] += 1
        else:
            dict_unique[each_token] = 1
    return print(dict_unique)

#https://stackoverflow.com/questions/2068349/understanding-get-method-in-python
def count_string(string_input):
    token_list = string_input.split(' ')
    dict_unique = {}
    for each in token_list:
        dict_unique[each] = dict_unique.get(each, 0) + 1
    return print(dict_unique)

count_string('My name is Grant grant Aguinaldo. What is your name my name.?')