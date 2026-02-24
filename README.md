# disify.py
Web-API for [disify.com](https://disify.com) website to validate and verify single email address. check if email address is disposable, temporary, has invalid MX records, detect if its mistyped, inactive or non-existent

## Example
```python
from disify import Disify

disify = Disify()
email_validation = disify.check_email(email="example@gmail.com")
print(email_validation)
```
