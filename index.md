# Introduction

This is my solution to one of Matt Parker's Maths Problems.
See the video on YouTube for the problem: [MPMP: The 1 Million Bank Balance puzzle](https://www.youtube.com/watch?v=ILrqPpLpwpE)

# Solution

## Evolution of the sequence

The sequence evolves like the Fibonacci sequence: b_k = b_(k-1) + b_(k-2). ('b' for 'balance') (**1**)


## Initial conditions of the sequence

Let b_1 be the first balance, and b_2 be the second balance. 

Let d_1 be the first deposit, and d_2 be the second deposit.

In the question description, b_2 = b_1 + d_2. (**2**) 

By (**1**), b_2 = b_1 + b_0. (**3**)

By (**2**) and (**3**), we can pretend there is a balance zero, b_0 = d_2. (**4**)

Thus the initial conditions can be thought of as b_0=d_2; b_1=d_1.


## Working backwards

For a solution to be valid (and not 'trivial' as said in the video), we need b_N = 10^6 for some integer N > 3. (**5**)

We can rearrange (**1**) as b_(k-2) = b_k - b_(k-1), or equivalently b_k = b_(k+2)-b_(k+1) (**6**)

The evolution step needs two knowns, so we can take an arbitrary b_(N-1) and that will define a definite sequence going back in time by recursively using (**6**).

Assuming the two deposits need to be positive integers (the bank has decided not to clarify the rules of the competition), b_(N-1) must be in the non-inclusive range (0,10^6) because, if it were equal to either limit, it would imply one of the deposits was zero, and if it were outside the limit it would imply a deposit was negative. (**7**)


## Base case to working backwards

Assuming the two deposits need to be positive integers, b_0 and b_1 must be positive integers. When an attempt to generate a previous day results in zero or a negative number, the recursion must stop.


## Grading function

This function will take a candidate b_(N-1) and give us the grading of how many days it can back track.

```
let b_k_plus_2 = 10^6
let b_k_plus_1 = __b_(N-1)__ // The argument to the function.
let b_k = b_k_plus_2 - b_k_plus_1
let N = 1 // When b_k is verified to be greater than 0, N will be set to 2. 
          // That means that if k was taken to equal 0 then, b_2 would be the 10^6.
while (b_k > 0){
  let N = N + 1
  // if k is taken to be 0 here, b_N is then the 10^6
  let (b_k, b_k_plus_1, b_k_plus_2) = (b_k_plus_2 - b_k_plus_1, b_k, b_k_plus_1) 
      /* Calculated in the simultaneous tuple-packing/unpacking way 
         that Python would do this. */
}
// b_k is now one step too far back, thus k=-1.
let b_0 = b_k_plus_1 // this is the second day's deposit
let b_1 = b_k_plus_2 // this is the first day's deposit
/* **Note:** N has not been incremented since the value we have for b_k_plus_1
   was in the b_k slot, so N has its correct value relative to b_0 and b_1. */
return N // this is the number of the day 10^6 balance is reached
```

## Following up

1. I will code up the grading function

2. I will plot its results on a line graph against all the integers from 1 to 999999.

3. The highest point of the graph will be the solution for the days, and the grading function can be trivially tweaked to tell us the starting deposit values.

