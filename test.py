# a = 'Hello'
# print(a)
# print(type(a))
# b=123
# print(b)
# print(type(b))
# c='hello$@@$% 123'
# print(c)
# print(type(c))
# a=2.1
# print(a)
# print(type(a))
# a='asdf'
# b=123
# print(a is b)
# print(a==b)
# if(a!=b) :
#     print(f'They are not equal as a value {a} and b value is {b}')
# else :
#     print(f'They are equal as a value {a} and b value is {b}')
# a=5
# b=3
# print(str(a)+str(b))
#
# a='async'
# b='asy'
# print(a+b)

# a='Sudarsan'
# b=a[0:3]
# print(b)
# c=a[::-1]
# print(c)

# a='apple,orange'
# b=a.split(',')
# d=[]
# for i in b:
#     e=(i+'s')
#     print(e)
#     d.append(e)
# print(d[1])

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
#
# newlist = [x for x in range(10)]
#
# print(newlist)

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = []
#
# for x in fruits:
#   if "a" in x:
#     newlist.append(x)
#
# print(newlist)

# a=['Raja', 'Raman', 'Belvina', 'Shyamantha', 'MeenaShree']
# b = [x[::-1] for x in a]
# print(b)

# a=['Raja', 'Raman', 'Belvina', 'Shyamantha', 'MeenaShree']
# b=[x[replace("a", "")] for x in a]
# print(b)
# a = "Hello, World!"
# print(a.replace("H", "J"))



a = ['Raja', 'Raman', 'Belvina', 'Shyamantha', 'MeenaShree','MeenaShree']
# b=[]
# for x in a:
#     if x not in b:
#         b.append(x)
# print(b)
# output = [''.join(set(x)) for x in a]
# if x not in output:
#     output.append(x)
# print(output)


def has_duplicate_characters(word):
    seen = set()
    for char in word:
        if char in seen:
            return True
        seen.add(char)
    return False

a = ['Raja', 'Raman', 'Belvina', 'Shyamantha', 'MeenaShree']

output = [word for word in a if has_duplicate_characters(word)]

print(output)


def find_duplicates(word):
    seen = set()
    duplicates = {}

    for char in word:
        if char in seen:
            if char in duplicates:
                duplicates[char] += 1
            else:
                duplicates[char] = 2  # Counting the first occurrence as 2
        seen.add(char)

    if duplicates:
        duplicate_info = []
        for char, count in duplicates.items():
            duplicate_info.append(f"'{char}'" + (f" ({count} times)" if count > 2 else ""))
        return f"{word} has {len(duplicates)} duplicated element{'s' if len(duplicates) > 1 else ''} which {'are' if len(duplicates) > 1 else 'is'} {', '.join(duplicate_info)}"
    else:
        return f"{word} has no duplicated elements"


a = ['Raja', 'Meena', 'Tmmbbsd']

output = [find_duplicates(word) for word in a]

for result in output:
    print(result)
