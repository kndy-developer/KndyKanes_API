from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data (replace with your data model)
books = [
    {"id": 1, "title": "Book 1", "author": "Author 1"},
    {"id": 2, "title": "Book 2", "author": "Author 2"},
]

# GET all books
@app.route('/books', methods=['GET'])
def get_all_books():
    return jsonify(books)

# GET a book by ID
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = [b for b in books if b['id'] == book_id]
    if book:
        return jsonify(book[0])
    else:
        return jsonify({'message': 'Book not found'}), 404

# Run the app
if __name__ == '__main__':
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)
    app.run(debug=True)
