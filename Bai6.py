student = {
    "name": "Lan",
    "scores": {
        "math": 9,
        "english": 8,
        "history": 7
    }
}

english_score = student["scores"]["english"]
print(english_score)

scores = student["scores"].values()
average = sum(scores) / len(scores)

print(average)
