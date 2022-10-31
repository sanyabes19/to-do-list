def length_identifier(variable, length):
    '''Cut string length if it is longer than expected'''
    if len(variable) > length:
        variable = variable[:length]
    return variable

def description_as_title(title, description):
    '''If description is empty, substitute with title'''
    if description == '':
        description = title
    return description

def priority_check(priority, type, range):
    '''Check is priority is valid and in range'''
    if type(priority) != type and priority not in range(10) :
        priority = input('Specified wrong value. Please, enter 1 to 10')

print(priority_check(2,int,10))

