# The Explainer guide by polymath
Modern backend systems must accept user-generated files.  
+ Documents(PDFs,  ZIPs,etc)
+ Images
+ Media

Files are fundamentally different from normal form data.  
+ They are `binary`
+ They can be `large`
+ They must be stored outside a db
+ They have security implications

Django provide tools to handle this correctly.  

---
## High-level Architecture
1. `Browser` - sends a multipart/`form-data`request
2. `URL routing` - maps a path to a `view`
3. `View` - orchestrates request handling
4. `Model` - stores files references in a database
5. `Storage` - writes file bytes into disk

The database never stores the file itself. It only stores a path string like:  
```python
files/report.pdf
```
The actual file lives on disk.  
```python
media/files/report.pdf
```
---

## Project & App structure
We use `django pillow` because django`s `ImageFiled` depends on Pillow.  

We separate concerns using Django`s app system.  
+ config/ - Project configuration
+ uploads/ - Files upload domain logic

## Media Configuration
`settings.py`.  
```python
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```
purpose:  
+ `MEDIA_ROOT` - where files are physically stored.  
+ `MEDIA_URL` - how files are accessed in the browser

## Development env media serving
```python
if settings.DEBUG:
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```
This is used in development env only for media serving.  
In production media is served by a CDN, Nginx, S3.  