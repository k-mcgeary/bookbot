def get_num_words(text):
    words = text.split()
    return len(words)

def character_count(text):
    char_count = {}
    
    for char in text:
        if char.lower() in char_count:
            char_count[char.lower()] += 1
        else:
            char_count[char.lower()] = 1
    return char_count

def sort_dict(char_count):
    dict_list = []

    for key, value in char_count.items():
        dict_list.append({'char':key, 'count':value})
    
    dict_list.sort(key=lambda item: item['count'], reverse=True)

    return dict_list        
