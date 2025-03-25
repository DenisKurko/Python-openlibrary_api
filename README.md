# OpenLibrary Python API

---

This client simplifies interaction with OpenLibrary’s public API. For full API documentation, see [OpenLibrary API Docs](https://openlibrary.org/developers/api). Project was created as training of Python skills.

# Table of contents

---

- [Installation](#Installation)
- [Quick Start](#QuickStart)
- [Documentation](#Documentation)
- [Usage Notes](#UsageNotes)
- [Thanks](#Thanks)

<h1 id=Installation> Installation !!! currently unavailable !!! </h1>

---

```powershell
pip install openlibrary_api
```

<h1 id=QuickStart> Quick start</h1>

---

```python
from openlibrary_api import API

# Initialize the API client
openlib_api = API(debug=True)  # Enable debug logging

# Fetch a book by ISBN
data, status_code = openlib_api.get_book_by_isbn("3548234100")  # 1984 by George Orwell

print(f"Title: {data['title']}")
print(f"Authors: {data['authors']}")
```

<h1 id=Documentation>Documentation</h1>

---

## Class Overview

```python
class API:
    def __init__(self, requests_session: requests.Session = False, debug: bool = False):
        # ... initialization logic ...
```

### Initialization

Creates an instance of the OpenLibrary API client.

**Parameters**:

- `requests_session` (Optional):
    
    An existing `requests.Session` object to use for HTTP requests. If not provided, a new session is created.
    
    Example use cases: Custom retry logic, proxy configuration, or connection pooling.
    
    **Default**: `False` (creates a new session).
    
- `debug` (`bool`):
    
    Enables debug logging. When `True`, method calls and response status codes are printed.
    
    **Default**: `False`.
    

---

## Methods

### `get_books_by_query(query: str) -> tuple[dict, int]`

Searches for books by a query string.

**Parameters**:

- `query` (`str`): The search term (e.g., "Harry Potter", "Science Fiction").

**Returns**:

- `tuple[dict, int]`:
    - `response_dict` (`dict`): JSON response.
    - `status_code` (`int`): HTTP status code of the response (e.g., `200`, `404`).

**Example Response Structure**:

```json
{
  "numFound": 3834,
  "start": 0,
  "numFoundExact": true,
  "num_found": 3834,
  "documentation_url": "https://openlibrary.org/dev/docs/api/search",
  "q": "Harry Potter",
  "offset": null,
  "docs": [
    {
      "author_key": [
        "OL23919A"
      ],
      "author_name": [
        "J. K. Rowling"
      ],
      "cover_edition_key": "OL22856696M",
      "cover_i": 10521270,
      "edition_count": 337,
      "first_publish_year": 1997,
      "has_fulltext": true,
      "ia": [
        "harrypotterylapi0000rowl_q5r6",...,"bdrc-W1KG14543"
      ],
      "ia_collection_s": ...,
      "key": "/works/OL82563W",
      "language": [
        "cze",...,"por"
      ],
      "lending_edition_s": "OL38565767M",
      "lending_identifier_s": "harrypotterylapi0000rowl_q5r6",
      "public_scan_b": false,
      "title": "Harry Potter and the Philosopher's Stone"
    },
    ...
```

---

### `get_authors_by_query(query: str) -> tuple[dict, int]`

Searches for authors by a query string.

**Parameters**:

- `query` (`str`): The search term (e.g., "J.K. Rowling", "Isaac Asimov").

**Returns**:

- `tuple[dict, int]`:
    - `response_dict` (`dict`): JSON response.
    - `status_code` (`int`): HTTP status code.

**Example Response Structure**:

```json
{
  "numFound": 3,
  "start": 0,
  "numFoundExact": true,
  "docs": [
    {
      "alternate_names": [
        "Joanne Rowling",
        ...
        "J. K. ROWLING"
      ],
      "birth_date": "31 July 1965",
      "key": "OL23919A",
      "name": "J. K. Rowling",
      "top_subjects": [
        "Children's fiction",
        ...
        "Juvenile fiction"
      ],
      "top_work": "Harry Potter and the Philosopher's Stone",
      "type": "author",
      "work_count": 411,
      "ratings_average": 4.21433,
      "ratings_sortable": 4.180542,
      "ratings_count": 3224,
      "ratings_count_1": 169,
      ...
      "ratings_count_5": 1776,
      "want_to_read_count": 35951,
      "already_read_count": 5692,
      "currently_reading_count": 2842,
      "readinglog_count": 44485,
      "_version_": 1821153508626268200
    }
  ]
}
```

---

### `get_book_by_olid(olid: str) -> tuple[dict, int]`

Retrieves a book by its OpenLibrary ID (OLID).

**Parameters**:

- `olid` (`str`): The OpenLibrary identifier (e.g., `"OL12345678M"`).

**Returns**:

- `tuple[dict, int]`:
    - `response_dict` (`dict`): Book details (title, authors, ISBN, etc.).
    - `status_code` (`int`): HTTP status code.

**Example Response**:

```json
{
  "publishers": [
    "Treaty Oak Map Distributers"
  ],
  "key": "/books/OL12345678M",
  "languages": [
    {
      "key": "/languages/eng"
    }
  ],
  "title": "Yucatan Road Map",
  "isbn_13": [
    "9783928855617"
  ],
  "covers": [
    3282975
  ],
  "physical_format": "Map",
  "isbn_10": [
    "3928855611"
  ],
  "publish_date": "June 30, 1996",
  "last_modified": {
    "type": "/type/datetime",
    "value": "2010-04-13T09:09:14.289385"
  },
  "authors": [
    {
      "key": "/authors/OL2940426A"
    }
  ],
  "latest_revision": 3,
  "works": [
    {
      "key": "/works/OL8692072W"
    }
  ],
  "type": {
    "key": "/type/edition"
  },
  "subjects": [
    "General",
    "Maps, charts & atlases",
    "Mexico",
    "Travel / road maps & atlases",
    "Reference",
    "Maps",
    "Yucatan",
    "Travel - Foreign"
  ],
  "revision": 3
}
```

---

### `get_book_by_isbn(isbn: str) -> tuple[dict, int]`

Retrieves a book by its ISBN.

**Parameters**:

- `isbn` (`str`): The 10- or 13-digit ISBN (e.g., `"9780747542988"`).

**Returns**:

- `tuple[dict, int]`:
    - `response_dict` (`dict`): Book details.
    - `status_code` (`int`): HTTP status code.

---

### `get_work_by_olid(olid: str) -> tuple[dict, int]`

Retrieves a work by its OpenLibrary ID (OLID). A "work" represents a conceptual entity (e.g., all editions of "1984").

**Parameters**:

- `olid` (`str`): The OpenLibrary work ID (e.g., `"OL22856696M"`).

**Returns**:

- `tuple[dict, int]`:
    - `response_dict` (`dict`): Work metadata, including editions, descriptions, and links.
    - `status_code` (`int`): HTTP status code.

**Example Responses**:

```json
{
  "identifiers": {
    "alibris_id": [
      "9780747542988"
    ],
    "google": [
      "795qQgAACAAJ"
    ],
    "librarything": [
      "5403381"
    ],
    "goodreads": [
      "56073094"
    ]
  },
  "series": [
    "Harry Potter #1"
  ],
  "covers": [
    14362634,
    10521270,
    -1
  ],
  "languages": [
    {
      "key": "/languages/eng"
    }
  ],
  "genres": [
    "Juvenile fiction",
    "Juvenile fiction."
  ],
  "source_records": [
    "marc:wfm_bk_marc/wfm_bk_marc:376490528:1276",
    "bwb:9780747542988"
  ],
  "title": "Harry Potter and the Sorcerer's Stone",
  "edition_name": "printing (2)",
  "subjects": [
    ...
    "England -- Juvenile fiction"
  ],
  "publish_country": "enk",
  "by_statement": "J. K. Rowling.",
  "type": {
    "key": "/type/edition"
  },
  "location": [
    "NBuC"
  ],
  "publishers": [
    "Bloomsbury"
  ],
  "description": ...,
  "physical_format": "Paperback",
  "key": "/books/OL22856696M",
  "authors": [
    {
      "key": "/authors/OL23919A"
    }
  ],
  "publish_places": [
    "London, England"
  ],
  "oclc_number": [
    "41534303"
  ],
  "pagination": "223 p. ;",
  "classifications": {},
  "notes": "Sequel: Harry Potter and the Chamber of Secrets\r\nBloomsbury Paperbacks UK",
  "number_of_pages": 223,
  "publish_date": "1998",
  "copyright_date": "2023",
  "works": [
    {
      "key": "/works/OL82563W"
    }
  ],
  ...
  ],
  "latest_revision": 28,
  "revision": 28,
  "created": {
    "type": "/type/datetime",
    "value": "2009-01-07T23:46:06.178276"
  },
  "last_modified": {
    "type": "/type/datetime",
    "value": "2023-07-17T06:59:49.622159"
  }
}
```

---

<h2 id=UsageNotes>Usage Notes</h2>

### Debug Mode

When `debug=True` is set during initialization, all method calls log:

1. The method name and arguments.
2. The HTTP status code of the response.

**Example Output**:

```
Calling get_books_by_query with args: ("Harry Potter",) and kwargs: {}
Response: get_books_by_query ("Harry Potter",) with status code: 200
```

### Error Handling

- Check the `status_code` in the returned tuple to verify successful requests.
- A `200` status indicates success. Non-`200` codes (e.g., `404`, `500`) indicate errors.

### Rate Limits and Sessions

- To customize HTTP behavior (retries, timeouts, proxies), pass a pre-configured `requests.Session` to `requests_session`.
- OpenLibrary may enforce rate limits; ensure your implementation respects them.

---

<h1 id=Thanks>Thanks</h1>

---

to all who supported this project. Your opinion and advice are very important to me. I do not plan to abandon this package and will continue to support it with your help and support.

07 and Glory to Mankind
