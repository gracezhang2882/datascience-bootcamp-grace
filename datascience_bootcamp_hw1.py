#1 Display Fibonacci Series upto 10 terms
def fib(n):
    fib_series = [0, 1]
    for i in range(n - 2):
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series
print(fib(10))

#2 Display numbers at the odd indices of a list
lst_1 = [0,1,2,3,4,5,6,7,8,9,10]
print([lst_1[i] for i in range (1, len(lst_1), 2)])

#3 Count the number of different words in this text
string = """
I have provided this text to provide tips on creating interesting paragraphs.
First, start with a clear topic sentence that introduces the main idea.
Then, support the topic sentence with specific details, examples, and evidence.
Vary the sentence length and structure to keep the reader engaged.
Finally, end with a strong concluding sentence that summarizes the main points.
Remember, practice makes perfect!
"""
string = string.lower().replace(".", " ").replace(",", " ").replace("!", " ")
words = string.split()
unique_words = []
for word in words:
    if word not in unique_words:
        unique_words.append(word)
print(len(unique_words))

#4 Write a function count_vowels(word) that takes a word as an argument and returns the number of vowels in the word
def count_vowels(word):
    vowels = "AEIOUaeiou"
    count = 0  
    for char in word:
        if char in vowels:
            count += 1
    return count

#5 ⁠Iterate through the following list of animals and print each one in all caps
animals=['tiger', 'elephant', 'monkey', 'zebra', 'panther']
print([i.upper() for i in animals])

#6 Write a program that iterates from 1 to 20, printing each number and whether it's odd or even.
for i in range(1, 21):  
    if i % 2 == 0:
        print(i, "even")
    else:
        print(i, "odd")

#7 Write a function sum_of_integers(a, b) that takes two integers as input from the user and returns their sum
int1 = int(input("Enter the first integer: "))
int2 = int(input("Enter the second integer: "))
print("Sum: ", int1+int2)