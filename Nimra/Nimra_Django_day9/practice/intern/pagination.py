from rest_framework.pagination import PageNumberPagination

class CustomPagination(PageNumberPagination):
    page_size = 3   # ✅ har page par 3 records
    page_size_query_param = 'page_size'  # user URL me ?page_size=10 likh kar override kar sakta hai
    max_page_size = 100
