from collections import deque

def read_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    return [line.strip().split() for line in lines]

def decode_message(pairs):
    # Create a dictionary to store words corresponding to each number
    word_dict = {int(num): word for num, word in pairs}

    # Find the maximum number in the dictionary
    max_num = max(word_dict.keys())

    # Determine the size of the pyramid based on the maximum number
    pyramid_size = 0
    while pyramid_size * (pyramid_size + 1) // 2 < max_num:
        pyramid_size += 1

    # Traverse the pyramid and collect the words
    message = ''
    current_num = 1
    for level in range(1, pyramid_size + 1):
        # Collect the words corresponding to the numbers in the current level
        for _ in range(level):
            message += word_dict.get(current_num, '') + ' '
            current_num += 1

    return message.strip()

def main():
    filename = 'coding_qual_input.txt'
    pairs = read_file(filename)
    decoded_message = decode_message(pairs)
    print("Decoded Message:", decoded_message)

if __name__ == "__main__":
    main()

