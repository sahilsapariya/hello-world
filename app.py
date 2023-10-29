from flask import Flask, request, jsonify
from init_db import get_database_conn
import uuid
import datetime

app = Flask(__name__)


@app.route('/')
def Home():
    conn = get_database_conn()
    data = conn.execute("SELECT * FROM blogs").fetchall()
    conn.close()

    if data is None:
        return {
            "message": "No data found"
        }

    data = [dict(row) for row in data]

    return {
        "message": f"found {len(data)} blogs",
        "data": data,
        "success": True
    }

@app.route('/create-blog', methods=['POST'])
def CreateBlog():
    if request.method == 'POST':
        data = request.get_json()
        title = data['title']
        description = data["description"]
        author = data["auther"]
        date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        id = uuid.uuid4().hex

        conn = get_database_conn()
        cur = conn.cursor()

        cur.execute("INSERT INTO blogs (id, _title, _description, _auther, _date) VALUES(?,?,?,?,?)", (id, title, description, author, date))

        cur.close()
        conn.commit()
        conn.close()

        return {
            "message": "blog inserted successfully!",
            "success": True
        }
    

@app.route('/delete-blog/<id>', methods=['DELETE'])
def DeleteBlog(id):
    conn = get_database_conn()
    cur = conn.cursor()
    cur.execute("DELETE FROM blogs WHERE id = ?", (id,))
    cur.close()
    conn.commit()
    conn.close()

    return {
        "message": "blog deleted successfully!",
        "success": True
    }


@app.route('/update-blog/<id>', methods=['PUT', 'PATCH'])
def update_blog(id):
    conn = get_database_conn()
    blog = conn.execute("SELECT * FROM blogs WHERE id = ?", (id,)).fetchone()

    if blog is None:
        return jsonify({
            "message": "sorry blog not found or something went wrong. Try again!",
            "success": False
        }), 400
    
    data = request.get_json()

    cursor = conn.cursor()
    cursor.execute("UPDATE blogs SET _title=?, _description=?, _auther=?, _likes=?, _dislikes=? WHERE id=?", (data["title"], data["description"], data["auther"], data["likes"], data["dislikes"], id))

    cursor.close()
    conn.commit()
    conn.close()
    
    return jsonify({
        "message": "Blog updated successfully!",
        "success": True
    }), 200


if __name__ == "__main__":
    app.run()
