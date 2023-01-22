# rate-limit-problem
Your task is to implement a Rate Limiter. Given a list of timestamped queries, you will need to accept or decline each of them, depending on the number of requests from the same IP during a given window of time.

The queries are represented by the two arrays timestamps and ipAddresses:

timestamps is an array of integers representing the Unix timestamps of the requests. timestamps[i] represents the timestamp for the ith request, in milliseconds. It is guaranteed that all requests are in chronological order, i.e. the timestamps array is sorted in non-decreasing order. It is guaranteed that no two requests from the same IP address have the same timestamp.
ipAddresses is an array of strings representing source IP addresses - ipAddresses[i] corresponds to the IP address of the ith request.
You are also given two integers limit and timeWindow:

limit represents the maximum number of requests that can be accepted from the same IP address, within the time window.
timeWindow represents the duration of the inclusive time window, in milliseconds.
Your task is to return an array of integers where the ith element of the array corresponds to the ith request. Each element of the array you return should equal to 1 if the ith request has been accepted, and 0 if the request has been declined.

Focus first on getting a basic solution working to handle fewer than 1000 requests and window sizes smaller than 40, and confirm this is working with test cases 1-9. Then, optimize your solution to handle the following efficiently to past test cases 10-20.

High load - handing up to 105 queries
Large window size - handling window size of up to 109 milliseconds
Note: even though you are given all the requests at once, assume they come serially. That is, you don't know anything about the next request when answering the ith request - that's how a rate limiter is supposed to work in real life.

# Example

For timestamps = [1600040547954, 1600040547957, 1600040547958], ipAddresses = ["127.105.232.211", "127.105.232.211", "127.105.232.211], limit = 1, and timeWindow = 3, the output should be solution(timestamps, ipAddresses, limit, timeWindow) = [1, 0, 1].

Let's consider all the requests one by one:

The first request has arrived at timestamp 1600040547954 from IP address "127.105.232.211", and since there are no accepted requests from the same IP address during the last timeWindow = 3ms, the first request is accepted.
The second request has arrived at timestamp 1600040547957 from IP address "127.105.232.211", and since there is already one accepted request from the same IP address during the last timeWindow = 3ms and limit = 1, the second request is declined.
The third request has arrived at timestamp 1600040547958 from IP address "127.105.232.211", and since there are no other accepted requests from the same IP address during the last timeWindow = 3ms, the third request is accepted. Note that since the second request has been declined, it isn't counted here.


For timestamps = [1600000000000, 1600000000000, 1600000000001], ipAddresses = ["56.75.0.49", "62.2.159.38", "62.2.159.38"], limit = 2, and timeWindow = 10, the output should be solution(timestamps, ipAddresses, limit, timeWindow) = [1, 1, 1].

There were no more than two requests from each IP address which fits into the limit = 2. Thus, all requests should be accepted.

# Input/Output

[execution time limit] 4 seconds (py3)

[input] array.integer64 timestamps

An array of Unix timestamps for each of the requests, in milliseconds. It is guaranteed that the array is non-decreasing and no two requests from the same IP address have the same timestamp.

Guaranteed constraints:
1 ≤ timestamps.length ≤ 105,
16 · 1011 ≤ timestamps[i] ≤ 16 · 1011 + 109.

[input] array.string ipAddresses

An array of IP addresses for each of the requests. It is guaranteed that all given IPs are valid, i.e. they are in the range ["0.0.0.0", "255.255.255.255"].

Guaranteed constraints:
ipAddresses.length = timestamps.length,
7 ≤ ipAddresses[i].length ≤ 15.

[input] integer limit

The maximal amount of requests from the same IP address within every timeWindow milliseconds.

Guaranteed constraints:
1 ≤ limit ≤ timestamps.length.

[input] integer timeWindow

The window size, in milliseconds.

Guaranteed constraints:
1 ≤ timeWindow ≤ 109.

[output] array.integer

An array of 0s and 1s representing whether the request has been accepted or declined.

[Python 3] Syntax Tips

# Prints help message to the console
# Returns a string
def helloWorld(name):
    print("This prints to the console when you Run Tests")
    return "Hello, " + name