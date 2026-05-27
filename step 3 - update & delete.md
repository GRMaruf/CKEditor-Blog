Perfect.
Now you’ll complete the core CRUD cycle:

| Operation | Django Feature    |
| --------- | ----------------- |
| Create    | `CreateView`      |
| Read      | Detail/List views |
| Update    | `UpdateView`      |
| Delete    | `DeleteView`      |

These are Django **class-based generic views**.

---

# What We’ll Build

## Edit Post

```text id="k79aef"
/post/1/update/
```

## Delete Post

```text id="4gaw19"
/post/1/delete/
```

---

# Step 1 — Import Generic Views

## `views.py`

```python id="ewmqmr"
from django.views.generic import UpdateView, DeleteView
from django.urls import reverse_lazy
```

---

# Step 2 — Create UpdateView

## `views.py`

```python id="0mkq4x"
class PostUpdateView(UpdateView):

    model = Post
    fields = ['title', 'thumbnail', 'content']

    template_name = 'blog/update_post.html'

    success_url = reverse_lazy('home')
```

---

# Understanding This

## `model`

Which model to edit.

---

## `fields`

Fields shown in the form.

---

## `template_name`

HTML template used.

---

## `success_url`

Where to redirect after successful update.

We use:

```python id="trxyqb"
reverse_lazy()
```

because class-based views load before URL configs are fully ready.

---

# Step 3 — Create DeleteView

## `views.py`

```python id="mzt0lh"
class PostDeleteView(DeleteView):

    model = Post

    template_name = 'blog/delete_post.html'

    success_url = reverse_lazy('home')
```

---

# Step 4 — Add URLs

## `blog/urls.py`

```python id="iw0pk8"
path(
    'post/<int:pk>/update/',
    views.PostUpdateView.as_view(),
    name='update_post'
),

path(
    'post/<int:pk>/delete/',
    views.PostDeleteView.as_view(),
    name='delete_post'
),
```

---

# IMPORTANT

Class-based views use:

```text id="0v5s0h"
pk
```

NOT:

```text id="bmrth3"
id
```

because Django generic views expect:

```python id="f3hiyg"
self.kwargs['pk']
```

internally.

---

# Step 5 — Update Template

## `update_post.html`

```html id="j89e3l"
<!DOCTYPE html>
<html>
<head>
    <title>Update Post</title>

    {{ form.media }}
</head>
<body>

<h1>Update Post</h1>

<form method="POST" enctype="multipart/form-data">

    {% csrf_token %}

    {{ form.as_p }}

    <button type="submit">
        Update
    </button>

</form>

</body>
</html>
```

---

# Step 6 — Delete Confirmation Template

## `delete_post.html`

```html id="fuvd0x"
<!DOCTYPE html>
<html>
<head>
    <title>Delete Post</title>
</head>
<body>

<h1>Delete Post</h1>

<p>
    Are you sure you want to delete:
    <strong>{{ object.title }}</strong> ?
</p>

<form method="POST">

    {% csrf_token %}

    <button type="submit">
        Yes, Delete
    </button>

</form>

</body>
</html>
```

---

# Step 7 — Add Buttons

## `post_detail.html`

```html id="as6ixv"
<a href="{% url 'update_post' post.id %}">
    Edit
</a>

<a href="{% url 'delete_post' post.id %}">
    Delete
</a>
```

---

# Why `post.id` Works With `pk`

Because:

```python id="vby0lc"
pk == primary key
```

and Django’s default primary key is:

```python id="lk0dd3"
id
```

So these are effectively the same unless you customize the primary key.

---

# What You Just Learned

You now know:

| Concept        | Meaning                          |
| -------------- | -------------------------------- |
| Generic Views  | Prebuilt CRUD views              |
| UpdateView     | Edit existing objects            |
| DeleteView     | Remove objects                   |
| `pk`           | Object identifier                |
| `reverse_lazy` | Lazy URL reversing               |
| `as_view()`    | Convert class into callable view |

---

# HUGE Django Milestone

You can now build:

* blogs
* portfolio CMS
* dashboards
* admin panels
* note systems
* expense trackers
* task managers

because you now understand the entire CRUD workflow.

---

# Next Important Step

The next real-world improvement is:

## Restrict Editing/Deleting

Currently:

```text id="d3s18r"
ANYONE can edit/delete ANY post
```

Next you should learn:

* `LoginRequiredMixin`
* `UserPassesTestMixin`
* associating posts with users

Example:

```python id="x42q3o"
post.author == request.user
```

That’s where Django apps start feeling real and production-like.
