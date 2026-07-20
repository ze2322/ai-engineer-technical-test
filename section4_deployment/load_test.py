import concurrent.futures
import time
import requests

URL = "http://127.0.0.1:8000/generate"

payload = {
    "prompt": "Explain Artificial Intelligence."
}


def send():

    start = time.time()

    requests.post(URL, json=payload)

    return time.time() - start


with concurrent.futures.ThreadPoolExecutor(
    max_workers=10
) as executor:

    futures = [
        executor.submit(send)
        for _ in range(10)
    ]

times = [
    future.result()
    for future in futures
]

print(f"Average latency: {sum(times)/len(times):.2f}s")