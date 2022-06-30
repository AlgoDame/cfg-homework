-- Question 8
-- Since the authors dataset and books dataset both contain 1M+ rows, I will create an index on the
--author_name column of the Authors table
-- and create another index on the book_name column of the Books table.

CREATE INDEX idx_author
ON Authors (author_name);

CREATE INDEX idx_book
ON Books (book_name);

