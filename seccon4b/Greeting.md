usernameがadminならフラグが出力される。
```
<?php

if(isset($_POST['name'])) {
  setcookie("name", $_POST['name'], time()+3600);
  $username = htmlspecialchars($_POST['name'], ENT_QUOTES, "UTF-8");

  // 管理者でログインできる？
  if($username === "admin") {
    $username = "偽管理者";
  }
} elseif(isset($_COOKIE['name'])) {
  $username = htmlspecialchars($_COOKIE['name'], ENT_QUOTES, "UTF-8");
} else {
  $username = "ゲスト";
}
```

Cookieにname=adminがセットされてる状態で、GETアクセスすればOK
