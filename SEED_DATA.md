# Poblar la base de datos — Autores y Libros

## Cómo acceder al admin de Django

1. Asegúrate de tener el servidor corriendo:
   ```
   python manage.py runserver
   ```
2. Ve a `http://127.0.0.1:8000/admin/`
3. Inicia sesión con tu superusuario.

> Si aún no tienes los modelos registrados en el admin, agrega esto a `quotes/admin.py`:
> ```python
> from django.contrib import admin
> from .models import Author, Book
>
> admin.site.register(Author)
> admin.site.register(Book)
> ```

---

## Alternativa: Django Shell

```bash
python manage.py shell
```

```python
from quotes.models import Author, Book

# Crear un autor
a = Author.objects.create(
    name="Gabriel García Márquez",
    email="gabo@example.com",
    birth_date="1927-03-06"
)

# Crear un libro asociado
Book.objects.create(title="Cien años de soledad", author=a, isbn="978-0-06-088328-7", publication_date="1967-05-30")
```

---

## Autores sugeridos

| name | email | birth_date |
|------|-------|------------|
| Gabriel García Márquez | gabo@example.com | 1927-03-06 |
| Jorge Luis Borges | borges@example.com | 1899-08-24 |
| Isabel Allende | allende@example.com | 1942-08-02 |
| Octavio Paz | opaz@example.com | 1914-03-31 |
| Mario Vargas Llosa | vargas@example.com | 1936-03-28 |
| Ernest Hemingway | hemingway@example.com | 1899-07-21 |
| George Orwell | orwell@example.com | 1903-06-25 |
| Franz Kafka | kafka@example.com | 1883-07-03 |
| Fyodor Dostoevsky | dostoevsky@example.com | 1821-11-11 |
| Virginia Woolf | woolf@example.com | 1882-01-25 |

---

## Libros sugeridos (por autor)

### Gabriel García Márquez
| title | isbn | publication_date |
|-------|------|-----------------|
| Cien años de soledad | 978-0-06-088328-7 | 1967-05-30 |
| El amor en los tiempos del cólera | 978-0-14-303943-3 | 1985-09-05 |
| El coronel no tiene quien le escriba | 978-0-06-112009-3 | 1961-01-01 |

### Jorge Luis Borges
| title | isbn | publication_date |
|-------|------|-----------------|
| Ficciones | 978-0-8021-3030-0 | 1944-01-01 |
| El Aleph | 978-0-14-028680-4 | 1949-01-01 |
| Laberintos | 978-0-8112-0012-8 | 1962-01-01 |

### Isabel Allende
| title | isbn | publication_date |
|-------|------|-----------------|
| La casa de los espíritus | 978-1-5011-2099-2 | 1982-10-01 |
| Eva Luna | 978-0-553-38329-8 | 1987-01-01 |

### George Orwell
| title | isbn | publication_date |
|-------|------|-----------------|
| 1984 | 978-0-452-28423-4 | 1949-06-08 |
| Rebelión en la granja | 978-0-452-28424-1 | 1945-08-17 |

### Franz Kafka
| title | isbn | publication_date |
|-------|------|-----------------|
| La metamorfosis | 978-0-553-21369-7 | 1915-10-15 |
| El proceso | 978-0-805-21040-3 | 1925-01-01 |
| El castillo | 978-0-805-21044-1 | 1926-01-01 |

### Ernest Hemingway
| title | isbn | publication_date |
|-------|------|-----------------|
| El viejo y el mar | 978-0-684-80122-3 | 1952-09-01 |
| Por quién doblan las campanas | 978-0-684-80335-7 | 1940-10-21 |

### Fyodor Dostoevsky
| title | isbn | publication_date |
|-------|------|-----------------|
| Crimen y castigo | 978-0-14-044913-6 | 1866-01-01 |
| El idiota | 978-0-14-044792-7 | 1869-01-01 |
| Los hermanos Karamazov | 978-0-374-52837-0 | 1880-11-01 |

---

## Script completo para poblar todo de una vez

Guarda esto como `seed.py` en la raíz del proyecto y ejecuta `python manage.py shell < seed.py`:

```python
from quotes.models import Author, Book

data = [
    {
        "author": {"name": "Gabriel García Márquez", "email": "gabo@example.com", "birth_date": "1927-03-06"},
        "books": [
            {"title": "Cien años de soledad", "isbn": "978-0-06-088328-7", "publication_date": "1967-05-30"},
            {"title": "El amor en los tiempos del cólera", "isbn": "978-0-14-303943-3", "publication_date": "1985-09-05"},
        ],
    },
    {
        "author": {"name": "Jorge Luis Borges", "email": "borges@example.com", "birth_date": "1899-08-24"},
        "books": [
            {"title": "Ficciones", "isbn": "978-0-8021-3030-0", "publication_date": "1944-01-01"},
            {"title": "El Aleph", "isbn": "978-0-14-028680-4", "publication_date": "1949-01-01"},
        ],
    },
    {
        "author": {"name": "Isabel Allende", "email": "allende@example.com", "birth_date": "1942-08-02"},
        "books": [
            {"title": "La casa de los espíritus", "isbn": "978-1-5011-2099-2", "publication_date": "1982-10-01"},
            {"title": "Eva Luna", "isbn": "978-0-553-38329-8", "publication_date": "1987-01-01"},
        ],
    },
    {
        "author": {"name": "George Orwell", "email": "orwell@example.com", "birth_date": "1903-06-25"},
        "books": [
            {"title": "1984", "isbn": "978-0-452-28423-4", "publication_date": "1949-06-08"},
            {"title": "Rebelión en la granja", "isbn": "978-0-452-28424-1", "publication_date": "1945-08-17"},
        ],
    },
    {
        "author": {"name": "Franz Kafka", "email": "kafka@example.com", "birth_date": "1883-07-03"},
        "books": [
            {"title": "La metamorfosis", "isbn": "978-0-553-21369-7", "publication_date": "1915-10-15"},
            {"title": "El proceso", "isbn": "978-0-805-21040-3", "publication_date": "1925-01-01"},
        ],
    },
    {
        "author": {"name": "Fyodor Dostoevsky", "email": "dostoevsky@example.com", "birth_date": "1821-11-11"},
        "books": [
            {"title": "Crimen y castigo", "isbn": "978-0-14-044913-6", "publication_date": "1866-01-01"},
            {"title": "Los hermanos Karamazov", "isbn": "978-0-374-52837-0", "publication_date": "1880-11-01"},
        ],
    },
]

for entry in data:
    author = Author.objects.create(**entry["author"])
    for book in entry["books"]:
        Book.objects.create(author=author, **book)
    print(f"Creado: {author.name} con {len(entry['books'])} libro(s)")
```
