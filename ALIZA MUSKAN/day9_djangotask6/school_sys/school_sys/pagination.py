from rest_framework.pagination import PageNumberPagination

class ProductPagination(PageNumberPagination):
    """
    Custom Pagination Class for product ony
    Controls:
    - Default page size
    - User-defined page size
    - Max page size limit
    """
    # Default number of items per page
    page_size = 5
    # Allow user to override page size using query param
    page_size_query_param = 'page_size'
    # Maximum allowed page size
    max_page_size = 20