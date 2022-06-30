import unittest

# Question 3 Palindrome question
# madam

def palindrome(str):
    array = []
    for i in str:
        array.append(i)
    reversed_array = list(reversed(array))
    str2 = "".join(reversed_array)
    if str == str2:
        return True
    else:
        return False

#print(palindrome("madam"))

# 4 Write tests for the newly created Palindrome function. Provide a
# brief explanation for your test case options.

class MyTestCase(unittest.TestCase):
    def test_palindrome_true(self):
        self.assertTrue(palindrome("madam"))

    def test_palindrome_false(self):
        self.assertFalse(palindrome("madman"))

# Explanation:
# in the test_palindrome_true case, I am testing with a real palindrome string and I expect my function to return True
# while in the test_palindrome_false case, I am testing with a non-palindrome string and I expect my function
# return  False.

# 9. TWO NUMBER SUM:
def two_sum(array, target):
    result = []
    while len(array) != 0:
        cursor = array[0]
        for num in array:
            if num == array[-1]:
                break
            next_index = (array.index(num) + 1)
            a_sum = cursor + array[next_index]
            if a_sum == target:
                result.append(cursor)
                result.append(array[next_index])
        array.pop(0)

    return result
