#   Imports
import requests
from urllib.parse import quote

class API():
    def __init__(self, requests_session: requests.Session = False):
        # In case usage of custom Retry, Proxy etcetera
        if requests_session:
            self.__session: requests.Session = requests_session
        else:
            self.__session: requests.Session = requests.Session()
            
        # API link
        self.__api_link: str = "https://openlibrary.org{}"
        
        # Read Books Requst API URL/Headers
        self.__readbooks_link: str = "/books/{}"
        self.__readbooks_headers: dict[str, str] = {'accept: application/json'}
        
        # Read Isbn Requst API URL/Headers
        self.__readisbn_link: str = "/isbn/{}"
        self.__readisbn_headers: dict[str, str] = {'accept: application/json'}
        
        # Read Works Requst API URL/Headers
        self.__readworks_link: str = "/works/{}"
        self.__readworks_headers: dict[str, str] = {'accept: application/json'}
        
        # Search Requst API URL/Headers
        self.__search_link: str = "/search.json"
        self.__search_headers: dict[str, str] = {'accept: application/json'}
        
        # Search Authors Requst API URL/Headers
        self.__searchauthors_link: str = "/search/authors.json"
        self.__searchauthors_headers: dict[str, str] = {'accept: application/json'}
    
    def get_books_by_query(self, query: str):
        pass
    
    def get_authors_by_query(self, olid: int):
        pass
    
    def get_book_by_olid(self, olid: int):
        pass
    
    def get_book_by_isbn(self, olid: int):
        pass
    
    
if __name__ == "__main__":
    pass