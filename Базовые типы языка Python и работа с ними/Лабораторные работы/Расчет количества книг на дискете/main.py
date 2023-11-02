floppy_capacity_megabytes = 1.44

pages = 100
lines_per_page = 50
symbols_per_line = 25
bytes_per_symbol = 4

floppy_capacity_bytes = floppy_capacity_megabytes * 1024 * 1024
bytes_per_book = bytes_per_symbol * symbols_per_line * lines_per_page * pages
book_numbers = int(floppy_capacity_bytes / bytes_per_book)

# TODO Найдите количество книг, которое можно разместить на дискете

print("Количество книг, помещающихся на дискету:", book_numbers)
