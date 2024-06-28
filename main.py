from fastapi import FastAPI

app = FastAPI()

def fibonacci(n: int) -> int:
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

@app.get("/fibonacci/{number}")
def read_fibonacci(number: int):
    return {"Fibonacci number": fibonacci(number)}