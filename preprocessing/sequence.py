import numpy as np
import pandas as pd 

def pad_sequence(seqs, maxlen, value=0, mode='numpy'):
    """Pad each line of sequence to same length.

    Receive a list of sequences, which are lists of interger, the function 
    will pad the sequences to same length with given value appended at the 
    end of the single seq.

    Args:
        seqs: a list of list, contains the seqs value.
        maxlen: the target length to pad to.
        value: the number to pad the seq.
        mode: return type, 'list' or 'numpy'
    
    Returns:
        A numpy array of a list of lists.
    """
    sample_size = len(seqs)

    output = np.ones((sample_size, maxlen)) * value
    for i, seq in enumerate(seqs):
        output[i,:len(seq)] = np.array(seq)

    if mode == 'numpy':
        return output
    elif mode == 'list':
        return output.tolist()

