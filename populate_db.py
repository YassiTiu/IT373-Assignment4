import os
import django
from datetime import date

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mainsite.settings')
django.setup()

from mainapp.models import Author, Category, Book

# Clear existing data (optional)
Author.objects.all().delete()
Category.objects.all().delete()
Book.objects.all().delete()

# Create Authors
author1 = Author.objects.create(name="George R. R. Martin")
author2 = Author.objects.create(name="J.K. Rowling")
author3 = Author.objects.create(name="J.R.R. Tolkien")

print("✅ Created 3 Authors")

# Create Categories
category1 = Category.objects.create(
    name="Fantasy",
    description="Magical worlds and epic adventures filled with wizards, dragons, and enchantments."
)
category2 = Category.objects.create(
    name="Adventure",
    description="Thrilling journeys and quests that take you to extraordinary places."
)
category3 = Category.objects.create(
    name="Fiction",
    description="Creative stories and narratives from imaginative minds."
)

print("✅ Created 3 Categories")

# Create Books
book1 = Book.objects.create(
    title="A Game of Thrones",
    author=author1,
    published=date(1996, 8, 1),
    isbn="978-0-553-10354-1",
    pages=694,
    description="The first novel of the epic fantasy series 'A Song of Ice and Fire'. "
                "In a land where summers can last decades and winters a lifetime, "
                "trouble is brewing. War and intrigue await in the Seven Kingdoms of Westeros."
)
book1.categories.set([category1, category2, category3])

book2 = Book.objects.create(
    title="Harry Potter and the Philosopher's Stone",
    author=author2,
    published=date(1997, 6, 26),
    isbn="978-0-747-53269-9",
    pages=223,
    description="The magical tale of a young wizard named Harry Potter who discovers he is famous "
                "in the wizarding world. He attends Hogwarts School of Witchcraft and Wizardry "
                "where he makes friends and discovers his true potential."
)
book2.categories.set([category1, category3])

book3 = Book.objects.create(
    title="The Lord of the Rings: The Fellowship of the Ring",
    author=author3,
    published=date(1954, 7, 29),
    isbn="978-0-544-93427-5",
    pages=423,
    description="The epic fantasy masterpiece that started it all. Frodo inherits a magic ring "
                "from his uncle, only to learn that it is an instrument of terrible power. "
                "He must embark on a dangerous quest to destroy it."
)
book3.categories.set([category1, category2])

print("✅ Created 3 Books")
print("\n🎉 Database populated successfully!")
print(f"\nSummary:")
print(f"  • Authors: {Author.objects.count()}")
print(f"  • Categories: {Category.objects.count()}")
print(f"  • Books: {Book.objects.count()}")
