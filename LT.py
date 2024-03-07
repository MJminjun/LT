import openpyxl
import random

file_path = "LT.xlsx"

workbook = openpyxl.load_workbook(file_path)
worksheet = workbook.worksheets[0]

data = []
for row in worksheet.iter_rows(min_row=1):
    data.append([cell.value for cell in row])

print('로딩된 데이터 수(회차) :', len(data))

number_counts = {}
for result in data:
    for number in result:
        number_counts[number] = number_counts.get(number, 0) + 1

sorted_counts = sorted(number_counts.items(), key=lambda x: x[1], reverse=True)

for i, (number, count) in enumerate(sorted_counts):
    if i % 5 == 0:
        print()
    print(f"{number} : {count} 회", end=" | ")
print()

total_count = sum(number_counts.values())
weights = {}
for number, count in number_counts.items():
    weights[number] = count / total_count

# sorted_weights = sorted(weights.items(), key=lambda x: x[1], reverse=True)

# for i, (number, weight) in enumerate(sorted_weights):
#     if i % 5 == 0:
#         print()
#     print(f"{number}: {weight:.5f} %", end=" | ")
# print()

cumulative_weights = {}
last_weight = 0
for number, weight in weights.items():
    cumulative_weights[number] = last_weight + weight
    last_weight += weight
    
# sorted_cumulative_weights = sorted(cumulative_weights.items(), key=lambda x: x[1], reverse=True)

# for i, (number, weight) in enumerate(sorted_cumulative_weights):
#     if i % 5 == 0:
#         print()
#     print(f"{number}: {weight:.5f} %", end=" | ")
# print()

def draw_number():
    random_value = random.random()
    for number, cumulative_weight in cumulative_weights.items():
        if random_value <= cumulative_weight:
            return number
        
def draw_numbers():
    numbers = []
    for _ in range(6):
        numbers.append(draw_number())
    return sorted(numbers)

# numbers = draw_numbers()
# print('\n추첨 번호 :', numbers)

print('\n지난 당첨 번호', len(data), '회차', data[0])

while True:
   print("\n1. 추첨 번호 받기")
   print("2. 종료")
   choice = input("선택하세요: ")

   if choice == "1":
       numbers = draw_numbers()
       print("\n추첨 번호:", numbers)
   elif choice == "2":
       print("\n종료합니다.")
       break
   else:
       print("\n잘못된 입력입니다. 다시 선택하세요.")