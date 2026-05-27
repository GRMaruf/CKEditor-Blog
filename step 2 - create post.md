

Perfect next step.

Now you'll learn:

* Django `ModelForm`
* Handling POST requests
* File uploads
* CSRF protection
* Validation
* Saving database objects
* Frontend CRUD basics

We’ll create:

```text
/create-post/
```

where users can submit blog posts directly from the frontend.

---

# Step 1 — Create Form

## `blog/forms.py`

```python
from django import forms
from .models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'thumbnail', 'content']
```

---

# Step 2 — Create View

## `blog/views.py`

Add imports:

```python
from .forms import PostForm
from django.shortcuts import redirect
```

Now add:

```python
def create_post(request):

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()

            return redirect('home')

    else:
        form = PostForm()

    return render(request, 'blog/create_post.html', {
        'form': form
    })
```

---

# Understanding This

## `request.POST`

Contains normal form data.

---

## `request.FILES`

Contains uploaded images/files.

Without this:

```python
request.FILES
```

your image upload will fail.

---

## `form.is_valid()`

Checks:

* required fields
* image validity
* field lengths
* form errors

---

## `form.save()`

Creates the database object automatically.

Equivalent to:

```python
Post.objects.create(...)
```

---

# Step 3 — Add URL

## `blog/urls.py`

```python
path('create-post/', views.create_post, name='create_post'),
```

Full file:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post/<int:id>/', views.post_detail, name='post_detail'),
    path('create-post/', views.create_post, name='create_post'),
]
```

---

# Step 4 — Create Template

## `templates/blog/create_post.html`

```html
<!DOCTYPE html>
<html>
<head>
    <title>Create Post</title>
</head>
<body>

<h1>Create Post</h1>

<form method="POST" enctype="multipart/form-data">

    {% csrf_token %}

    {{ form.as_p }}

    <button type="submit">
        Publish
    </button>

</form>

</body>
</html>
```

---

# VERY IMPORTANT

## Why `enctype="multipart/form-data"`?

Without it:

* image uploads DO NOT work

Always use it when uploading files.

---

# Step 5 — Test It

Run server:

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/create-post/
```

Try:

* title
* image upload
* rich text formatting
* links
* headings
* tables

Submit → redirected to homepage.

---

# Improve Form Styling

Default Django forms look ugly.

Add Bootstrap CDN:

```html
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.7/dist/css/bootstrap.min.css" rel="stylesheet">
```

Then:

```html
<div class="container mt-5">

    <form method="POST" enctype="multipart/form-data">

        {% csrf_token %}

        {{ form.as_p }}

        <button class="btn btn-dark">
            Publish
        </button>

    </form>

</div>
```

---

# Better Form Rendering

Instead of:

```html
{{ form.as_p }}
```

render fields manually.

Example:

```html
<div>
    <label>Title</label>
    {{ form.title }}
</div>
```

This gives full design control.

---

# Add Bootstrap Classes to Fields

## `forms.py`

```python
class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'thumbnail', 'content']

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control'
            }),
        }
```

---

# Important Security Note

This:

```python
{{ post.content|safe }}
```

renders HTML directly.

Rich text editors generate trusted HTML, but later you should learn sanitization using:

* `bleach`
* allowed tags
* allowed attributes

because unsafe HTML can create XSS vulnerabilities.

---

# What You Learned

You now understand:

| Concept         | Meaning                    |
| --------------- | -------------------------- |
| ModelForm       | Generate forms from models |
| POST request    | Submitting data            |
| FILE uploads    | Image handling             |
| CSRF token      | Request security           |
| Form validation | Prevent bad input          |
| Redirects       | Navigation after submit    |
| Frontend CRUD   | User-generated content     |

---

# Next Best Step

After this, build:

1. Edit post
2. Delete post
3. Login-required posting
4. User-specific posts
5. Rich text image uploads
6. Slug URLs
7. Pagination

The next major learning milestone is usually:

```text
UpdateView + DeleteView
```

because that completes CRUD.
