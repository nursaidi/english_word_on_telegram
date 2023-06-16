# nums = [3,2,4]
# target = 6
#
# result = []
#
# # for x in range(len(nums)):
# #     for y in range(x, len(nums)):
# #         if nums[x] + nums[y] == target:
# #             result.append(x)
# #             result.append(y)
# # print(result)
#
# for x in range(len(nums)):
#     for y in range(x + 1, len(nums)):
#         if nums[x] + nums[y] == target:
#             print(f'{nums[x]} + {nums[y]} = {target}')

# numbers = [2, 4, 5, 6]
#
# for index, number in enumerate(numbers):
# #     print(f'{index} : {number}')
#
# s = "MCMXCIV"
#
# dict_of_numbers = {
#     'I': 1,
#     'V': 5,
#     'X': 10,
#     'L': 50,
#     'C': 100,
#     'D': 500,
#     'M': 1000,
# }
# result = 0
# count = len(s) - 1
# for index, number in enumerate(s):
#     if count > 1:
#         next_number = s[index + 1]
#         count -= 1
#     else:
#         next_number = s[index]
#
#     if dict_of_numbers[number] < dict_of_numbers[next_number]:
#         result += dict_of_numbers[next_number] - dict_of_numbers[number]
#     else:
#         result += dict_of_numbers[number]





strs = ["flower","flow","flight"]
result = ""
count_of_attempt = len(strs) - 1
# for x in range(len(strs)):
#     for y in range(x + 1, len(strs)):
#         print(y)
#     print(x, 'end')

# for first_index in range(len(strs)):
#     for first_letter in strs[first_index]:
#         count = 0
#         for second_index in range(first_index +1, len(strs)):
#             for second_letter in strs[second_index]:
#                 if first_letter == second_letter:
#                     count += 1
#                     break
#         if count_of_attempt == count:
#             result += first_letter
#         else:
#             break
#
# print(result)


# prefix = strs[0]
# for i in range(1, len(strs)):
#     while strs[i].find(prefix) != 0:
#         prefix = prefix[:-1]
#
# print(prefix)

s = "()"

# dict_of_brackets = {
#     '(': ')',
#     '[': ']',
#     '{': '}'
# }
#
# result = False
#
# for second_bracket_index in range(1, len(s), 2):
#     first_bracket_index = second_bracket_index - 1
#
#     if dict_of_brackets[s[first_bracket_index]] == s[second_bracket_index]:
#         result = True
#     else:
#         print(second_bracket_index)
#
# print(result)
#
# example = [0,0,1,1,1,2,2,3,3,4]
#
# def removeDuplicates(nums):
#
#     list_of_dubbles = []
#     list_without_dubbles = []
#
#     for x in nums:
#         if x not in list_without_dubbles:
#             list_without_dubbles.append(x)
#         else:
#             list_of_dubbles.append(x)
#
#     result = list(len(list_of_dubbles) * "_")
#     result = list_without_dubbles + result
#
#     print(f'{len(list_without_dubbles)}, nums = {result}')
#
# removeDuplicates(example)


params = [
    [1, 2, 3],
    '1234',
    1234
]
data = zip(params)
print(data)