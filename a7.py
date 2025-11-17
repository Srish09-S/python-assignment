total_amount = int(input("Enter the total amount: "))
remaining_amount = total_amount
notes_100 = remaining_amount // 100
remaining_amount %= 100
notes_50 = remaining_amount // 50
remaining_amount %= 50
notes_20 = remaining_amount // 20
remaining_amount %= 20
notes_10 = remaining_amount // 10
remaining_amount %= 10
notes_5 = remaining_amount // 5
remaining_amount %= 5
notes_2 = remaining_amount // 2
remaining_amount %= 2
notes_1 = remaining_amount // 1
remaining_amount %= 1
print(f"100 rupees note: {notes_100}")
print(f"50 rupees note: {notes_50}")
print(f"20 rupees note: {notes_20}")
print(f"10 rupees note: {notes_10}")
print(f"5 rupees note: {notes_5}")
print(f"2 rupees note: {notes_2}")
print(f"1 rupee note: {notes_1}")