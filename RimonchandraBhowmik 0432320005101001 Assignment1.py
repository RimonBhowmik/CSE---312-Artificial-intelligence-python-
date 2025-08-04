def analyze_name(full_name):
    name = full_name.replace(" ", "").lower()  # remove spaces and lowercase
    vowels = 'aeiou'
    vowel_count = sum(1 for char in name if char in vowels)
    consonant_count = sum(1 for char in name if char.isalpha() and char not in vowels)

    print(f"Vowels: {vowel_count}, Consonants: {consonant_count}\n")

    print("ASCII values:")
    for char in full_name:
        print(f"  {char}: {ord(char)}")
    print()

    reversed_name = full_name[::-1]
    print(f"Reversed name: {reversed_name}\n")

    is_palindrome = full_name.lower().replace(" ", "") == reversed_name.lower().replace(" ", "")
    print(f"Is palindrome: {'Yes' if is_palindrome else 'No'}\n")

    unique_letters = sorted(set(name))
    print(f"Unique sorted letters: {unique_letters}\n")

    # Bonus: First non-repeating character
    for char in name:
        if name.count(char) == 1:
            print(f"First non-repeating character: {char}")
            break
    else:
        print("No non-repeating character found.")

# Example usage
analyze_name("Rimon Chandra Bhowmik")
