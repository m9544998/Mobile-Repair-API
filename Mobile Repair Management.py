from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Create database
conn = sqlite3.connect("repair.db")
conn.execute("""
CREATE TABLE IF NOT EXISTS repairs(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_name TEXT,
    mobile_model TEXT,
    problem TEXT,
    repair_cost REAL
)
""")
conn.commit()
conn.close()


# POST - Add Repair
@app.route("/repairs", methods=["POST"])
def add_repair():
    data = request.get_json()

    conn = sqlite3.connect("repair.db")
    conn.execute(
        """INSERT INTO repairs
        (customer_name, mobile_model, problem, repair_cost)
        VALUES (?, ?, ?, ?)""",
        (
            data["customer_name"],
            data["mobile_model"],
            data["problem"],
            data["repair_cost"]
        )
    )
    conn.commit()
    conn.close()

    return jsonify({"message": "Repair Added Successfully"}), 201


# GET - View Repairs
@app.route("/repairs", methods=["GET"])
def get_repairs():
    conn = sqlite3.connect("repair.db")
    conn.row_factory = sqlite3.Row

    repairs = conn.execute("SELECT * FROM repairs").fetchall()
    conn.close()

    return jsonify([dict(repair) for repair in repairs])


# PUT - Update Repair
@app.route("/repairs/<int:id>", methods=["PUT"])
def update_repair(id):
    data = request.get_json()

    conn = sqlite3.connect("repair.db")
    conn.execute(
        """UPDATE repairs
        SET customer_name=?, mobile_model=?, problem=?, repair_cost=?
        WHERE id=?""",
        (
            data["customer_name"],
            data["mobile_model"],
            data["problem"],
            data["repair_cost"],
            id
        )
    )
    conn.commit()
    conn.close()

    return jsonify({"message": "Repair Updated Successfully"})


# DELETE - Delete Repair
@app.route("/repairs/<int:id>", methods=["DELETE"])
def delete_repair(id):
    conn = sqlite3.connect("repair.db")

    conn.execute(
        "DELETE FROM repairs WHERE id=?",
        (id,)
    )

    conn.commit()
    conn.close()

    return jsonify({"message": "Repair Deleted Successfully"})


if __name__ == "__main__":
    app.run(debug=True)