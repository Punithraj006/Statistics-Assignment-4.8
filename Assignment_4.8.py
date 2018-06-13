Problem Statement: 4.8

In one state, 52% of the voters are Republicans, and 48% are Democrats. In a second
state, 47% of the voters are Republicans, and 53% are Democrats. Suppose a simple
random sample of 100 voters are surveyed from each state.


What is the probability that the survey will show a greater percentage of Republican
voters in the second state than in the first state?


Solution:
    
    let P1 = the proportion of Republican voters in the first state,
    P2 = the proportion of Republican voters in the second state,
    p1 = the proportion of Republican voters in the sample from the first state,
    p2 = the proportion of Republican voters in the sample from the second state. 
    The number of voters sampled from the first state (n1) = 100
    the number of voters sampled from the second state (n2) = 100.
    
    
    
    n1P1 = 100 * 0.52 = 52,
    n1(1 - P1) = 100 * 0.48 = 48,
    n2P2 = 100 * 0.47 = 47,
    n2(1 - P2) = 100 * 0.53 = 53
    
    Mean of the difference in sample proportions:
        E(p1 - p2) = P1 - P2 = 0.52 - 0.47 = 0.05.
        
        
     Standard deviation (S.D) =   sqrt{ [ (0.52)(0.48) / 100 ] + [ (0.47)(0.53) / 100 ] } 
                   S.D =         sqrt (0.002496 + 0.002491) = sqrt(0.004987) 
                     S.D= 0.0706
                     
                     
    To find the probability: 
        Z(p1-p2) = (0 - 0.05)/0.0706 = -0.7082
        
Using Stat Trek's Normal Distribution Calculator,
 we find that the probability of a z-score being -0.7082 or less is 0.24.
 
 Therefore, the probability that the survey will show a greater percentage of
 Republican voters in the second state than in the first state is 0.24.