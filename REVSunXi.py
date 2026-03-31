'''
#Name: [Sun Xi]
#Date: March 16, 2026
#Module: 03REV – Review Python Fundamentals
#Description: This program is a tool that helps users find out how many vowels are in a specific sentence or word. 
First, it asks the user to type in some text, and then it goes through that text character by character to find A, E, I, O, and U. 
I used a dictionary to keep track of the count for each specific vowel and a running total variable for the overall count. 
To follow the assignment rules, I made sure not to use built-in functions like sum() or count(), relying on loops and if-statements instead. 
Finally, the program prints out a neat report that shows the breakdown of each vowel and the grand total at the bottom.
'''

# CONSTANTS
TITLE = "Welcome to vowel counter program!"
PROMPT = "Enter any text: "
LINE = '-'
REPORT_LIST = ["VOWEL COUNT REPORT:", "Vowel", "Count", "Total"]

def main():
    """
    This is the starting point of the script. It prints the welcome 
    header, gets the string from the user, and then calls the other 
    two functions to do the math and show the report.
    """
    print(TITLE)
    print(LINE * len(TITLE))
    
    # Prompt the user for input and convert to upper case for easier matching
    text = input(PROMPT).upper()
    
    # Call findVowelCount and capture the returned dictionary and total
    vDict, total = findVowelCount(text)
    
    # Call generateReport to display the final results
    generateReport(vDict, total)

def findVowelCount(text):
    """
    This function does the heavy lifting. It loops through the user's 
    text and checks if each letter is a vowel. If it finds one, it 
    updates the dictionary and adds 1 to the total counter.
    """
    vDict = {'A': 0, 'E': 0, 'I': 0, 'O': 0, 'U': 0}
    total = 0
    
    # Traverse each character in the text entered using for loop
    for char in text:
        # If the character is a key in our vowel dictionary
        if char in vDict:
            # Increment corresponding vDict value to keep track of the count
            vDict[char] += 1
            # Increment total to keep track of the total vowel count
            total += 1
            
    return vDict, total

def generateReport(vDict, total):
    """
    This function just handles the printing. It takes the dictionary 
    and the total number we calculated and formats them into the 
    table layout requested in the lab instructions.
    """
    print("\n" + REPORT_LIST[0])
    print(LINE * len(REPORT_LIST[0]))
    print(f"{REPORT_LIST[1]:<10} {REPORT_LIST[2]:<10}")
    print(LINE * 20)
    
    # Loop through the dictionary to print each vowel and its count
    for vowel in vDict:
        print(f"{vowel:<10} {vDict[vowel]:<10}")
        
    print(LINE * 20)
    print(f"{REPORT_LIST[3]:<10} {total:<10}")

# Call the main function to start the program
if __name__ == "__main__":
    main()