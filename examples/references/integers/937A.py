import cotegen
from typing import List

# http://codeforces.com/problemset/problem/937/A


class CF937A(cotegen.Task):
    input_parameters = \
        {
            'a': cotegen.types.IntegerSequence(1, 100, 0, 600)
        }

    output_type = int

    constraints = [
        cotegen.constraints.CustomConstraint(lambda test: any(x > 0 for x in test['a']))
    ]

    def solve(a: List[int]) -> int:
        ans = 0
        n = len(a)
        for i in range(n):
            good = (a[i] > 0)
            for j in range(i):
                if a[i] == a[j]:
                    good = False
            if good:
                ans += 1
        return ans

    def compare(user_answer: int, jury_answer: int) -> bool:
        return user_answer == jury_answer


if __name__ == '__main__':
    tests = CF937A.generate_random_tests()
    print(len(tests))
    for test in tests:
        print(test)