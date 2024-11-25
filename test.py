import requests
import concurrent.futures

def generate_image():
    url = "http://localhost:8080/generate"
    headers = {"Content-Type": "application/json"}
    data = {"prompt": "A futuristic cityscape at sunset"}

    response = requests.post(url, headers=headers, json=data)
    print(f"Response size: {len(response.text)} bytes")
    print(f"Generation time: {response.json().get('generation_time', 'N/A')}")

def generate_images_concurrently(n):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(generate_image) for _ in range(n)]
        concurrent.futures.wait(futures)

# Example usage
if __name__ == "__main__":
    generate_images_concurrently(2)