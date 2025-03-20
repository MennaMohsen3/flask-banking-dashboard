from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

# Sample banking data
data = {
    "Account": ["Savings", "Checking", "Credit Card"],
    "Balance": [15000, 4200, -2000],
    "Currency": ["USD", "USD", "USD"]
}
df = pd.DataFrame(data)

@app.route("/")
def dashboard():
    return render_template("index.html", data=df.to_dict(orient="records"))

if __name__ == "__main__":
    app.run(port=5000, debug=True)
