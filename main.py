
file_path = "books/frankenstein.txt"
    

def bookbot(file_path):
    with open(file_path, "r") as f:
        contents = f.read()
        words = contents.split()
        word_count = len(words)
        print(f"\n--- Begin report of {file_path} ---\n")
        print(f"Word count: {word_count}\n")
        #Counting the letters
        contents = contents.lower()
        letter_count = {}
        count_list = []
        for i in contents:
            if i in letter_count:
                letter_count[i] += 1
            else:
                letter_count[i] = 1
        for key, value in letter_count.items():
            if key.isalpha(): 
                count_list.append(f"The character '{key}' has appeared {value} times.")
                count_list.sort()
        for items in count_list:
            print(items)


bookbot(file_path)

