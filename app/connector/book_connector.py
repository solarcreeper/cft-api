from bson import ObjectId

from app.data_model.book_model.book import Book


class BookController(object):
    @classmethod
    def query(cls, **kwargs):
        books = Book.objects(name=kwargs.get('name')).first()
        return books

    @classmethod
    def update(cls, book, **kwargs):
        try:
            book.update(**kwargs)
            book = book.reload()
            return book
        except Exception as err:
            print(err)

    @classmethod
    def delete(cls, name):
        Book.objects.get(name=name).delete()

    @classmethod
    def add(cls, **kwargs):
        book_obj = Book.objects(name=kwargs.get('name')).first()
        if book_obj is None:
            if not kwargs.get('id'):
                kwargs['id'] = ObjectId()
            book_obj = Book(**kwargs).save()
        return book_obj
