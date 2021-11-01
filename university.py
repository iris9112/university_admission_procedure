departments = {"Biotech": [], "Chemistry": [], "Engineering": [], "Mathematics": [], "Physics": []}
exams = {"Biotech": [2, 3], "Chemistry": [3], "Engineering": [4, 5], "Mathematics": [4], "Physics": [2, 4]}


def get_score(app, dep):
    scores = [float(app[i]) for i in exams[dep]]
    return max(sum(scores) / len(scores), int(app[6]))


def order(dep):
    return lambda x: (-get_score(x, dep), f"{x[0]} {x[1]}")


def get_admission_list(max_accepted):
    with open("applicants.txt") as file:
        applications = [line.split() for line in file.readlines()]
    for priority in range(7, 10):
        for department in departments.keys():
            sorted_applications = sorted([a for a in applications if a[priority] == department], key=order(department))
            departments[department].extend(
                sorted_applications[0:min(max_accepted - len(departments[department]), len(sorted_applications))]
            )
            applications = [a for a in applications if a not in departments[department]]
    for department in departments.keys():
        with open(f"{department}.txt", "w") as department_file:
            for application in sorted(departments[department], key=order(department)):
                department_file.write(f"{application[0]} {application[1]} {get_score(application, department)}\n")


if __name__ == '__main__':
    get_admission_list(max_accepted=int(input()))
