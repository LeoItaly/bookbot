def get_number_of_words(text):
    words = text.split()
    return len(words)

def get_character_count(text):
    char_count = {}
    for character in text:
        lower_character = character.lower()
        if lower_character in char_count:
            char_count[lower_character] += 1
        else:
            char_count[lower_character] = 1
    return char_count

def sort_character_count(char_count):
    sorted_list = []
    for char, count in char_count.items():
        if char.isalpha():
            sorted_list.append({"char": char, "num": count})
    sorted_list.sort(reverse=True, key=lambda item: item["num"])
    for item in sorted_list[:8]:
        print(f"{item['char']}: {item['num']}")
    return sorted_list

    