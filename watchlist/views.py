# INF601 - Advanced Programming in Python
# Antonio Hernandez
# Final Project

# Proper import of packages used.
from flask import render_template, request, url_for, redirect, flash
from flask_login import login_user, login_required, logout_user, current_user

from watchlist import app, db
from watchlist.models import User, Movie


@app.route('/', methods=['GET', 'POST'])    # For search - movies
def index():
    if request.method == 'POST':
        if not current_user.is_authenticated:
            return redirect(url_for('index'))

        title = request.form['title']
        year = request.form['year']

        if not title or not year or len(year) != 4 or len(title) > 60:
            flash('Invalid input.')
            return redirect(url_for('index'))

        movie = Movie(title=title, year=year)
        db.session.add(movie)
        db.session.commit()
        flash('Item created.')
        return redirect(url_for('index'))

    movies = Movie.query.all()
    return render_template('index.html', movies=movies)

'''
@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':        # user registers with 3 values
        username = request.form['username']
        email_address = request.form['email']
        password = request.form['password']
        db = get_db()
        error = None

        if not username:        # If error occurs, displays msg to user
            error = 'Username is required.'
        elif not email_address:
            error = 'Email is required.'
        elif not password:
            error = 'Password is required.'

        if error is None:       # If no errors, successfully adds user to database
            try:
                db.execute(
                    "INSERT INTO user (username, email_address, password) VALUES (?, ?, ?)",
                    (username, email_address, generate_password_hash(password)),
                )
                db.commit()
            except db.IntegrityError:       # If username or email is registered/taken..
                error = f"User {username} is already registered."
            except db.IntegrityError:
                error = f"User {email_address} is already registered."
            else:
                return redirect(url_for("auth.login"))

        flash(error)

    return render_template('auth/register.html')
'''



@app.route('/movie/edit/<int:movie_id>', methods=['GET', 'POST'])
@login_required
def edit(movie_id):                             # Change, Edit, etc
    movie = Movie.query.get_or_404(movie_id)

    if request.method == 'POST':
        title = request.form['title']
        year = request.form['year']

        if not title or not year or len(year) != 4 or len(title) > 60:
            flash('Invalid input.')
            return redirect(url_for('edit', movie_id=movie_id))

        movie.title = title
        movie.year = year
        db.session.commit()
        flash('Item updated.')
        return redirect(url_for('index'))

    return render_template('edit.html', movie=movie)


@app.route('/movie/delete/<int:movie_id>', methods=['POST'])
@login_required
def delete(movie_id):                           # Delete / Remove
    movie = Movie.query.get_or_404(movie_id)
    db.session.delete(movie)
    db.session.commit()
    flash('Item deleted.')
    return redirect(url_for('index'))


@app.route('/settings', methods=['GET', 'POST'])
@login_required
def settings():
    if request.method == 'POST':
        name = request.form['name']

        if not name or len(name) > 20:
            flash('Invalid input.')
            return redirect(url_for('settings'))

        user = User.query.first()
        user.name = name
        db.session.commit()
        flash('Settings updated.')
        return redirect(url_for('index'))

    return render_template('settings.html')


@app.route('/login', methods=['GET', 'POST'])
def login():                                # user login with username and password
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if not username or not password:
            flash('Invalid input.')
            return redirect(url_for('login'))

        user = User.query.first()

        if username == user.username and user.validate_password(password):
            login_user(user)
            flash('Login success.')
            return redirect(url_for('index'))

        flash('Invalid username or password.')
        return redirect(url_for('login'))

    return render_template('login.html')


@app.route('/logout')                   # user logs out
@login_required
def logout():
    logout_user()
    flash('Goodbye.')
    return redirect(url_for('index'))