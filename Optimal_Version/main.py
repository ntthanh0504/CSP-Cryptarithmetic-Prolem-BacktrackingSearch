from cryptarithmetic_problem import CryptarithmeticProblem
from utils import *
import time

if __name__ == "__main__":
    # file_path = str(get_command_line_arguments()[1])
    # folder, file = file_path.split('/')
    # name, tail = file.split('.')
    # _, index = name.split('_')
    # equation = read_file(f'{file_path}')
    for lv in range(1,4):
        for idx in range(1,6):
            equation = read_file(f'Cryptarithmetic-Problem\Level_{lv}\input_{idx}.txt')
            problem = CryptarithmeticProblem(equation)
            print(f'Cryptarithmetic-Problem\Level_{lv}\input_{idx}.txt')
            print(equation)

            start_time = time.time()
            solution = problem.backtracking_search()
            end_time = time.time()
            execution_time = end_time - start_time
            print("Execution Time:", execution_time, "seconds")

            write_file(f'Cryptarithmetic-Problem\Level_{lv}\input_{idx}.txt', solution)
            if solution:
                vars = sorted(solution.keys())
                for var in vars:
                    print(f'{var}: {solution[var]}', end=' | ')
                print('\n')
            else:
                print("NO SOLUTION\n")
