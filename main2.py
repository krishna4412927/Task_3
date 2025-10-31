def decode(pattern): # DECODING LOGIC
    result = ""
    i = 0
    while i < len(pattern):
        letter = pattern[i]
        
        # check if it's a valid letter
        if not letter.isalpha():
            return " Invalid pattern! Expected a letter."
        i += 1
        number = ""

        # collect digits after the letter
        while i < len(pattern) and pattern[i].isdigit():
            number += pattern[i]
            i += 1

        # if no number found
        if number == "":
            return " Invalid pattern! Missing number after letter."

        count = int(number)
        if count <= 0:
            return " Invalid pattern! Number must be positive."

        # repeat the letter ‘count’ times
        result += letter * count
    return result
  
def encode(text): # ENCODING LOGIC
    if not text:
        return ""

    result = ""
    count = 1

    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            count += 1
        else:
            result += text[i - 1] + str(count)
            count = 1

    # add last letter
    result += text[-1] + str(count)
    return result

choice = input("Enter your choice (1 or 2): ")

if choice == "1":
    pattern = input("Enter pattern: ")
    print("Decoded:", decode(pattern))
elif choice == "2":
    text = input("Enter text: ")
    print("Encoded:", encode(text))
else:
    print(" Invalid choice!")
