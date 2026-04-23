import sqlite3
        
def backup_db(source_db_path, target_db_path):
    try:
        # الاتصال بقاعدة البيانات المصدر (الموجودة حالياً)
        source = sqlite3.connect(source_db_path)
        # الاتصال بقاعدة البيانات الهدف (سيتم إنشاؤها إذا لم تكن موجودة)
        dest = sqlite3.connect(target_db_path)
        
        print("جاري بدء عملية النسخ الاحتياطي...")
        
        with dest:
            source.backup(dest)
            
        print(f"تمت عملية النسخ بنجاح من {source_db_path} إلى {target_db_path}")
        
        source.close()
        dest.close()
        
    except sqlite3.Error as e:
        print(f"حدث خطأ أثناء النسخ: {e}")

# --- هنا نقوم باستدعاء الدالة لتشغيلها ---
# استبدل 'my_database.db' باسم قاعدة بياناتك الحقيقية
backup_db('sqlite3.db', 'backup_datas.db')