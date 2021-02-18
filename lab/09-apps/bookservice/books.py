
class Books:
    """The books class used by the books service."""

    def __init__(self):
        self.books = {
            "978-0-316-45742-2": {
                "title"     : "The Coast-To-Coast Murders",
                "author"    : "James Patterson",
                "publisher" : "Little Brown USA"
            },
            "978-0-525-95498-9": {
                "title"     : "The Evening and the Morning",
                "author"    : "Ken Follett",
                "publisher" : "Penguin LCC US"
            },
            "978-1-250-14523-9": {
                "title"     : "All the Devils Are Here",
                "author"    : "Louise Penny",
                "publisher" : "Macmillan USA"
            }
        }


    def get_books(self):
        return self.books


    def get_book(self, isbn):
        return self.books[isbn]
