DROP TABLE IF EXISTS blogs;

CREATE TABLE blogs (
    id INT PRIMARY KEY,
    _date TEXT DEFAULT (strftime('%Y-%m-%d %H:%M:%f', 'now')),
    _title TEXT,
    _description TEXT,
    _auther TEXT,
    _likes INT DEFAULT 0,
    _dislikes INT DEFAULT 0
);