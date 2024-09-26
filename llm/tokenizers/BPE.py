from collections import defaultdict

# step 2:  Initialize the dataset
def get_initial_vocab(dataset):
    vocab = {}
    for word in dataset:
        chars = list(word)
        chars.append('</w>')
        token = ' '.join(chars)
        if token in vocab:
            vocab[token] += 1
        else:
            vocab[token] = 1
    return vocab


# step 3: Define Functions to Compute Pair Frequencies and Merge Pairs
def get_stats(vocab):
    """Compute frequency of each pair of symbols."""
    pairs = defaultdict(int)
    for word, freq in vocab.items():
        symbols = word.split()
        for i in range(len(symbols)-1):
            pair = (symbols[i], symbols[i+1])
            pairs[pair] += freq
    return pairs

def merge_vocab(pair, vocab):
    """Merge all occurrences of the most frequent pair in the vocabulary."""
    new_vocab = {}
    bigram = ' '.join(pair)
    replacement = ''.join(pair)
    for word in vocab:
        new_word = word.replace(bigram, replacement)
        new_vocab[new_word] = vocab[word]
    return new_vocab

# step 5: Tokenize new Text using learned BPE operations
def learn_bpe_operations(dataset, num_merges):
    vocab = get_initial_vocab(dataset)
    merges = []
    for i in range(num_merges):
        pairs = get_stats(vocab)
        if not pairs:
            break
        best_pair = max(pairs, key=pairs.get)
        vocab = merge_vocab(best_pair, vocab)
        print(f"Step {i + 1}: Merged pair {best_pair}")
        print(f"Updated Vocabulary: {vocab}\n")
        merges.append(best_pair)
    return merges


def tokenize(word, merges):
    # Initialize the word as a list of characters ending with '</w>'
    symbols = list(word) + ['</w>']
    idx = 0
    while idx < len(symbols) - 1:
        pair = (symbols[idx], symbols[idx+1])
        if pair in merges:
            # Merge the pair
            symbols[idx:idx+2] = [''.join(pair)]
            # Restart from the previous index if possible
            if idx > 0:
                idx -= 1
        else:
            idx += 1
    # Remove the end-of-word token for display purposes
    if symbols[-1] == '</w>':
        symbols = symbols[:-1]
    return symbols

if __name__ == "__main__":
    # Example usage
    # step 1:  Prepare the dataset
    dataset = [
        'low',
        'lowest',
        'newest',
        'wider',
        'low',
        'lowest',
        'low',
        'new',
        'wide',
        'widest',
    ]
    vocab = get_initial_vocab(dataset)
    num_merges = 10
    bpe_merges = learn_bpe_operations(dataset, num_merges)
    new_word = 'lowest'
    tokenized_word = tokenize(new_word, bpe_merges)
    print(f"Tokenized '{new_word}': {tokenized_word}")
