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
