class Author:
    def __init__(self, name):
        self.name = name
        self.books = []

    def __str__(self):
        titles = ', '.join(self.books) or 'no books'
        return f'{self.name} has published {titles}.'

    def publish(self,title):
        if title in self.books: # to avoid duplicates, check if title already in self.books aray
            print('That book is already linked to the author')
        else:
            self.books.append(title)

def main():
    christie = Author('Agatha Christie')
    christie.publish('Death on the Nile')
    christie.publish('The Murder of Roger Ackroyd')
    christie.publish('The ABC Murders')
    christie.publish('Death on the Nile') #need to avoid publishing this one
    print(christie) #print the object using the __str__  method

    tempas = Author('Sierra Tempas')
    print(tempas)

main()  #call main fx