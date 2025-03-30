# Write your code here.

# Task 1: Hello
def hello():
    return "Hello!"
# print(hello())

# Task 2: Greet
def greet(name):
    return f"Hello, {name}!"

# Task 3: Calculator
def calc(num1, num2, operator = "multiply"):
    try:
        if operator == 'add':
            return num1 + num2;
        elif operator == 'subtract':
            return num1 - num2;
        elif operator == 'modulo':
            return  num1 % num2;
        elif operator == 'multiply':
            return num1 * num2;
        elif operator =='divide':
            return num1 / num2;
    except ZeroDivisionError:
        return "You can't divide by 0!"
    except TypeError:
        return f"You can't {operator} those values!"
    except ValueError as e:
        return f"Error is: {e}"
# print(calc(2, "0dfgd", "divide"))
# print(calc("one", "two" 'add'))
# print(calc(12.6, 4.4, "subtract"))

# Task 4: Data Type Conversion
def data_type_conversion(value, data_type):
    try:
        if data_type == "int":
            return int(value)
        elif data_type == "float":
            return float(value)
        elif data_type == "str":
            return str(value)
    except ValueError:
        return f"You can't convert {value} into a {data_type}."
# print(data_type_conversion(1000, "str"))

# Task 5: Grading System, Using *args
def grade(*args):
    try:
        avgPoints = sum(args) / len(args)
    except (ValueError, TypeError):
        return "Invalid data was provided."
    else:
        if avgPoints >= 90:
            return "A"
        elif avgPoints >= 80 and avgPoints < 90:
            return "B"
        elif avgPoints >= 70 and avgPoints < 80:
            return "C"
        elif avgPoints >= 60 and avgPoints < 70:
            return "D"
        elif avgPoints < 60:
            return "F"
# print(grade(85,85,85))

#  Task 6: Use For Loop with a Range
def repeat(str, count):
    newStr = ""
    for x in range(count):
        newStr = newStr + str;
    return newStr;
    # return str * count;
# print(repeat("ku-", 5))

# Task 7: Student Score, Using **kwargs
def student_scores(option, **kwargs):
    if option == "mean":
        return sum(kwargs.values()) / len(kwargs)
    elif option == "best":
        return max(kwargs, key=kwargs.get)
    else:
        return "Invalid option"
    # return "test"
# print(student_scores("mean", Tom=75, Dick=89, Angela=91))

# Task 8:Titleize, with String and List Operations
def titleize(str):
    little_words = ("a", "on", "an", "the", "of", "and", "is", "in")
    words = str.split(" ")
    new_str = [];
    
    for i, word in enumerate(words):
        if i == 0 or i == len(words) - 1:  # Capitalize first and last word
            new_str.append(word.capitalize())
        elif word.lower() not in little_words:  # Capitalize words not in little_words
            new_str.append(word.capitalize())
        else:
            new_str.append(word.lower())  # Keep little words in lowercase

    return " ".join(new_str)
# print(titleize("which part of this crazy world IS in the GAME?"))

# Task 9: Hangman, with more String Operations
def hangman(secret, guess):
    newStr = ""
    for letter in secret:
        if letter in guess:
            newStr = newStr + letter
        else:
            newStr = newStr + "_"
    return newStr;
print(hangman("superstar", "asdf"))

# Task 10: Task 10: Pig Latin, Another String Manipulation Exercise
def pig_latin(str):
    vowels = ("a", "e", "i", "o", "u")
    newArr = str.split(" ")
    result = []
    for word in newArr:
        if word.startswith(vowels):
            result.append(word + "ay")
        else:
            while not word.startswith(vowels):
                if word.startswith('qu'):
                    word = word[2:] + "qu"
                else:
                    word = word[1:] + word[0]
            result.append(word + "ay")
    return " ".join(result)
print(pig_latin("quuiet boy"))