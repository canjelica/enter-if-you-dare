"""Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.

It should remove all values from list a, which are present in list b.

array_diff([1,2],[1]) == [2]
If a value is present in b, all of its occurrences must be removed from the other:

array_diff([1,2,2,2,3],[2]) == [1,3]

----------------------------------------TEST CASES---------------------------------------
Test.describe("Basic Tests")
Test.assert_equals(array_diff([1,2], [1]), [2], "a was [1,2], b was [1], expected [2]")
Test.assert_equals(array_diff([1,2,2], [1]), [2,2], "a was [1,2,2], b was [1], expected [2,2]")
Test.assert_equals(array_diff([1,2,2], [2]), [1], "a was [1,2,2], b was [2], expected [1]")
Test.assert_equals(array_diff([1,2,2], []), [1,2,2], "a was [1,2,2], b was [], expected [1,2,2]")
Test.assert_equals(array_diff([], [1,2]), [], "a was [], b was [1,2], expected []")

"""


def array_diff(a, b):
    if not b:
        return a
    else:
        difference = []
        for item in a:
            for num in b:
                if num != item:
                    difference.append(item)
        return difference
        