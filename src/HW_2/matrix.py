from random import randint

m = int(input("Введите размер матрицы: "))
lst = [[randint(1, 50) for _ in range(m)] for _ in range(m)]


def print_matrix(matrix, sum_matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(f'{matrix[i][j]:>5}', end='')
        print()
    print()

    for j in range(len(sum_matrix)):
        print(f'{sum_matrix[j]:>5}', end='')
    print()
    print()


lst_sum = [0] * len(lst[0])
for i in range(len(lst)):
    for j in range(len(lst[i])):
        lst_sum[j] += lst[i][j]


def sort_matrix(matrix, sum_matrix):
    for i in range(len(sum_matrix)-1):
        flag = True
        for j in range(len(sum_matrix)-1-i):
            if sum_matrix[j] > sum_matrix[j + 1]:
                sum_matrix[j], sum_matrix[j + 1] = sum_matrix[j + 1], sum_matrix[j]
                for k in range(len(sum_matrix)):
                    matrix[k][j], matrix[k][j+1] = matrix[k][j+1],  matrix[k][j]
                flag = False
        if flag:
            break

    for k in range(len(matrix)):
        for i in range(len(matrix)-1):
            flag = True
            for j in range(len(matrix)-1-i):
                if matrix[j][k] > matrix[j + 1][k] if k % 2 else matrix[j][k] < matrix[j + 1][k]:
                    matrix[j][k], matrix[j + 1][k] = matrix[j + 1][k],  matrix[j][k]
                    flag = False
            if flag:
                break


print_matrix(lst, lst_sum)
sort_matrix(lst, lst_sum)
print_matrix(lst, lst_sum)

