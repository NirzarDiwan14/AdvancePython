#Multiprocessing coding challenge-2 
import concurrent.futures
import time 
import random  


SIZE = 500

def multiply_row(row,matrix_b):
    return [
        sum(row[i] * matrix_b[i][j] for i in range(len(row)))
        for j in range(len(matrix_b[0]))
    ]

def multiply_without_multiprocessing(matrix_a,matrix_b):
    result = []
    for row in matrix_a:
        result.append(multiply_row(row,matrix_b))
    return result

def multiply_with_multiprocessing(matrix_a,matrix_b):
    with concurrent.futures.ProcessPoolExecutor() as executer:
        result = list(executer.map(multiply_row,matrix_a,[matrix_b] * len(matrix_a)))
        return result
    
if __name__ == "__main__":

    matrix_a = [[random.random() for _ in range(SIZE)] for _ in range(SIZE)]
    matrix_b = [[random.random() for _ in range(SIZE)] for _ in range(SIZE)]

    start  = time.perf_counter()

    multiply_without_multiprocessing(matrix_a,matrix_b)
    end = time.perf_counter()

    print(f"without multiprocessing task was completed in {end  - start} seconds.")


    start  = time.perf_counter()
    multiply_with_multiprocessing(matrix_a,matrix_b)

    end = time.perf_counter()

    print(f"with multiprocessing task was completed in {end  - start} seconds.")