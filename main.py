# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

story = 'C:/Users/HP/Downloads/Reading-Text-Files/Reading-Text-Files/story.txt'

def read_file_content(story):
    # [assignment] Add your code here
    story = open(story, 'r')
    lines = story.readlines()
    story.close()
    
    return lines


def count_words(story):
    text = str(read_file_content(story)).split()
    # [assignment] Add your code here
    counts = dict()

    for word in text:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
            
    return counts
print(count_words(story))
