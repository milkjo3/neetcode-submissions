class WordDictionary:

    # Node structure.
    def __init__(self):
        self.children = {}
        self.is_word = False 
    

    # Add a word to the Trie.
    def addWord(self, word: str) -> None:
        # Start at the root.
        node = self

        # Iterate through the word.
        for char in word:

            # If the character is not a children node: make one for it.
            if char not in node.children:

                # Create Children Trie node.
                node.children[char] = WordDictionary()

            # Move downward along the Trie path.
            node = node.children[char]

        # We've added the word. Now set the final node (character) to indicate a word was inserted.
        node.is_word = True

    # Search for words in the Trie.
    def search(self, word: str) -> bool:

        # DFS to search for all possible words though "." words.
        def backtrack(index, node):

            # Base case. We've reached the end of the word.
            if index == len(word):
                return node.is_word

            # Get the current character.
            char = word[index]

            # If the character is normal, look in the children to see if it exists.
            if char != ".":
                if char not in node.children:
                    return False    
                
                # Character (child node) exists, move onto the next character in the word.
                return backtrack(index + 1, node.children[char])

            # The character is a ".", which can be any character.
            else:

                # We must recurse toward all possible characters to find a valid word.
                for child in node.children.values():

                    # Recurse into a path. If it is true, the word exists in our Trie.
                    if backtrack(index + 1, child):
                        return True

                # We've gone through all possibilities, and found no words that match the word with
                # the dot "." notation. 
                return False

        # Begin searching recursively.
        return backtrack(0, self)