from bibtexparser.bwriter import BibTexWriter
from bibtexparser.bibdatabase import BibDatabase
import datetime
def get_references(db_conn):
    database_connection = db_conn
    cursor = database_connection.cursor()

    cursor.execute("SELECT id, author, title, year, publisher, tag FROM book;")
    references = cursor.fetchall()
    return references

def get_references_by_tag(tag, db_conn):
    cursor = db_conn.cursor()
    print(tag)
    if tag is None:
        cursor.execute('SELECT * FROM book')
    else:
        cursor.execute('SELECT * FROM book WHERE tag=?', [tag])
    filtered_references = cursor.fetchall()
    return filtered_references

def get_references_by_tag_and_sort_by_year_asc(tag, db_conn):
    cursor = db_conn.cursor()
    if tag is None or "all":
        cursor.execute('select * FROM book ORDER BY year ASC')
    else:
        cursor.execute('SELECT * FROM book WHERE tag=? ORDER BY year ASC', [tag])
    filtered_references = cursor.fetchall()
    return filtered_references

def get_references_by_tag_and_sort_by_year_desc(tag, db_conn):
    cursor = db_conn.cursor()
    if tag is None or "all":
        cursor.execute('select * FROM book ORDER BY year DESC')
    else:
        cursor.execute('SELECT * FROM book WHERE tag=? ORDER BY year DESC', [tag])
    filtered_references = cursor.fetchall()
    return filtered_references

def get_references_by_tag_and_sort_by_added_asc(tag, db_conn):
    cursor = db_conn.cursor()
    if tag is None or "all":
        cursor.execute('select * FROM book ORDER BY addedDate ASC')
    else:
        cursor.execute('SELECT * FROM book WHERE tag=? ORDER BY addedDate ASC', [tag])
    filtered_references = cursor.fetchall()
    return filtered_references

def get_references_by_tag_and_sort_by_added_desc(tag, db_conn):
    cursor = db_conn.cursor()
    if tag is None or "all":
        cursor.execute('select * FROM book ORDER BY addedDate DESC')
    else:
        cursor.execute('SELECT * FROM book WHERE tag=? ORDER BY addedDate DESC', [tag])
    filtered_references = cursor.fetchall()
    return filtered_references

def get_references_by_tag_and_sort(tag, sort, db_conn):
    print(sort)
    if sort == "year_asc":
        filtered_references = get_references_by_tag_and_sort_by_year_asc(tag, db_conn)
    elif sort == "year_desc":
        filtered_references = get_references_by_tag_and_sort_by_year_desc(tag, db_conn)
    elif sort == "added_asc":
        filtered_references = get_references_by_tag_and_sort_by_added_asc(tag, db_conn)
    elif sort == "added_desc":
        filtered_references = get_references_by_tag_and_sort_by_added_desc(tag, db_conn)
    elif sort is None:
        filtered_references = get_references_by_tag(tag, db_conn)
    print(filtered_references)
    return filtered_references


def get_reference_by_id(viite_id, db_conn):
    cursor = db_conn.cursor()
    cursor.execute('SELECT * FROM book WHERE id=?', [viite_id])
    reference = cursor.fetchall()
    return reference

def add_book(author, title, year, publisher, tag, db_conn):
    if not isinstance(year, int):
        return "Vuoden on oltava numero"

    if not isinstance(author, str):
        return "Kirjailijan on oltava merkkijono"

    if not isinstance(title, str):
        return "Otsikon on oltava merkkijono"

    if not isinstance(publisher, str):
        return "Julkaisijan on oltava merkkijono"

    if len(author) < 1 or len(title) < 1 or year < 1 or len(publisher) < 1:
        return "Syötteen pituus on oltava yli 1"
    addedDate = datetime.datetime.now()
    conn = db_conn
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO book (author, title, year, publisher, addedDate, tag) VALUES (?, ?, ?, ?, ?, ?)',
        (author, title, year, publisher, addedDate, tag)
    )
    conn.commit()
    return True

def delete_book(viite, db_conn):
    try:
        conn = db_conn
        cursor = conn.cursor()
        cursor.execute('DELETE FROM book WHERE id=?', viite)
        conn.commit()
        return True
    except:
        return "Kirjan poistamisessa tapahtui virhe"

def get_tags(db_conn):
    conn = db_conn
    cursor = conn.cursor()
    cursor.execute('SELECT tag FROM book')
    tags = cursor.fetchall()
    print(tags)
    return tags

def get_unique_tags(db_conn):
    all_tags = get_tags(db_conn)
    tags = []
    for tag in all_tags:
        if tag not in tags:
            tags.append(tag)
    tags.append(('all',))
    return tags

def generate_bibtex(references):
    db = BibDatabase()
    db.entries = []
    for reference in references:
        db.entries.append({
            'ID': 'viite',
            'author': reference[1],
            'title': reference[2],
            'year': str(reference[3]),
            'publisher': reference[4],
            'ENTRYTYPE': 'book'
        })
    writer = BibTexWriter()
    writer.entry_separator = ';\n'
    bibtex = writer.write(db)
    return bibtex.split(';\n')
