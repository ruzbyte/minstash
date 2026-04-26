from flask import render_template, request, redirect, url_for, session
from sqlalchemy import text

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        result = db.session.execute(text(query))
        user = result.fetchone()

        print(f"Login attempt: username={username}, password={password}")
        if user:
            print(user)
            session['username'] = user.username or 'unknown'
            return redirect(url_for('home'))
        else:
            error = 'Ungültige Zugangsdaten.'

    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        retypepassword = request.form['retypepassword']

        if password != retypepassword:
            error = 'Passwörter stimmen nicht überein.'
            return render_template('register.html', error=error)

        neuer_user = User(username=username, password=password)
        db.session.add(neuer_user)
        db.session.commit()
        session['username'] = username
        return redirect(url_for('home'))

    return render_template('register.html', error=error)

@app.route('/search')
def search():
    q = request.args.get('q', '')

    query = f"SELECT * FROM blog_artikel WHERE title LIKE '%{q}%' OR content LIKE '%{q}%'"
    result = db.session.execute(text(query))
    items = result.fetchall()

    return render_template('search.html', items=items, q=q)


@app.route('/artikel')
def artikel():
    return render_template('artikel.html')


@app.route('/blog')
def blog():
    artikel_liste = BlogArtikel.query.order_by(BlogArtikel.created_at.desc()).all()
    return render_template('blog.html', items=artikel_liste)


@app.route('/blog/<int:id>')
def blog_artikel(id):
    artikel = BlogArtikel.query.get_or_404(id)
    return render_template('artikel.html', artikel=artikel)


@app.route('/blog/neu', methods=['GET', 'POST'])
def neuer_artikel():
    if not session.get('username'):
        return redirect(url_for('login'))
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        author = request.form['author']
        neuer = BlogArtikel(title=title, content=content, author=author)
        db.session.add(neuer)
        db.session.commit()
        return redirect(url_for('blog'))
    return render_template('neuer_artikel.html')
