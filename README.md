python-shuffle
==============

Let’s say one is a computer programmer and let’s say one’s wife (or roommate; or significant other) does social 
science research (a totally hypothetical scenario of course). When doing social science research one needs to create 
randomized groups of participants.

So in a group you might be testing a variable X and you need to divide the group in half to test that variable 
with a number of control subjects. In this scenario, one needs to create groups A and B (or 1 and 2) such that there 
are the same number of A and B in a given set.

Now normally when generating random numbers you can just generate an arbitrary set of random numbers. But if you need 
a set of 10 numbers with 5 1′s and 5 2′s then that’s a different problem. You could of course generate a set and test 
to make sure it’s evenly distributed and then throw it away if it doesn’t meet this constraint. That of course is 
an inefficient way of generating your sets because you would likely have to throw a lot of them away.

The solution to this conundrum is to use random numbers not to create your set, but to shuffle it. Luckily other 
smart people have proven ways to do this already. The Fisher-Yates shuffle is the technique that I used.
