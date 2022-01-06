char_list = ["i", "o", "u", "ø", "t", "n", "k"]
string = "nøkk"

matched_list = [characters in char_list for characters in string]

print(matched_list)
[True, True, True, False]

string_contains_chars = all(matched_list)

print(string_contains_chars)
