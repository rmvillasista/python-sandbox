def evaluate_priority(score):
    if score >= 90:
        return "URGENT"
    elif score >= 50:
        return "NORMAL"
    elif score > 0:
        return "LOW"
    else:
        return "INVALID"

test_scores = [95, 60, 10, -5]

for score in test_scores:
    priority = evaluate_priority(score)
    print(f"Score: {score:3d} -> Priority: {priority}")