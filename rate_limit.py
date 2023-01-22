'''
rate limit problem
'''

accepted_ip_addresses = []
accepted_time_stamps = []

def accept_or_reject(time_stamps, ip_addresses, limit, lower_ts_threshold, ip_address, time_stamp):
    '''
    Decision making function
    '''
    count = 0
    for i,j in zip(ip_addresses, time_stamps):
        if j >= lower_ts_threshold and str(i) == str(ip_address):
            count += 1
    if count < limit:
        result = 1
        accepted_ip_addresses.append(ip_address)
        accepted_time_stamps.append(time_stamp)
    else:
        result = 0
    return result

def sol(time_stamps, ip_addresses, limit, time_window):
    '''
    Function that returns soltion
    '''
    sol_arr = []
    for ip_address, time_stamp in zip(ip_addresses, time_stamps):
        lower_ts_threshold = time_stamp - time_window
        result = accept_or_reject(accepted_time_stamps, accepted_ip_addresses, 
                                    limit, lower_ts_threshold,
                                    ip_address, time_stamp)
        sol_arr.append(result)

    print(sol_arr)
    return sol_arr


if __name__ == "__main__" :
    sol([1600040547954, 1600040547957, 1600040547958], ["127.105.232.211", "127.105.232.211", "127.105.232.211"], 1, 3)
    sol([1600000000000, 1600000000000, 1600000000001], ["56.75.0.49", "62.2.159.38", "62.2.159.38"], 2, 10)
