# Introduction

This is my solution to one of Matt Parker's Maths Puzzles.
See the video on YouTube for the puzzle: [MPMP: The 1 Million Bank Balance puzzle](https://www.youtube.com/watch?v=ILrqPpLpwpE)

Files I mention creating in this writeup can be found in [the GitHub repository for this project.](https://github.com/JNCressey/MPMP_BankBalance)

# Solution


## Solution outline

This solution will work backwards from the condition that, on some day, the balance should equal `1 million (10^6)`. I will exhaust all the possible cases, and select the one with the greatest score (number of days from the two deposits when `10^6` is reached.)


## Evolution of the sequence

The sequence evolves like the Fibonacci sequence: `b_k = b_(k-1) + b_(k-2)`. ('b' for 'balance') (**1**)


## Initial conditions of the sequence

Let `b_1` be the first balance, and `b_2` be the second balance. 

Let `d_1` be the first deposit, and `d_2` be the second deposit.

In the question description, `b_2 = b_1 + d_2`. (**2**) 

By (**1**), `b_2 = b_1 + b_0`. (**3**)

By (**2**) and (**3**), we can pretend there is a balance zero, `b_0 = d_2`. (**4**)

Thus the initial conditions can be thought of as `b_0=d_2; b_1=d_1`.


## Working backwards

For a solution to be valid (and not 'trivial' as said in the video), we need `b_N = 10^6` for some integer `N > 3`. (**5**)

We can rearrange (**1**) as `b_(k-2) = b_k - b_(k-1)`, or equivalently `b_k = b_(k+2)-b_(k+1)` (**6**)

The evolution step needs two knowns, so we can take an arbitrary `b_(N-1)` and that will define a definite sequence going back in time by recursively using (**6**).

Assuming the two deposits need to be positive integers (the bank has decided not to clarify the rules of the competition), `b_(N-1)` must be in the non-inclusive range `(0,10^6)` because, if it were equal to either limit, it would imply one of the deposits was zero, and if it were outside the limit it would imply a deposit was negative. (**7**)


## Base case to working backwards

Assuming the two deposits need to be positive integers, `b_0` and `b_1` must be positive integers. When an attempt to generate a previous day results in zero or a negative number, the recursion must stop.


## Grading function

This function will take a candidate `b_(N-1)` and give us the grading of how many days it can back track.

```
let b_k_plus_2 = 10^6
let b_k_plus_1 = __b_(N-1)__ // The argument to the function.
let b_k = b_k_plus_2 - b_k_plus_1
let N = 2 // We wish to maintain the fact that assuming k=0 implies b_N=10^6.
          // For the starting values here k+2=N; so N=2.
          /* Assuming b_N_minus_1 in the non-inclusive range (0,10^6) 
             implies that this b_k is valid. */
loop with only manual break for exit {
  let candidate_new_b_k = b_k_plus_1 - b_k
  if ( candidate_new_b_k <= 0 ) { 
    break from the loop 
  } else {
    let (   N,               b_k, b_k_plus_1, b_k_plus_2 ) = 
        ( N+1, candidate_new_b_k,        b_k, b_k_plus_1 ) 
      /* Calculated in the simultaneous tuple-packing/unpacking way 
         that Python would do this. */
  }
}
/* Now b_k is tracked back as far as it can go
   and assuming k=0 implies N is our number of days. */
return N
```

## Gathering data

I coded up the grading function in Python 3.8.

I then looped over `b_(N-1)` values for the range `1` to `999999`, each one generating an `N` value from the grading function. I recorded this data in a CSV file. 


## *Excel*lent graph

I opened the CSV with Excel and produced this graph from the data.
![Chart of N against b_(N-1). The domain of b_(N-1) is 1 to 999999. The maximum point (618034,19) is circled and labelled.](https://github.com/JNCressey/MPMP_BankBalance/blob/master/Chart%20of%20N%20against%20b_(N-1).png?raw=true "maximum point at (618034,19)")

The greatest number of days we can score is `19` days. This is achieved for the case when `b_(N-1) = 618034`.


## Solution

I tweaked the grading function slightly to provide an option to return the last two valid balances it produces in the calculations. These are the two starting deposits. `Deposit for day 1 = b_1`; and `deposit for day 2 = b_0`. 

The two starting deposits that achieve the score of `19` days are:

 - day 1: deposit `144`
 - day 2: deposit `154`
 
## The Golden Ratio
 
For a sequence following the rule we have `b_k = b_(k-1) + b_(k-2)`, the ratio between the terms `b_k/b_(k-1)` will tend to the golden ratio phi. It appears that for this solution, there have been enough terms to get close to the ratio. The error `1000000 / 618034 - phi = -2.94*10^-8`, it's very close.

The other way, `1000000 / phi = 618033.99`, gives, to the closest integer, the optimal value for `b_(N-1)`.  Useful as a method of finding the value, but not imediately obvious that this would for certain produce the optimal value without checking other values.
