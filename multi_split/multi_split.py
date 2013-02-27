

def multi_split(string_to_split, list_of_delimiters):
    string_to_split = [string_to_split]
    for each in list_of_delimiters:
        output = []
        for item in string_to_split:
            result = 0
            while result >= 0:
                old_result = result
                result = item[result:].find(each)
                if result >= 0:
                    output.append(item[old_result:result + old_result])
                    result += len(each) + old_result
            output.append(item[old_result:])
        string_to_split = output
    return string_to_split

print multi_split('ddxy', ['d']) == ['', '', 'xy']
print multi_split('dogxycat', ['og', 'y']) == ['d', 'x', 'cat']
