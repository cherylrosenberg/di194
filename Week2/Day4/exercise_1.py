import random

def get_words_from_file(file_path):
    with open(file_path, "r") as f:
        content = f.read()
    return content.split()


def get_random_sentence(length):
    words = get_words_from_file(r"Week2\Day4\words.txt")
    
    chosen = [random.choice(words) for _ in range(length)]
    
    return " ".join(chosen).lower()

def main():
    length = 0
    # get input, validate, generate sentence
    try:
        length = int(input("Enter scentence length (2-20)"))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    if length < 2 or length > 20:
        print("Please enter a number between 2 and 20")
        return
    
    sentence = get_random_sentence(length)
    print(sentence)

main()
