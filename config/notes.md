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

## Data Models: Representing Files Correctly

**File Model**:  
```python
class UploadFile(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='files/')
    upload_at = models.DateTimeField(auto_now_add=True)
```
Key Points:  
+ `FileField` stores paths, not files
+ `upload_to` defines a subdirectory under `MEDIA_ROOT`
+ The database row references the file location


**Image Model:**
```python
class UploadImage(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')

```
Key points:  
+ Images have additional validation
+ Pillow verifies dimensions and format

---

## Admin: Verifying the Pipeline Early
We registered models in the admin panel to:  
+ Verify uploads without writing UI
+ Confirm file paths are correct
+ Debug storage issues early

Admin is `a diagnostic tool` not a user interface.  

---

## Forms: The Validation Layer

```python
class FileUploadForm(forms.ModelForm):
    class Meta:
        model = UploadFile
        fields = ['title','file']
```
Why forms matter:  
+ They validate file presence
+ They enforce required field
+ They protect against against malformed input

Forms are the boundary between user input and our models.  

---

## Views: Orchestrating the Upload
```python
if request.method == 'POST':
    form = FileUploadForm(request.POST, request.FILES)

```
This view:  
+ Receives input 
+ Delegates validation to the form
+ Saves only if valid

## URL Design:
We used a 2-level routing strategy.  

Project-level(prefix):  
```python
path('upload', include('uploads.urls'))

```
App-level(endpoints):   
```python
path('file/', views.upload_file_view)

```
Resulting URL:  
```python
/upload/file
```

