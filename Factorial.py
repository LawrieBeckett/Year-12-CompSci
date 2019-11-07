
def calc_recur(n):
  if n == 1:
      return 1
  else:
      return n* calc_recur(n - 1)


j = int(input())
print(calc_recur(j))


def addNums(numbers):
    if len(numbers) == 1:
        return numbers[0]
    else:
        return numbers[0] + addNums(numbers[1:])
# endif
# endfunction

mark
