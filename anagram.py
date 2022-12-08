def find_anagrams(word_list):
    anagram_keys = set()
    dictionary = {}

    for word in word_list:
        # sort the char in each word, anagrams will return same result
        sorted_word = "".join(sorted(word))

        if sorted_word in dictionary:
            # words are not anagrams of themselves
            if word in dictionary[sorted_word]:
                continue
            else:
                # an anagram exist so we put in the set of keys
                anagram_keys.add(sorted_word)
                # append the word to the key
                dictionary[sorted_word].append(word)

        else:
            # create an entry in the dictionary for the anagram
            dictionary[sorted_word] = [word]

    output = []
    for i in anagram_keys:
        output.append(dictionary[i])
    return output


if __name__ == '__main__':
    word_list = [['xyz', 'abcde', 'uured', 'cdeab', 'yzxy', 'badec', 'yxy'], 
    ['deltas', 'a', 'desalt', 'a', 'lasted', 'salted', 'slated', 'staled', 'retainers', 'ternaries','generating', 'greatening', 'resmelts', 'smelters', 'termless'], 
    ['a', 'a', 'ab', 'ba', 'ab', 'cc', 'cc', 'cb', 'bc','12','21'],
    ['','']
    ]
    for list in word_list:
        print(find_anagrams(list))
