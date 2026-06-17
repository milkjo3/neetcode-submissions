class PrefixTree:

    # Node structure
    def __init__(self):
        self.children = {}
        self.is_word = False

    def insert(self, word: str) -> None:
        # Begin at the root
        node = self
        
        # Iterate through word character by character.
        for char in word:

            # If the current char is not in the tree, create a new node.
            if char not in node.children:
                node.children[char] = PrefixTree()

            # Move to the newly created node (Character).
            node = node.children[char]

        # We've reached the end of the word, set is_word flag to true.
        node.is_word = True


    def search(self, word: str) -> bool:
        # Start at the root.
        node = self

        # Iterate through word character by character.
        for char in word:

            # If any of the characters are not in the tree, the word DNE.
            if char not in node.children:
                return False
            
            # Move to the next character (node).
            node = node.children[char]

        # We've reached the end of the word, if we've inserted it, then it exists.
        return node.is_word


    def startsWith(self, prefix: str) -> bool:
        # Start at the root.
        node = self

        # Iterate through the prefix character by character. 
        for char in prefix:

            # If the any of the characters are not there, then no word has this prefix.
            if char not in node.children:
                return False

            # Moev onto the next character (node).
            node = node.children[char]

        # Return True as there exists one word in the tree with the prefix.
        return True
        
        