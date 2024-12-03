def safe_report(report):
    if not (report == sorted(report) or report == sorted(report, reverse=True)):
        return 0
    else:  
        for i in range(0, len(report)-1): 
            if not (1 <= abs(report[i+1] - report[i]) <= 3):
                 return 0
        return 1


with open('./day2_problem1_input.txt', "r") as file:

    safe_reports = 0

    for line in file:
        report = []
        for item in line.strip().split():
            report.append(int(item))
        
        safe_reports += safe_report(report)

print(safe_reports)
