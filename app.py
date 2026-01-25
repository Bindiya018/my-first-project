from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/check", methods=["POST"])
def check_inventory():
    system_stock = int(request.form["system"])
    actual_stock = int(request.form["actual"])

    if system_stock != actual_stock:
        result = f"⚠️ Inventory Distortion Detected! Difference: {system_stock - actual_stock}"
        status = "warning"
    else:
        result = "✅ Inventory is Accurate"
        status = "success"

    return render_template("index.html", result=result, status=status)

if __name__ == "__main__":
    app.run(debug=True)
