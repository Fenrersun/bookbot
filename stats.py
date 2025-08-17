def get_num_letter(t):
	endtext = t.split()
	num = len(endtext)
	return num

def get_num_each_letter(t):
    letterdict = {}
    for char in t:
        if char.isalpha():
            char = char.lower()
            if char in letterdict:
                letterdict[char] += 1
            else:
                letterdict[char] = 1
        else:
            if char in letterdict:
                letterdict[char] += 1
            else:
                letterdict[char] = 1
    return letterdict

def sort_on(item):
    return item["num"]

def char_sort(char_dict):
    def sort_on(items):
        return items["num"]

    sorted_list = []
    for k,v in char_dict.items():
        tempdict = {"char":k,"num":v}
        sorted_list.append(tempdict)
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list