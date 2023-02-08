# 백준 5597번

students = [i for i in range(1,31)]     # 1부터 30까지 학생 추가

for _ in range(28):
    applied = int(input())
    students.remove(applied)    # students에서 applied한 학생들 삭제

print(min(students))
print(max(students))