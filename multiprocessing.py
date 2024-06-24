import multiprocessing


def make_request(url):
    response = requests.get(url)
    print(f"Response from {url}: {response.text}")

def main():
    urls = ['https://www.example.com', 'https://www.example.org', 'https://www.example.net']

    # Create processes
    processes = [multiprocessing.Process(target=make_request, args=(url,)) for url in urls]

    # Start processes
    for process in processes:
        process.start()

    # Wait for all processes to finish
    for process in processes:
        process.join()

    print("Main process continues execution.")

if __name__ == "__main__":
    main()
