def palindromes(text):
    
    if isinstance(text, str):
        delchars = ''.join(c for c in map(chr, range(256)) if not c.isalnum()) #create a string containing all non-alphanumeric characters 
        text = text.translate(None, delchars) # Rid string of these non-alphanumeric characters
        text = text.lower() # Lowercase all characters

        results, start_idxs = [], []

        # Part A: Finds all palindromes in any supplied string
        for i in range(len(text)):
            for j in range(0, i):
                sub = text[j:i + 1]

                if sub == sub[::-1]:
                    results.append(sub)
                    start_idxs.append(j)

        # Part B: Only select palindromes that are a different word/chunk from each other
        # Eg. 'ala' and 'ala' are same substrings so they will be removed
        tuples = [[i,j] for i,j in zip(results, start_idxs)] # Ensures substring corresponds to its start index 
        subs = list(dict(tuples).items()) # Remove tuples from list if first element (substring) is a duplicate
        subs = [i+(len(i[0]),) for i in subs] # Append length of substring to each tuple
        subs.sort(key=lambda x: x[2]) # Sort in ascending order by length, from shortest to longest string

        # Part C: Extracts UNIQUE palindromes. UNIQUE here not only means a different chunk, but a chunk cannot be a substring of a longer string
        # Eg. 'hijkllkjih' and 'ijkllkji' are not unique
        text_only = [i[0] for i in subs]
        unique_subs = [subs[i] for i in range(len(subs)-1) if any(subs[i][0] in x for x in text_only[i+1:]) == False] # Check if palindrome is a substring of a longer palindrome 
        unique_subs.append(subs[-1])

        # Part D: Filter only the top 3 longest palindromes
        unique_subs.sort(key=lambda x: x[2], reverse=True) 
        for i in unique_subs[0:3]:
            print(' Text: ' + str(i[0]) + ' ,Index: ' + str(i[1]) + ' ,Length: ' + str(i[2]))
            
        return unique_subs[0:3]
    else:
        print 'Input variable should be a string.'

