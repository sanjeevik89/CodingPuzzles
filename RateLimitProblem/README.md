# rate-limit-problem
Your task is to implement a Rate Limiter. Given a list of timestamped queries, you will need to accept or decline each of them, depending on the number of requests from the same IP during a given window of time.

Your task is to return an array of integers where the ith element of the array corresponds to the ith request. Each element of the array you return should equal to 1 if the ith request has been accepted, and 0 if the request has been declined.
