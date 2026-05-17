import re 
with open('settings.py', 'r') as f: 
    content = f.read() 
 
# Replace default SQLite with PostgreSQL 
    'default': { 
        'ENGINE': 'django.db.backends.postgresql', 
        'NAME': 'bscs_zs21_db', 
        'USER': 'postgres', 
        'PASSWORD': 'postgres', 
        'HOST': 'localhost', 
        'PORT': '5432', 
    } 
 
# Find and replace DATABASES section 
pattern = r'DATABASES = \{[}]+\}[}]*\}[}]*\}' 
content = re.sub(pattern, db_config, content, flags=re.DOTALL) 
 
with open('settings.py', 'w') as f: 
    f.write(content) 
print("Database configuration updated to PostgreSQL") 
