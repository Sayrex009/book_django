from rest_framework.decorators import api_view
from rest_framework.response import Response
from app.models import Book, Author, Category, Comment, User

@api_view()
def get_book_list(request):
    books = []
    for book in Book.objects.all():
        books.append({
            "id": book.id,
            "title": book.title,
            "descriptions": book.descriptions,
            "img": book.img.url if book.img else None,
            "author": book.author.full_name if book.author else None,
            "category": book.category.name if book.category else None,
        })
    return Response(books)


@api_view()
def get_author_list(request):
    authors = []
    for author in Author.objects.all():
        authors.append({
            "id": author.id,
            "full_name": author.full_name,
            "descriptions": author.descriptions,
        })
    return Response(authors)


@api_view()
def get_category_list(request):
    categories = []
    for category in Category.objects.all():
        categories.append({
            "id": category.id,
            "name": category.name,
            "descriptions": category.descriptions,
        })
    return Response(categories)


@api_view()
def get_comment_list(request):
    comments = []
    for comment in Comment.objects.all():
        comments.append({
            "id": comment.id,
            "rating": comment.rating,
            "descriptions": comment.descriptions,
            "book": comment.book.title if comment.book else None,
            "user": comment.user.full_name if comment.user else None,
        })
    return Response(comments)


@api_view()
def get_user_list(request):
    users = []
    for user in User.objects.all():
        users.append({
            "id": user.id,
            "full_name": user.full_name,
            "visited_at": user.visited_at,
            "descriptions": user.descriptions,
            "img": user.img.url if user.img else None,
            "website_with": user.website_with,
        })
    return Response(users)
