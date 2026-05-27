Here’s a solid **production-friendly CKEditor configuration** for Django that includes most useful tools (formatting, media, tables, links, code, etc.) and is commonly used in real projects.

---

## ✅ 1. Install (if not done yet)

```bash
pip install django-ckeditor
```

Add to `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    ...
    "ckeditor",
    "ckeditor_uploader",
]
```

---

## ✅ 2. Media settings (important for uploads)

```python
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"
```

---

## ✅ 3. CKEditor Config (FULL FEATURED)

Put this in `settings.py`:

```python
CKEDITOR_UPLOAD_PATH = "uploads/"

CKEDITOR_CONFIGS = {
    "default": {
        # ===== Toolbar (rich + practical) =====
        "toolbar": "Custom",
        "toolbar_Custom": [
            ["Bold", "Italic", "Underline", "Strike", "RemoveFormat"],
            ["Blockquote", "CodeSnippet"],
            ["NumberedList", "BulletedList", "Outdent", "Indent"],
            ["JustifyLeft", "JustifyCenter", "JustifyRight"],
            ["Link", "Unlink", "Anchor"],
            ["Image", "Table", "HorizontalRule", "SpecialChar"],
            ["Format", "Font", "FontSize"],
            ["TextColor", "BGColor"],
            ["Maximize", "ShowBlocks", "Source"],
            ["Undo", "Redo"],
        ],

        # ===== Features =====
        "height": 400,
        "width": "auto",
        "removePlugins": "stylesheetparser",
        "allowedContent": True,

        # ===== Extra plugins (important for modern editor use) =====
        "extraPlugins": ",".join([
            "uploadimage",      # image upload
            "image2",          # better image handling
            "codesnippet",     # code blocks
            "widget",
            "lineutils",
        ]),

        # ===== Code block styling =====
        "codeSnippet_theme": "monokai_sublime",

        # ===== File upload =====
        "filebrowserUploadUrl": "/ckeditor/upload/",
        "filebrowserBrowseUrl": "/ckeditor/browse/",

        # ===== UI improvements =====
        "uiColor": "#f8f9fa",
        "removeDialogTabs": "image:advanced;link:advanced",
    }
}
```

---

## ✅ 4. URLs setup

In `urls.py`:

```python
from django.urls import path, include

urlpatterns = [
    ...
    path("ckeditor/", include("ckeditor_uploader.urls")),
]
```

---

## ✅ 5. Model usage example

```python
from ckeditor_uploader.fields import RichTextUploadingField

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextUploadingField()
```

---

## 🚀 What this setup gives you

You get:

* Bold, italic, underline, strike
* Headings + font control
* Color picker
* Tables
* Image upload
* File upload support
* Code snippets (very useful for dev blogs)
* Alignment tools
* Lists + indentation
* Link tools
* Fullscreen editor mode
* Source code view (HTML editing)

---

## 🔥 Optional upgrades (if you want next level)

You can also add:

### 1. Auto image resizing

```python
"image2_alignClasses": ["image-align-left", "image-align-center", "image-align-right"],
```

### 2. Clipboard paste clean formatting

```python
"forcePasteAsPlainText": False,
```

### 3. Better security (recommended for production)

```python
"allowedContent": False,
```

---

If you want next step, I can also help you with:

* ✅ CKEditor image upload not working fix (very common issue)
* ✅ Custom toolbar design like Medium/Notion
* ✅ Integrating CKEditor with DRF API
* ✅ Deploying CKEditor in cPanel without broken uploads

Just tell me 👍
