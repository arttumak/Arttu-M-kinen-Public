
def arithmetic_arranger(problems,print_solutions = False):
    arranged_problems = str()
    row_1 = str()
    row_2 = str()
    row_3 = str()
    row_4 = str()
    problems_to_solve = len(problems)
    variable_1 = []
    variable_2 = []
    definitor = []
    answer = []
    space = " "
    end_char = space*4

    for problem in problems:
        problem_split = problem.split(" ")
        var_1 = problem_split[0]
        var_2 = problem_split[2]
        defi = problem_split[1]

        if(problems_to_solve > 5):
            return "Error: Too many problems."

        try:
            int(var_1)
            int(var_2)
        except:
            return "Error: Numbers must only contain digits."

        if(len(var_1) > 4 or len(var_2) > 4):
            return "Error: Numbers cannot be more than four digits."

        if (defi != ("-") and defi != ("+")):
            return "Error: Operator must be '+' or '-'."

        variable_1.append(var_1)
        variable_2.append(var_2)
        definitor.append(defi)

    
    for i in range(problems_to_solve):
        if(definitor[i] == "+"):
            solution = int(variable_1[i]) + int(variable_2[i])
        else:
            solution = int(variable_1[i]) - int(variable_2[i])
        answer.append(str(solution))

    for i in range(problems_to_solve):
        max_length = max((len(variable_1[i]) + len(definitor[i]) + 1), ( len(variable_2[i]) + len(definitor[i]) + 1))
        padding = max_length - len(variable_1[i])
        row_1 = (row_1 + str(space*padding + variable_1[i]))
        if(i != problems_to_solve-1):
            row_1 = (row_1 + str(end_char))
    
    for i in range(problems_to_solve):
        max_length = max((len(variable_1[i]) + len(definitor[i]) + 1), ( len(variable_2[i]) + len(definitor[i]) + 1))-1
        padding = max_length - len(variable_2[i])
        row_2 = (row_2 + str(definitor[i] + space*padding + variable_2[i]))
        if(i != problems_to_solve-1):
            row_2 = (row_2 + str(end_char))

    for i in range(problems_to_solve):
        max_length = max((len(variable_1[i]) + len(definitor[i]) + 1), ( len(variable_2[i]) + len(definitor[i]) + 1))
        row_3 = (row_3 + str("-"*max_length))
        if(i != problems_to_solve-1):
            row_3 = (row_3 + str(end_char))

    if(print_solutions == True):
        for i in range(problems_to_solve):
            max_length = max((len(variable_1[i]) + len(definitor[i]) + 1), ( len(variable_2[i]) + len(definitor[i]) + 1))
            padding = max_length - len(answer[i])
            row_4 = (row_4 + str(space*padding + answer[i]))
            if(i != problems_to_solve-1):
                row_4 = (row_4 + str(end_char))
    
    if(print_solutions == True):
        arranged_problems = row_1 + "\n" + row_2 + "\n" + row_3 + "\n" + row_4
    else:
        arranged_problems = row_1 + "\n" + row_2 + "\n" + row_3
    
    return arranged_problems


def main():

    print(arithmetic_arranger(['24 + 852', '3801 - 2', '45 + 43', '123 + 49'],True))

    return None

main()