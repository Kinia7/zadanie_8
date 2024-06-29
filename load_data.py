import json
from models import Author, Quote

# Load authors
with open('authors.json', 'r') as file:
    authors_data = json.load(file)
    for item in authors_data:
        author = Author(
            fullname=item['fullname'],
            born_date=item.get('born_date', ''),
            born_location=item.get('born_location', ''),
            description=item.get('description', '')
        )
        author.save()

# Load quotes
with open('quotes.json', 'r') as file:
    quotes_data = json.load(file)
    for item in quotes_data:
        author = Author.objects(fullname=item['author']).first()
        if author:
            quote = Quote(
                tags=item['tags'],
                author=author,
                quote=item['quote']
            )
            quote.save()
