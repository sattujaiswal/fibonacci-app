from fastapi import FastAPI

app = FastAPI()

def fibonacci(n):
    """Return the Fibonacci sequence up to n."""
    a, b = 0, 1
    result = []
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result

def is_prime(number):
    """Check if a number is prime."""
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True

@app.get("/fibonacci/{number}")
def get_fibonacci(number: int):
    return {"fibonacci_sequence": fibonacci(number)}

@app.get("/prime/{number}")
def check_prime(number: int):
    if is_prime(number):
        return {"message": f"{number} is prime."}
    else:
        return {"message": f"{number} is not prime."}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)