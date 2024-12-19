# app.py
from flask import Flask
from routes.book_routes import book_blueprint
from routes.member_routes import member_blueprint
from routes.transaction_routes import transaction_blueprint

# Initialize Flask App
app = Flask(__name__)

# Register Blueprints
app.register_blueprint(book_blueprint, url_prefix='/books')
app.register_blueprint(member_blueprint, url_prefix='/members')
app.register_blueprint(transaction_blueprint, url_prefix='/transactions')

@app.route('/')
def home():
    return {"message": "Welcome to the Library Management System API!"}

if __name__ == '__main__':
    app.run(debug=True)



# from flask import Flask, request, jsonify, abort
# from functools import wraps
# import json
# from library_management_system import Book, Member, Library, BorrowLimitExceededException

# # Initialize Flask App
# app = Flask(__name__)

# # Initialize Library
# data_library = Library()

# # Token-based Authentication
# def require_auth(func):
#     @wraps(func)
#     def decorated(*args, **kwargs):
#         token = request.headers.get('Authorization')
#         if not token or token != 'Bearer mysecrettoken':
#             abort(401, description='Unauthorized')
#         return func(*args, **kwargs)
#     return decorated

# # Routes
# @app.route('/')
# def home():
#     return jsonify({"message": "Welcome to the Library Management System API!"})

# @app.route('/books', methods=['GET'])
# @require_auth
# def get_books():
#     """Retrieve all books with optional search and pagination."""
#     search_title = request.args.get('title', '').lower()
#     search_author = request.args.get('author', '').lower()
#     page = int(request.args.get('page', 1))
#     per_page = int(request.args.get('per_page', 5))

#     filtered_books = [
#         book.__dict__ for book in data_library.book_collection
#         if search_title in book.title.lower() or search_author in book.author.lower()
#     ]

#     start = (page - 1) * per_page
#     end = start + per_page
#     paginated_books = filtered_books[start:end]

#     return jsonify(paginated_books), 200

# @app.route('/books', methods=['POST'])
# @require_auth
# def add_book():
#     """Add a new book."""
#     data = request.json
#     try:
#         new_book = Book(len(data_library.book_collection) + 1, data['title'], data['author'], data['category'])
#         data_library.add_book(new_book)
#         return jsonify(new_book.__dict__), 201
#     except ValueError as e:
#         return jsonify({'error': str(e)}), 400

# @app.route('/books/<int:book_id>', methods=['PUT'])
# @require_auth
# def update_book(book_id):
#     """Update an existing book."""
#     data = request.json
#     try:
#         book = data_library.get_book(book_id)
#         book.title = data.get('title', book.title)
#         book.author = data.get('author', book.author)
#         book.category = data.get('category', book.category)
#         data_library.save_books()
#         return jsonify(book.__dict__), 200
#     except ValueError as e:
#         return jsonify({'error': str(e)}), 404

# @app.route('/books/<int:book_id>', methods=['DELETE'])
# @require_auth
# def delete_book(book_id):
#     """Delete a book."""
#     try:
#         book = data_library.get_book(book_id)
#         data_library.book_collection.remove(book)
#         data_library.save_books()
#         return '', 204
#     except ValueError as e:
#         return jsonify({'error': str(e)}), 404

# @app.route('/members', methods=['GET'])
# @require_auth
# def get_members():
#     """Retrieve all members with pagination."""
#     page = int(request.args.get('page', 1))
#     per_page = int(request.args.get('per_page', 5))

#     start = (page - 1) * per_page
#     end = start + per_page
#     paginated_members = [
#         {
#             'member_id': member.member_id,
#             'name': member.name,
#             'membership': member.membership,
#             'borrowed_books': [book.title for book in member.borrowed_books]
#         }
#         for member in data_library.members[start:end]
#     ]

#     return jsonify(paginated_members), 200

# @app.route('/members', methods=['POST'])
# @require_auth
# def add_member():
#     """Register a new member."""
#     data = request.json
#     try:
#         new_member = Member(len(data_library.members) + 1, data['name'], data['membership'])
#         data_library.register_member(new_member)
#         return jsonify({
#             'member_id': new_member.member_id,
#             'name': new_member.name,
#             'membership': new_member.membership
#         }), 201
#     except ValueError as e:
#         return jsonify({'error': str(e)}), 400
    


# # Borrow Book Endpoint
# @app.route('/borrow', methods=['POST'])
# def borrow_book():
#     data = request.get_json()
#     member_id = data.get('member_id')
#     book_id = data.get('book_id')
#     try:
#         data_library.lend_book(member_id, book_id)
#         return jsonify({"message": f"Book ID {book_id} borrowed by Member ID {member_id}"}), 200
#     except (ValueError, BorrowLimitExceededException) as e:
#         return jsonify({"error": str(e)}), 400

# # Return Book Endpoint
# @app.route('/return', methods=['POST'])
# def return_book():
#     data = request.get_json()
#     member_id = data.get('member_id')
#     book_id = data.get('book_id')
#     try:
#         data_library.receive_return(member_id, book_id)
#         return jsonify({"message": f"Book ID {book_id} returned by Member ID {member_id}"}), 200
#     except ValueError as e:
#         return jsonify({"error": str(e)}), 400


# # Main Entry
# if __name__ == '__main__':
#     app.run(debug=True)
