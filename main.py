grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

# len_grades = len(grades)
# print(len_grades)

# avg_list = [
#     sum(grades[0])/len(grades[0]),
#     sum(grades[1])/len(grades[1]),
#     sum(grades[2])/len(grades[2]),
#     sum(grades[3])/len(grades[3]),
#     sum(grades[4])/len(grades[4]),
# ]

avg_list = []
print(range(len(grades)))

# 0, 1, 2, 3, 4, 5
#    *  *
for i in range(len(grades)):
    avg_list.append(sum(grades[i]) / len(grades[i]))

list = list(students)

sort_list = sorted(list)

grades_and_students = dict(zip(sort_list, avg_list))
print(grades_and_students)


users = [
    {
        "name": "John",
        "age": 18
    },
    {
        "name": "Carl",
        "age": 190
    },
    {
        "name": "Petr",
        "age": 19
    },
    {
        "name": "Sam",
        "age": 12
    },

]


print(users)

# Имя: имя, Возраст: возраст
for user in users:
    print(f'Имя: {user["name"]}.\n'
          f'Возраст: {user["age"]}')



