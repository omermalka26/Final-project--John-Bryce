# התקנת MySQL מקומי

## שלב 1: הורדת MySQL
1. לך לאתר: https://dev.mysql.com/downloads/mysql/
2. בחר "MySQL Community Server"
3. הורד את הגרסה המתאימה ל-Windows

## שלב 2: התקנה
1. הרץ את קובץ ההתקנה
2. בחר "Developer Default" או "Server only"
3. הגדר סיסמה ל-root
4. הפעל את השירות

## שלב 3: יצירת מסד נתונים
```sql
CREATE DATABASE vacationdb;
CREATE USER 'vacationuser'@'localhost' IDENTIFIED BY 'vacationpass';
GRANT ALL PRIVILEGES ON vacationdb.* TO 'vacationuser'@'localhost';
FLUSH PRIVILEGES;
```

## שלב 4: עדכון קובץ database.py
```python
class DatabaseConfig:
    def __init__(self):
        self.host = 'localhost'  # במקום 'mysql'
        self.port = 3306
        self.database = 'vacationdb'
        self.user = 'vacationuser'
        self.password = 'vacationpass'
```

## שלב 5: הפעלת הפרויקט
```bash
cd vite-backend
python setup_database.py
python app.py
```

## שלב 6: התחברות למסד הנתונים
```bash
mysql -u vacationuser -p vacationdb
```






