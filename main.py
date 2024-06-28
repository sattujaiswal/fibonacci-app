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

@app.get("/fibonacci/{number}")
def get_fibonacci(number: int):
    return {"fibonacci_sequence": fibonacci(number)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)