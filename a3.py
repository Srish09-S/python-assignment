first_term = float(input("first term (a): "))
common_diff = float(input("common difference (d): "))
n_terms = int(input("Enter num of terms : "))
nth_term = first_term + (n_terms - 1) * common_diff
print(f"The nth term is:",nth_term)
sum_nth = (n_terms / 2) * (2 * first_term + (n_terms - 1) * common_diff)
print(f"The sum up to the nth term is:",sum_nth)