from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

dataset = {
    "M1": ["Differential Equations", "Matrices", "Laplace Transforms", "Vector Calculus", "Probability"],
    "EDA": ["Data Preprocessing", "Regression", "Classification", "Clustering", "Model Evaluation"],
    "DMS": ["Logic", "Set Theory", "Graph Theory", "Combinatorics", "Relations"]
}

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/generate-plan", methods=["POST"])
def generate_plan():
    data = request.json
    scores = {
        "M1": int(data["m1"]),
        "EDA": int(data["eda"]),
        "DMS": int(data["dms"])
    }

    sorted_scores = sorted(scores.items(), key=lambda x: x[1])
    lowest = sorted_scores[0][0]
    medium = sorted_scores[1][0]
    highest = sorted_scores[2][0]

    subjects = [lowest, lowest, medium, lowest, medium, highest, lowest]

    plan = []
    for i in range(7):
        sub = subjects[i]
        topic = dataset[sub][i % len(dataset[sub])]
        plan.append({
            "day": i + 1,
            "subject": sub,
            "chapter": topic
        })

    return jsonify({
        "lowest": lowest,
        "medium": medium,
        "highest": highest,
        "plan": plan
    })

if __name__ == "__main__":
    app.run(debug=True)