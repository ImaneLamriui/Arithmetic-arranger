
def arithmetic_arranger(problems, show_answers=False):
  if not problems:
    return ""
  max_length = max(len(problem) for problem in problems)
  formatted_problems = []
  for problem in problems:
    if show_answers:
      operands = problem.split()
      answer = str(eval(problem))
      formatted_problem = f"{operands[0].rjust(max_length)}\n{operands[1].rjust(max_length)}\n{'-' * max_length}\n{answer.rjust(max_length)}"
    else:
            formatted_problem = problem
            

    
    formatted_problems.append(formatted_problem)
  return "\n\n".join(formatted_problems)



  

