query = input('Enter your query: ')
q_terms = [term.lower() for term in query.strip().split()]

print(q_terms)
print(calc_docs_sorted_order(q_terms)[0])
print(len(calc_docs_sorted_order(q_terms)))