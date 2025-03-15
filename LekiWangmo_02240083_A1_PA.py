import requests

#Function to display the menu
def menu():
    print("Menu:")
    print("1. Prime number sum")
    print("2. Length Unit Converter")
    print("3. Consonants Counter")
    print("4. Min Max Finder")
    print("5. Palindrome Checker")
    print("6. Word Counter")
    print("7. Exit")
    choice = int(input("Enter your choice : "))
    return choice #returns the choice to the main function

choice = menu()

#Prime number sum (To find the sum of prime numbers)
def prime_number_sum_calculator():
    start = int(input("Enter the starting number: "))
    end = int(input("Enter the ending number: "))
    sum = 0

    for num in range(start, end+1):
        if num > 1:
            for i in range(2, num):                      
                if num % i == 0:#num % i gives the remainder when num is divided by i, used to check divisibility
                    break
            else:
                sum += num
    print("Sum of prime numbers is: ", sum)
    return sum

#Length unit converter (To convert length units)
def length_unit_converter():
    length = float(input("Enter the length: "))
    direction = input("Enter the length (M for meters to feet, F for feet to meters): ")
    if direction == "M":
        x = length * 3.281  #1 meter = 3.281 feet
        y = round(x, 2)
        print("The length in feet is: ", y)
    elif direction == "F":
        x = length / 3.281 #1 feet = 0.3048 meters
        y = round(x, 2)
        print("The length in meters is: ", y)
    else:
        print("Invalid choice.")

#Consonant counter (To count the number of consonants in a given text)
def consonant_counter():
    string = input("Enter a string: ")
    count = 0
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    for i in string:
        if i in consonants:
            count += 1  #count is incremented by 1 if the character is a consonant
    print("The number of consonants in the text is: ", count)
    return count

#Min Max Finder (To find the minimum and maximum numbers in a list)
def min_max_finder():
    numbers = input("Enter the numbers separated by comas: ").split(',') #split() divides the string into a list
    numbers = [int(num.strip()) for num in numbers] #strip() removes spaces or characters from the beginning or end of a string
    print("The smallest number is: ", min(numbers))                                 
    print("The largest number is: ", max(numbers))

#Palindrome checker (To check if a given text is a palindrome)
def palindrome_checker():
    text = input("Enter a text: ")
    if text == text[::-1]: #text[::-1] reverses the text
        print("The text is a palindrome.")
    else:
        print("The text is not a palindrome.")

#Word counter (To count the number of words in a given text)
def word_counter():
    """Counts occurrences ['the', 'was', 'and'] in a text file."""
    url = input("Enter the URL of the text file: ")
    try:
        text = requests.get(url).text.lower()
        words = ["the", "was", "and"]
        counts = {word: text.count(word) for word in words}
        print(f"Word counts: {counts}")
    except requests.exceptions.RequestException:
         print("Error fetching the file. ")

def Exit():
    print("Goodbye! ThankYou")
    return

while True: #a while loop to keep the program running until the user chooses to exit
    if choice == 1:
        prime_number_sum_calculator()
    elif choice == 2:
        length_unit_converter()
    elif choice == 3:
        consonant_counter()
    elif choice == 4:   
        min_max_finder()
    elif choice == 5:
        palindrome_checker()
    elif choice == 6:
        word_counter()
    elif choice == 7:
        Exit()
        break
    else:
        print("Invalid choice. Please try again with valid choice")
    x = input("Do you want to attempt a different operation? (yes/no): ")
    if x.lower() == "yes":
        choice = menu()
    else:
        Exit() #exits a loop
        break
