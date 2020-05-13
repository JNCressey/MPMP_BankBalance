verbose = 2 # debug prints

def grading(b_N_minus_1, returnkey="N"):
    # returnkey "N" for N to be returned, "d" for the two deposits to be returned
    b_k_plus_2 = 1000000
    b_k_plus_1 = b_N_minus_1 # The argument to the function.
    b_k = b_k_plus_2 - b_k_plus_1
    N = 2   # We wish to maintain the fact that assuming k=0 implies b_N=10^6.
            # For the starting values here k+2=N; so N=2.
    if verbose>=2:
        print(f"{(N, b_k, b_k_plus_1, b_k_plus_2,)}")
    while (True):
        candidate_new_b_k = b_k_plus_1 - b_k
        if candidate_new_b_k > 0:
            (
                N,
                b_k,
                b_k_plus_1,
                b_k_plus_2,
            ) = (
                N,
                candidate_new_b_k,
                b_k,
                b_k_plus_1,
            )
            if verbose>=2:
                print(f"{(N, b_k, b_k_plus_1, b_k_plus_2,)}")
        else:
            break
    # now b_k is tracked back as far as it can go
    # and assuming k=0 implies N is our number of days
    b_0 = b_k # this is the second day's deposit
    d_2 = b_0
    b_1 = b_k_plus_1 # this is the first day's deposit
    d_1 = b_1
    if verbose>=2:
        print(f"b_0 = {b_0}") # this is the second day's deposit
        print(f"b_1 = {b_1}") # this is the first day's deposit
    if returnkey=="N":
        return N # this is the number of the day 10^6 balance is reached
    elif returnkey=="d":
        return (d_1, d_2) # this is (d_1, d_2)


def test():
    b_N_minus_1 = 618034 # should result in N=19
    print(f"b_N_minus_1 = {b_N_minus_1}")
    N = grading(b_N_minus_1)
    print(f"N = {N}")


def generate_data():
    # create a file with the data series
    # of (b_N_minus_1, N) for 0<b_N_minus_1<10^6.
    import csv
    with open("data.csv",'w', newline='') as data_file:
        csv_out = csv.writer(data_file)
        csv_out.writerow(("b_N_minus_1","N"))
        for b_N_minus_1 in range(1,1000000):
            if verbose>=1:
                if b_N_minus_1 % 100000 == 0:
                    print(b_N_minus_1)
            csv_out.writerow((b_N_minus_1,grading(b_N_minus_1)))

if __name__=="__main__":
    optimal_b_N_minus_1 = 618034
    (d_1,d_2) = grading(optimal_b_N_minus_1,returnkey="d")
    print(f"Maximum days 19 achieved when d_1={d_1}, d_2={d_2}")
