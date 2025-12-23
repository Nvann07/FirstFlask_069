from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None

    if request.method == "POST":
        nama = request.form.get("nama", "").strip()
        warga = request.form.get("warga", "").strip()

        if not nama or not warga:
            error = "Nama dan Warga wajib diisi!"
        else:
            result = f"Woyyyy {nama}, kamu warga {warga}"

    return render_template("index.html", result=result, error=error)

if __name__ == "__main__":
    app.run(debug=True)
