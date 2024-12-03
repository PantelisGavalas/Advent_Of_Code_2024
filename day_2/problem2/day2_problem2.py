def safe_report(report):
    if not (report == sorted(report) or report == sorted(report, reverse=True)):
        return False
    else:  
        for i in range(0, len(report)-1): 
            if not (1 <= abs(report[i+1] - report[i]) <= 3):
                 return False
        return True
    

def report_parser(report):
    my_bool = safe_report(report)
    if my_bool:
        return 1
    else:
        #print(report)
        for i in range(0, len(report)):
            updated_report = report[:i] + report[i+1:]
            #print(i, updated_report)
            my_bool = safe_report(updated_report)
            if my_bool:
                return 1
        return 0


with open('./day2_problem2_input.txt', "r") as file:

    safe_reports = 0

    for line in file:
        report = []
        for item in line.strip().split():
            report.append(int(item))
        
        safe_reports += report_parser(report)

print(safe_reports)
