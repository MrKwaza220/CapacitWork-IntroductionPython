print('Hello world')
print("Escape Sequences")

print('Hello \n World')
print('Or You can use three single or double qoutes')
print('''This string will
       print on two lines''')

print('''
**** *       * ********* *    *
*  *   *   *
****     *
*
*
''')

# Define the patterns for each letter in the word "PYTHON"
patterns = {
    'P': ["****",
          "*  *",
          "****",
          "*   ",
          "*   "],
    'Y': ["*   *",
          " * * ",
          "  *  ",
          "  *  ",
          "  *  "],
    'T': ["*****",
          "  *  ",
          "  *  ",
          "  *  ",
          "  *  "],
    'H': ["*  *",
          "*  *",
          "****",
          "*  *",
          "*  *"],
    'O': [" *** ",
          "*   *",
          "*   *",
          "*   *",
          " *** "],
    'N': ["*   *",
          "**  *",
          "* * *",
          "*  **",
          "*   *"]
}

 

# Function to display the word horizontally using patterns
def display_word_horizontally(word):
    for i in range(5):
        for letter in word:
            print(patterns[letter][i], end="  ")
        print()

 

# Call the function with the word "PYTHON"
word_to_display = "PYTHON"
display_word_horizontally(word_to_display)



