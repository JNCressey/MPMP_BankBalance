verbose = False # debug prints

def grading(b_N_minus_1):
    b_k_plus_2 = 1000000
    b_k_plus_1 = b_N_minus_1 # The argument to the function.
    b_k = b_k_plus_2 - b_k_plus_1
    if verbose:
        print(f"{(b_k, b_k_plus_1, b_k_plus_2,)}")
    N = 1   # When b_k is verified to be greater than 0, N will be set to 2. 
            # That means that if k was taken to equal 0 then,
            # b_2 would be the 10^6.
    while (b_k > 0):
        N += 1
        # if k is taken to be 0 here, b_N is then the 10^6
        (
            b_k,
            b_k_plus_1,
            b_k_plus_2,
        ) = (
            b_k_plus_1 - b_k,
            b_k,
            b_k_plus_1,
        )
        # the new b_k is b_(k-1) in the old step, so is calculated by
        # b_(k-1) = b_(k+1) - b_k by the previous step's labelling.
        if verbose:
            print(f"{(b_k, b_k_plus_1, b_k_plus_2,)}")
    # b_k is now one step too far back, thus k=-1.
    if verbose:
        print(f"b_0 = {b_k_plus_1}") # this is the second day's deposit
        print(f"b_1 = {b_k_plus_2}") # this is the first day's deposit
    # **Note:** N has not been incremented since the value we have for
    # b_k_plus_1 was in the b_k slot, so N has its correct value
    # relative to b_0 and b_1.
    return N # this is the number of the day 10^6 balance is reached

def test():
    b_N_minus_1 = 618034 # should result in N=19
    print(f"b_N_minus_1 = {b_N_minus_1}")
    N = grading(b_N_minus_1)
    print(f"N = {N}")

if __name__=="__main__":
    test()
