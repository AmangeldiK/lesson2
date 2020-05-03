"""
@Makers
Write a function biggest_guy that takes in three numbers as input and returns the biggest one.
Ex: biggest_guy(10, 30, 20) # --> 30
BONUS CHALLENGE: Write a 1 line solution (Medium Difficulty)
"""
def biggest_guy(one, two, three):
    return max(one, two, three)#write your code here ...
#DO NOT remove lines below here, this is designed to test your code.
def test_biggest_guy():
    try:
        assert biggest_guy(1, 3, 2) == 3
        assert biggest_guy(30, 10, 20) == 30
        assert biggest_guy(20, 10, 30) == 30
        assert biggest_guy(2, 1, 9) == 9
        assert biggest_guy('a', 'a', 'b') == 'b' # 'b' is greater than 'a'
    except (AssertionError) as e:
        print(e)
        print("WRONG!!")
        return
    print("SUCCESS!!!")
#test your code by un-commenting the line(s) below
test_biggest_guy()


"""
@Makers
Write a function string_length that takes in a string and returns its length.
HINT:
Question: What do you mean by length?
Answer: The character count of a string.
Ex: string_length('hello!') # --> 6
Explanation: calling string_length() function on the string 'hello!'
should give me back 6.
"""
def string_length(word):
    return len(word)#write your code here...
#DO NOT remove lines below here, this is designed to test your code.
def test_string_length():
    assert string_length('hello!') == 6
    assert string_length('banana') == 6
    assert string_length('8') == 1
    assert string_length('funnyguys') == 9
    assert string_length('101') == 3
    print("YOUR CODE IS CORRECT!")
#test your code by un-commenting the line(s) below
test_string_length()

"""
@Makers
Write a function bigger_guy that takes in wo numbers and returns the bigger one.
Ex: bigger_guy(10, 20) # --> 20
"""
def bigger_guy(one, two):
    return max(one, two) #write your code here ...
#DO NOT remove lines below here, this is designed to test your code.
def test_bigger_guy():
    assert bigger_guy(1, 2) == 2
    assert bigger_guy(10, 20) == 20
    assert bigger_guy(20, 10) == 20
    assert bigger_guy(10, 10) == 10
    assert bigger_guy(2, 1) == 2
    assert bigger_guy('a', 'b') == 'b' # 'b' is greater than 'a'
    print("YOUR CODE IS CORRECT!")
#test your code by un-commenting the line(s) below
test_bigger_guy()