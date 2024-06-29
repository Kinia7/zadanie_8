from models import Quote
import sys

def search_by_author(name):
    quotes = Quote.objects(author__fullname=name)
    for quote in quotes:
        print(f'{quote.author.fullname}: {quote.quote}')

def search_by_tag(tag):
    quotes = Quote.objects(tags=tag)
    for quote in quotes:
        print(f'{quote.author.fullname}: {quote.quote}')

def search_by_tags(tags):
    tags_list = tags.split(',')
    quotes = Quote.objects(tags__in=tags_list)
    for quote in quotes:
        print(f'{quote.author.fullname}: {quote.quote}')

def main():
    while True:
        command = input('Enter command (name:, tag:, tags:, exit): ')
        if command.startswith('name:'):
            name = command[len('name:'):].strip()
            search_by_author(name)
        elif command.startswith('tag:'):
            tag = command[len('tag:'):].strip()
            search_by_tag(tag)
        elif command.startswith('tags:'):
            tags = command[len('tags:'):].strip()
            search_by_tags(tags)
        elif command == 'exit':
            sys.exit()
        else:
            print('Invalid command.')

if __name__ == '__main__':
    main()
