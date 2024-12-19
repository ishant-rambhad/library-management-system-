from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Book and Member Models
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Book {self.title}>'

class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)

    def __repr__(self):
        return f'<Member {self.name}>'
@app.route('/')
def index():
    return render_template('index.html')

# Routes for books
@app.route('/books')
def books():
    books = Book.query.all()
    return render_template('books.html', books=books)

@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        year = request.form['year']
        new_book = Book(title=title, author=author, year=year)
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('books'))
    return render_template('add_book.html')

@app.route('/edit_book/<int:id>', methods=['GET', 'POST'])
def edit_book(id):
    book = Book.query.get_or_404(id)
    if request.method == 'POST':
        book.title = request.form['title']
        book.author = request.form['author']
        book.year = request.form['year']
        db.session.commit()
        return redirect(url_for('books'))
    return render_template('edit_book.html', book=book)

@app.route('/delete_book/<int:id>')
def delete_book(id):
    book = Book.query.get_or_404(id)
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for('books'))

# Routes for members
@app.route('/members')
def members():
    members = Member.query.all()
    return render_template('members.html', members=members)

@app.route('/add_member', methods=['GET', 'POST'])
def add_member():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        new_member = Member(name=name, email=email)
        db.session.add(new_member)
        db.session.commit()
        return redirect(url_for('members'))
    return render_template('add_member.html')

@app.route('/edit_member/<int:id>', methods=['GET', 'POST'])
def edit_member(id):
    member = Member.query.get_or_404(id)
    if request.method == 'POST':
        member.name = request.form['name']
        member.email = request.form['email']
        db.session.commit()
        return redirect(url_for('members'))
    return render_template('edit_member.html', member=member)

@app.route('/delete_member/<int:id>')
def delete_member(id):
    member = Member.query.get_or_404(id)
    db.session.delete(member)
    db.session.commit()
    return redirect(url_for('members'))

# Initialize database
# @app.before_first_request
# def create_tables():
#     db.create_all()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
