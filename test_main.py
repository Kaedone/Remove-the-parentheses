import codewars_test as test
from solution import remove_parentheses
from random import choice, randint
from re import sub

def correct(s):
    while '(' in s:
        s = sub('\([^()]*\)', '', s)
    return s

@test.describe("remove parentheses")
def tests():
    @test.describe("basic tests")
    def basic():
        test.assert_equals(remove_parentheses("example(unwanted thing)example"), "exampleexample")
        test.assert_equals(remove_parentheses("example (unwanted thing) example"), "example  example")
        test.assert_equals(remove_parentheses("a (bc d)e"), "a e")
        test.assert_equals(remove_parentheses("a(b(c))"), "a")
        test.assert_equals(remove_parentheses("hello example (words(more words) here) something"), "hello example  something")
        test.assert_equals(remove_parentheses("(first group) (second group) (third group)"), "  ")
    @test.describe("random tests")
    def random():
        for loop in range(100):
            chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ   '
            inp_str = ''.join(choice(chars) for char in range(randint(1, 500)))
            par_num = randint(1, 25)
            for par in range(par_num):
                rand_ind = randint(0, len(inp_str) - 1)
                inp_str = inp_str[:rand_ind] + f"({''.join(choice(chars) for char in range(randint(0, 25)))})" + inp_str[rand_ind:]
            test.assert_equals(remove_parentheses(inp_str[:]), correct(inp_str[:]))
