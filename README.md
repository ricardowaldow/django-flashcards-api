# Flashcards API

## 📋 Requisitos
- Python 3.8+
- pip

## 🚀 Instalação e Configuração

### 1. Criar ambiente virtual e instalar dependências

```bash
# Criar ambiente virtual
python -m venv venv

# Ativar ambiente virtual
# No Windows:
venv\Scripts\activate
# No Linux/Mac:
source venv/bin/activate

# Instalar dependências
pip install django djangorestframework
```

### 2. Criar o projeto Django

```bash
# Criar projeto
django-admin startproject flashcards_project .

# Criar app
python manage.py startapp flashcards
```

### 3. Configurar o projeto

Adicione ao `settings.py`:
- `'rest_framework'` em `INSTALLED_APPS`
- `'flashcards'` em `INSTALLED_APPS`
- Configure `REST_FRAMEWORK` (veja arquivo settings.py)

Configure o `urls.py` principal:
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('flashcards.urls')),
]
```

### 4. Aplicar migrações

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Criar superusuário (opcional)

```bash
python manage.py createsuperuser
```

### 6. Rodar o servidor

```bash
python manage.py runserver
```

## 📡 Endpoints da API

### Decks

- **GET** `/api/decks/` - Listar todos os decks
- **POST** `/api/decks/` - Criar novo deck
- **GET** `/api/decks/{id}/` - Detalhes de um deck
- **PUT** `/api/decks/{id}/` - Atualizar deck completo
- **PATCH** `/api/decks/{id}/` - Atualizar deck parcial
- **DELETE** `/api/decks/{id}/` - Deletar deck
- **GET** `/api/decks/{id}/cards/` - Listar cards de um deck

### Cards

- **GET** `/api/cards/` - Listar todos os cards
- **GET** `/api/cards/?deck={deck_id}` - Filtrar cards por deck
- **POST** `/api/cards/` - Criar novo card
- **GET** `/api/cards/{id}/` - Detalhes de um card
- **PUT** `/api/cards/{id}/` - Atualizar card completo
- **PATCH** `/api/cards/{id}/` - Atualizar card parcial
- **DELETE** `/api/cards/{id}/` - Deletar card

## 💡 Exemplos de Uso

### Criar um Deck

```bash
curl -X POST http://localhost:8000/api/decks/ \
  -H "Content-Type: application/json" \
  -d '{"name": "Vocabulário de Alemão"}'
```

### Criar um Card

```bash
curl -X POST http://localhost:8000/api/cards/ \
  -H "Content-Type: application/json" \
  -d '{
    "deck": 1,
    "front": "Hallo",
    "back": "Olá"
  }'
```

### Listar Decks

```bash
curl http://localhost:8000/api/decks/
```

### Listar Cards de um Deck

```bash
curl http://localhost:8000/api/decks/1/cards/
```

ou

```bash
curl http://localhost:8000/api/cards/?deck=1
```

## 📝 Formato das Respostas

### Deck
```json
{
  "id": 1,
  "name": "Vocabulário de Alemão",
  "cards_count": 5,
  "cards": [...],
  "created_at": "2025-11-05T10:30:00Z",
  "updated_at": "2025-11-05T10:30:00Z"
}
```

### Card
```json
{
  "id": 1,
  "deck": 1,
  "front": "Hallo",
  "back": "Olá",
  "created_at": "2025-11-05T10:30:00Z",
  "updated_at": "2025-11-05T10:30:00Z"
}
```

## 🌐 Interface Navegável

Acesse `http://localhost:8000/api/` no navegador para usar a interface navegável do Django REST Framework.