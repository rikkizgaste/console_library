from sqlalchemy.orm import sessionmaker
from library import engine, Book, BookInstance

Session = sessionmaker(bind=engine)
session = Session()

while True:
    option = int(input("Pasirinkite veiksmą: \n1 - sukurkite knygą \n2 - pridėti knygos kopiją \n3 - pasiskolinti "
                        "knygos kopiją \n4 - gražinti knygos kopiją\n5 - rasti knygos kopiją\n6 - baigti programą\n"))

    if option == 1:
        title = input("Įveskite knygos pavadinimą\n")
        author = input("Įveskite knygos autoriaus vardą ir pavardę\n")
        year = int(input("Įveskite knygos išleidimo metus\n"))
        book = Book(title, author, year)
        session.add(book)
        session.commit()

    if option == 2:
        books = session.query(Book).all()
        print("-------------------")
        for book in books:
            print(book)
        print("-------------------")
        book_id = int(input("Pasirinkite norimos pridėti knygos ID\n"))
        book_instance = BookInstance(book_id)
        session.add(book_instance)
        session.commit()

    if option == 3:
        books = session.query(Book).all()
        print("-------------------")
        for book in books:
            print(book)
        print("-------------------")
        book_id = int(input("Įveskite norimos pasiskolinti knygos ID:\n"))
        our_book = session.query(Book).get(book_id)
        loan_book = session.query(BookInstance).filter_by(book_id=book_id, on_loan=False).first()
        if not loan_book:
            print("-------------------")
            print(f'Atsiprašome, nėra galimybes išduoti knygos {our_book}. Visos kopijos jau išdalintos.')
            print("-------------------")
        else:
            loan_book.on_loan = True
            print("-------------------")
            print(f'Jums ką tik paskolinta {our_book} kopija.')
            print("-------------------")
            session.commit()

    if option == 4:
        books = session.query(Book).all()
        print("-------------------")
        for book in books:
            print(book)
        print("-------------------")
        book_id = int(input("Įveskite norimos gražinti knygos ID:\n"))
        our_book = session.query(Book).get(book_id)
        return_book = session.query(BookInstance).filter_by(book_id=book_id, on_loan=True).first()
        if not return_book:
            print("-------------------")
            print(f'Atsiprašome, bet mes turime visas savo knygų kopijas. Jus turbūt atvykote ne į tą biblioteką.')
            print("-------------------")
        else:
            return_book.on_loan = False
            print("-------------------")
            print(f'Ačiū, kad gražinote {our_book} knygą.')
            print("-------------------")
            session.commit()

    if option == 5:
        search_text = input("Įveskite paieškos tekstą: ")
        search_books = session.query(Book).filter(Book.author.like('%' + search_text + '%') |
                                                          Book.title.like('%' + search_text + '%')).all()
        print("-------------------")
        for book in search_books:
            print(book)
        print("-------------------")
    if option == 6:
        print("-------------------")
        print("Viso Gero!")
        print("-------------------")
        break
