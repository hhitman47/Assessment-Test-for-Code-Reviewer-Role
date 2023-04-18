""" Section C Code Challenge ( Option 1 Say the Number )

Follow these instructions to construct, examine, and execute the solution:

1: Initiate a terminal or command prompt.
2: Go to the folder where the script file is located.
3: Type in the command python3 say_number.py (or python say_number.py on Windows) to execute the script.
4: The test results and any errors or failures should be shown in the output.

The space complexity of this solution is O(1), which implies that the lists of words and variables
utilized in the algorithm use a fixed amount of memory, regardless of the input size. However, 
the time complexity is O(log_1000 n), where n is the input number, since the algorithm performs a 
constant amount of work for each group of three digits in the number. This indicates that the
execution time of the algorithm grows logarithmically with the size of the input number.
 """

def sayNumber(num):
    # define lists of words for each digit
    ones = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    tens = ['', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    teens = ['','eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    # define lists of words for each place value
    thousands = ['', 'thousand', 'million', 'billion', 'trillion']
    # initialize result string
    result = ''
    # handle zero case
    if num == 0:
        return 'Zero.'
    # iterate over each place value, starting from the highest
    i = 0
    while num > 0:
        # extract the last three digits
        digits = num % 1000
        num = num // 1000
        # convert the three digits to words
        words = ''
        if digits >= 100:
            words += ones[digits // 100] + ' hundred'
            digits %= 100
            if digits > 0:
                words += ' and '
        if digits >= 11 and digits <= 19:
            words += teens[digits - 10]
            digits = 0
        elif digits == 10 or digits >= 20:
            words += tens[digits // 10]
            digits %= 10
            if digits > 0:
                words += ' '
        if digits >= 1 and digits <= 9:
            words += ones[digits]
        # add the place value to the words
        if words != '':
            if i > 0:
                result = words + ' ' + thousands[i] + ', ' + result
            else:
                result = words + ' ' + result
        i += 1
    # add final punctuation
    print (result.capitalize() + '.')
    return result.capitalize() + '.'

# Test suite
assert sayNumber(0) 
assert sayNumber(11) 
assert sayNumber(1043283)
assert sayNumber(90376000010012) 
assert sayNumber(999999999999999)

print("All tests passed.")
