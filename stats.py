def count_words(text):
    words = text.split()
    return len(words)

def count_chars(text):
    char_stats = {}
    for char in text:
        if char.lower() in char_stats:
            char_stats[char.lower()] += 1
        else:          
            char_stats[char.lower()] = 1
    return char_stats

def sort_on(items):
    return items["num"]

def make_dict_of_chars(char_stats):
    character_count = []
    for k in char_stats:
        character_count.append({"char": k, "num": char_stats[k]})
    character_count.sort(reverse=True, key=sort_on)
    return character_count


