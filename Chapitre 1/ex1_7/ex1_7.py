file_name = "Chapitre 1//ex1_7//election.txt"

file = open(file_name, "r", encoding = "utf-8")

n_lists = int(file.readline())

candidate_list = file.readline().split()    # elements are strings!

print ("candidate - list")

for i in range(len(candidate_list)):
    print (f"{i + 1 : 4d} {int(candidate_list[i]):9d}")

votes = [0] * n_lists

print (votes)

total_votes = 0

for line in file :
    for v in line.split():
        votes[int(candidate_list[int(v) - 1]) - 1] += 1
        total_votes += 1

file.close()

print ("Liste :", end = "")

for i in range(n_lists):
    print(f"{i + 1 :7d}", end = "")

print ("\nVoix : ", end = "")

for i in range (n_lists):
    print (f"{votes[i]:7d}", end = "")

print ()

for i in range(n_lists):
    print (f"Liste {i + 1 : 2d} : {votes[i] / total_votes * 100 : 6.2f} %")