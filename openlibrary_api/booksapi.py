#   Imports
import requests
from urllib.parse import quote
import json

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
        self.__readbook_link: str = "/books/{}"
        self.__readbook_headers: dict[str, str] = {'accept: application/json'}
        
        # Read Isbn Requst API URL/Headers
        self.__readbookisbn_link: str = "/isbn/{}"
        self.__readbookisbn_headers: dict[str, str] = {'accept: application/json'}
        
        # Read Works Requst API URL/Headers
        self.__readwork_link: str = "/works/{}"
        self.__readwork_headers: dict[str, str] = {'accept: application/json'}
        
        # Search Requst API URL/Headers
        self.__search_link: str = "/search.json"
        self.__search_headers: dict[str, str] = {'accept: application/json'}
        
        # Search Authors Requst API URL/Headers
        self.__searchauthors_link: str = "/search/authors.json"
        self.__searchauthors_headers: dict[str, str] = {'accept: application/json'}
    
    def get_books_by_query(self, query: str) -> dict:
        query_encoded: str = quote(query)
        search_link: str = self.__api_link.format(self.__search_link)
        search_headers: str = self.__search_headers
        search_params: dict = {'q': query_encoded}
        response = self.__session.get(
            search_link,
            headers=search_headers,
            params=search_params
        )
        
        response_content: str = response.content
        response_dict: dict = json.loads(response_content)
        return response_dict
        
    def get_authors_by_query(self, query: str) -> dict:
        query_encoded: str = quote(query)
        search_link: str = self.__api_link.format(self.__searchauthors_link)
        search_headers: str = self.__searchauthors_headers
        search_params: dict = {'q': query_encoded}
        response = self.__session.get(
            search_link,
            headers=search_headers,
            params=search_params
        )
        
        response_content: str = response.content
        response_dict: dict = json.loads(response_content)
        return response_dict
    
    def get_book_by_olid(self, olid: str) -> dict:
        book_api_link: str = self.__readbook_link.format(olid)
        request_link: str = self.__api_link.format(book_api_link)
        request_headers: dict = self.__readbook_headers
        response = self.__session.get(
            request_link,
            headers=request_headers
        )
        
        response_content: str = response.content
        response_dict: dict = json.loads(response_content)
        return response_dict
    
    def get_book_by_isbn(self, isbn: str) -> dict:
        book_api_link: str = self.__readbookisbn_link.format(isbn)
        request_link: str = self.__api_link.format(book_api_link)
        request_headers: dict = self.__readbookisbn_headers
        response = self.__session.get(
            request_link,
            headers=request_headers
        )
        
        response_content: str = response.content
        response_dict: dict = json.loads(response_content)
        return response_dict

    def get_work_by_olid(self, olid: str) -> dict:
        work_api_link: str = self.__readwork_link.format(olid)
        request_link: str = self.__api_link.format(work_api_link)
        request_headers: dict = self.__readwork_headers
        response = self.__session.get(
            request_link,
            headers=request_headers
        )
        
        response_content: str = response.content
        response_dict: dict = json.loads(response_content)
        return response_dict
    
if __name__ == "__main__":
    pass