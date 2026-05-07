

try:
    save = []
    with open("../abc/abcd", "r", encoding="UTF-8") as file:
        for i in file:
            a = i.strip().split(',')
            b = a[0].strip()
            c = a[1].strip()

            p = {'studentid':b, 'name':c, 'gender': a[2].strip()}
            save.append(p)
except:
    print("asakjdadada")

for po in save:
    print(po)


delete_id = []
found = False
student = int(input("studentid: "))

for deleteid in save:
    print(deleteid)
    if deleteid['studentid'].strip() == student :
        found = True
        print(f'{student} have remove')
    else:
        delete_id.append(deleteid)


print(delete_id)
with open("../abc/abcd", "w", encoding="UTF-8")  as rr:
    for am in delete_id:
        rr.write(f"{student['studentid']}, {student['name']},{student['gender']}")



# try:
#     with open ("./abc/abcd.txt", "r") as file:
#         for a in file:
#             i = a.split(',')
#             print(i)
#
# except:
#     print("qewqw")

# with open("../abc/abcd","r")as file:
#     a=file.readlines()
#     # for line in file:
#     print(a)
