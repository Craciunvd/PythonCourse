with open('myfile.txt') as myfile:
    file_contents = myfile.readlines()

print(file_contents)
myfile.close()


def spy_game(nums):

    code = [0,0,7,'x']

    for num in nums:
        if num == code[0]:
            code.pop(0)

    return len(code) == 1

print(spy_game([1,2,4,0,7,0,7,5]))