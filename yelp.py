servers = [Server(0), ...]
weights = [4, 3, 2, 1 ...]

def serve():
    for request in requests.stream():
        find_server(request).serve(request)

def find_server(request):
    # generate a random number [0, n) 0, 1, 2, ..., n-1
    random.randint(n)
    0 0 0 0 1 1 1 2 2 3
    # use that number to pick a server
    arr = [[0]*weights[i] for i in range(len(weights))]