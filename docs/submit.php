<?php
  session_start();
  function h($word) {
  return htmlspecialchars($word, ENT_QUOTES, "UTF-8");
}
  if(isset($_POST["re_token"])
  && $_POST["re_token"] === $_SESSION["re_token"]){
?>

<!DOCTYPE html>
<html lang="ja">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="style.css" rel="stylesheet">
    <link href="css/bootstrap.min.css" rel="stylesheet">
    <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous" rel="stylesheet" >
    <script src="https://kit.fontawesome.com/6a85367f33.js" crossorigin="anonymous"></script>
    <title>送信</title>
  </head>
  <body>
    <div class="wrapper">
      <header>
        <div class="container">
          <div class="header-left">
            <img class="logo" src="logo.png" alt="">
          </div>
        </div>
      </header>
      <div class="container">
        <section class="section">
          <div class="section-title-block">
            <h2 class="section-title"><span class="fa fa-envelope-o" aria-hidden="true"></span>送信完了</h2>
          </div>
          <?php
            //自分のメールアドレスに送るメール
            $email="toshi.futa1991@gmail.com";
            mb_language("ja");
            mb_internal_encoding("UTF-8");
            $subject=h($_POST["name"])." 様からのお問い合わせ";
            $body="Tossy's portfolio から自動送信\r\n";
            $body.="【お名前】".h($_POST["name"])."\r\n";
            $body.="【メールアドレス】".h($_POST["mail"])."\r\n";
            $body.="【内容】".h($_POST["contents"]);
            $send=mb_send_mail($email,$subject,$body);
          ?>

          <?php
            //相手のメールアドレスに送るメール
            $email=h($_POST["mail"]);
            mb_language("ja");
            mb_internal_encoding('UTF-8');
            $subject="【お礼】お問い合わせを受け付けいたしました。\r\n";
            $body="Tossy's portfolio から自動送信\r\n";
            $body.="※このメールへの返信は、できません。\r\n";
            $body.="以下の通り、お問い合わせを受け付けいたしました。\r\n";
            $body.="◆お名前\n".h($_POST["name"])."\r\n";
            $body.="◆メールアドレス\n".h($_POST["mail"])."\r\n";
            $body.="◆内容\n".h($_POST["contents"]);
            $send=mb_send_mail($email,$subject,$body);
          ?>

          <!---送信後の画面確認 -->
          <table>
            <tr>
              <th><label for="name">お名前</label></th>
              <td><?php print(h($_POST["name"]));?></td>
            </tr>
            <tr>
              <th><label for="mail">メールアドレス</label></th>
              <td><?php print(h($_POST["mail"]));?></td>
            </tr>
            <tr>
              <th><label for="contents">内容</label></th>
              <td><?php print(h($_POST["contents"]));?></td>
            </tr>
          </table>
          <a href="index.html"><button type="submit" class="btn btn-primary">ホームへ戻る</button></a>

          <?php
            } else{
          ?>
          <p>メールの送信に失敗しました</p>
          <a href="index.html"><button type="submit" class="btn btn-primary">ホームへ戻る</button></a>
          <?php
            }
          ?>

        </div>
      </div>
      <footer>
      <p>
        Copylight Tossy-futa.All Rights Reserved.
      </p>
    </footer>
  </body>
</html>
