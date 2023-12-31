import os
import re

qData_folder = "Qdata"

# We are taking the body of the question, so we stop reading once we encounter examples
target_str = "Example 1:"

all_lines = []

for i in range(1, 2177):
    # adding body of the ith question
    file_path = os.path.join(qData_folder, "{}/{}.txt".format(i, i))

    doc = ""
    with open(file_path, "r", encoding='utf-8', errors="ignore") as f:
        lines = f.readlines()

    for line in lines:
        if target_str in line:
            break
        else:
            doc += line

    all_lines.append(doc)


# adding heading of the ith question
head_path = os.path.join(qData_folder, "index.txt")

with open(head_path, "r", encoding='utf-8', errors="ignore") as f:
    headings = f.readlines()

for (i, heading) in enumerate(headings, 0):
    try:
        # removing the Q No from the heading
        words = heading.split()
        if len(words) >= 2:
            heading = ' '.join(words[1:])
            # Now adding the remaining words in the heading to the respective q's body
            all_lines[i] += heading
        else:
            # Handle the case when there are not enough words in the heading
            print("Error: Not enough words in the heading.")
    except IndexError:
        # Handle the IndexError here
        print("Error: Index out of range occurred.")


def preprocess(text):      # remove problem no, and return a list of lowercase words
    # removing non alphanumeric chars
    text = re.sub(r'[^a-zA-Z0-9\s-]', '', text)
    terms = [term.lower() for term in text.strip().split()]

    return terms


vocab = {}          # word : no of docs that word is present in
documents = []      # all lists, with each list containing words of a document

for (index, line) in enumerate(all_lines):
    tokens = preprocess(line)  # list of processed words of this doc
    documents.append(tokens)

    tokens = set(tokens)
    for token in tokens:
        if token not in vocab:
            vocab[token] = 1
        else:
            vocab[token] += 1

# reverse sort vocab by values (by the no of docs the word is present in)
vocab = dict(sorted(vocab.items(), key=lambda item: item[1], reverse=True))


print("No of documents : ", len(documents))
print("Size of vocab : ", len(vocab))
print("Sample document: ", documents[100])

# keys of vocab thus is a set of distinct words across all docs
# save them in file vocab
with open("TF-IDF/vocab.txt", "w", encoding='utf-8', errors="ignore") as f:
    for key in vocab.keys():
        f.write("%s\n" % key)

# save idf values
with open("TF-IDF/idf-values.txt", "w", encoding='utf-8', errors="ignore") as f:
    for key in vocab.keys():
        f.write("%s\n" % vocab[key])


# save the documents(lists of words for each doc)
with open("TF-IDF/documents.txt", "w", encoding='utf-8', errors="ignore") as f:
    for doc in documents:
        f.write("%s\n" % doc)

# word : list of index of docs the word is present in.
inverted_index = {}
# inserting word multiple times from same doc too, so that we even get the term freq from here itself
for (index, doc) in enumerate(documents, start=1):
    for token in doc:
        if token not in inverted_index:
            inverted_index[token] = [index]
        else:
            inverted_index[token].append(index)


# save the inverted index in a file
with open("TF-IDF/inverted-index.txt", 'w', encoding='utf-8', errors="ignore") as f:
    for key in inverted_index.keys():
        f.write("%s\n" % key)

        doc_indexes = ' '.join([str(term) for term in inverted_index[key]])
        f.write("%s\n" % doc_indexes)
