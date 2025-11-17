minSkill = 100
skills = []
peoples = int(input("Enter num of people: "))
for i in range(peoples):
     push = int(input(f"Enter person {i+1} skill: "))
     skills.append(push)
for i in range(peoples):
  if skills[i] >= minSkill:
     print("Yes")
  else:
     print("No")