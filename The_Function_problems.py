# version code 542eddf1f327+
coursera = 1
# Please fill out this stencil and submit using the provided submission script.





## 1: (Problem 1) Tuple Sum
def tuple_sum(A, B):
    '''
    Input:
      -A: a list of tuples
      -B: a list of tuples
    Output:
      -list of pairs (x,y) in which the first element of the
      ith pair is the sum of the first element of the ith pair in
      A and the first element of the ith pair in B
    Examples:
    >>> tuple_sum([(1,2), (10,20)],[(3,4), (30,40)])
    [(4, 6), (40, 60)]
    >>> tuple_sum([(0,1),(-1,0),(2,2)], [(3,4),(5,6),(7,8)])
    [(3, 5), (4, 6), (9, 10)]
    '''
    [ ( A[i][0] + B[i][0], A[i][1] + B[i][1] ) for i in range(len(A)) ]



## 2: (Problem 2) Inverse Dictionary
def inv_dict(d):
    '''
    Input:
      -d: dictionary representing an invertible function f
    Output:
      -dictionary representing the inverse of f, the returned dictionary's
       keys are the values of d and its values are the keys of d
    Example:
    >>> inv_dict({'goodbye':  'au revoir', 'thank you': 'merci'}) == {'merci':'thank you', 'au revoir':'goodbye'}
    '''
    { v:k for (k,v) in d.items() }




## 3: (Problem 3) Nested Comprehension
def row(p, n):
    '''
    Input:
      -p: a number
      -n: a number
    Output:
      - n-element list such that element i is p+i
    Examples:
    >>> row(10,4)
    [10, 11, 12, 13]
    '''
    [ x+p for x in range(n) ]

comprehension_with_row = [ row(i, 20) for i in range(15) ]

comprehension_without_row = [ [ x+i for x in range(20) ] for i in range(15) ]



## 4: (Problem 4) Probability Exercise 1
codomain = {2:.5, 3:.2, 4:.1, 6:.1, 7:.1}
Pr_f_is_even = .7
Pr_f_is_odd  = .3



## 5: (Problem 5) Probability Exercise 2
codomain2 = {1:.2, 2:.2, 3:.2, 4:.1, 5:.1, 6:.1, 7:.1}
Pr_g_is_1    = .4
Pr_g_is_0or2 = .6

