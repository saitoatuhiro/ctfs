# Easy Pisy

sign.phpとexecute.phpのソースが与えらた。
sign.phpには以下の処理があった。  

* PDFファイルをテキスト化する(OCRっぽやつ)
```php
 $text = pdf_to_text($file_info['tmp_name']);
```
* テキスト化した値が"EXECUTE"から始まる場合は、怒られる。 
* テキスト化した値が"ECHO"から始まる場合は、ファイルのsignatureを出力してくれる
```php
$execute_query = "EXECUTE ";
$echo_query = "ECHO ";
if (substr($text, 0, strlen($execute_query)) === $execute_query) {
    print "I don't sign EXECUTE commands. Go away.<br/>";
} else if (substr($text, 0, strlen($echo_query)) === $echo_query) {
    print "I'm OK with ECHO commands. Here is the signature: <br/>";
    $data = file_get_contents($file_info['tmp_name']);
    openssl_sign($data, $signature, $privkey);   
    print bin2hex($signature); 
} else {
    print "I can't recognize the command type. Go away.<br/>";
}
```

execute.phpには以下の処理があった。

* PDFファイルをテキスト化する(OCRっぽやつ)  
```php
 $text = pdf_to_text($file_info['tmp_name']);
```
* 入力されたsignatureとファイルのsignatureが一致すれば、テキスト化した内容に応じて処理を行う。  
    * ECHOからは始まる場合、テキストの値をそのままECHOする
    ```php
    echo $payload 
    ```
    * EXECUTEから始まる場合、テキストの値で与えられたコマンドを実行する。
    ```php
    $out = shell_exec($payload);
    print "Output: $out";
    ```

当然、EXECUTEから始まるファイルをアップロードしてもsignatureを得ることはできないので、他の方法を考えるしかない。  
1. 鍵を盗む、割り出す
2. ハッシュ関数の脆弱性を探す

1.は問題のカテゴリがcryptでもあったので、違うかなと思った。  
そのため、問題を解く方針は2.にした。  

openssl_sign関数をphp.netで調べると、使用するアルゴリズムを省略すると、SHA-1が使用されることが分かった。  
SHA-1 衝突で調べると、異なる画像で同じsignatureを持つファイルを生成できることが分かったので、オンラインジェネレータを使用した。  

ECHOから始まるファイルのsignatureを使用して、EXECUTEのファイルをアップロードしたら、フラグゲット。  
```
EXECUTE cat flag;
```

```
OOO{phP_4lw4y5_d3l1v3r5_3h7_b35T_fl4g5}
```
