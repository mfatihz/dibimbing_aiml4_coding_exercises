def score(values, approved, not_approved):
    score = 0

    for x in values:
        if x in approved:
            score += 1
        if x in not_approved:
            score -= 1
    
    return score

result = score([1, 1, 3, 5, 5, 6, 7, 3], [1, 3], [5])
print(str(result))