__author__ = 'changhanryu'

def look_and_say(data='1', maxlen=5):
  #TODO populate result list with the look and say numbers

    lst = []
    added_element = ""
    count = 1
    starting_point = data[0]
    data = data[1:] + ""
    while maxlen != 0:
        for i in data:
            if i != starting_point:
                added_element += '{0}{1}'.format(count, starting_point)
                starting_point = i
                lst.append(added_element)
                maxlen -= 1
            else:
                count += 1
                maxlen -= 1

    return lst