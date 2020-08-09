# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx
def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    
    length = len(sequence)
    # no_perm = math.perm(length)
    count = 0
    list_word = []
    # A first char separator
    if length == 1:
        return sequence
    
    elif length > 1: 
        first_char = sequence[0]
        remainder = sequence[1:]
        temp_list_word = get_permutations(remainder)
    
    # A remaining word permutator
        #my program
    # A first word recombiner 
    
    for word in temp_list_word:
        permu_counter = len(word)
        count = 0
        while permu_counter >= 0:
            combi = word[:count] + first_char + word[(count):(length-1)]
            permu_counter -= 1
            count += 1
            list_word.append(combi)
    return list_word
    
if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

    
    example_input_1 = 'abc'
    print('Input:', example_input_1)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input_1))

    example_input_2 = 'xyz'
    print('Input:', example_input_2)
    print('Expected Output:', ['xyz', 'xzy', 'yxz', 'yzx', 'zxy', 'zyx'])
    print('Actual Output:', get_permutations(example_input_2))
