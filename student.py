# Say hi to everyone on  the list by their first name eg Hi Michael, Hi Alvin 
students = ["Njoroge,Michael", "Kamau, Alvin" , "Olum,Peter"]
for student in students:
    last_name , first_name = student.split(",")
    print(f"Hi {last_name}")
