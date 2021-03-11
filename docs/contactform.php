<?php
    session_start();
    function h($word) {
    return htmlspecialchars($word, ENT_QUOTES, "UTF-8");
  }
    $token = openssl_random_pseudo_bytes(16);
    $re_token = bin2hex($token);
    $_SESSION["re_token"] = $re_token;
?>

<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link href="style.css" rel="stylesheet">
  <link href="css/bootstrap.min.css" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/Swiper/5.3.7/css/swiper.min.css">
  <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous" rel="stylesheet" >
  <script src="https://kit.fontawesome.com/6a85367f33.js" crossorigin="anonymous"></script>
  <title>内容確認</title>
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
          <h2 class="section-title"><span class="fa fa-envelope-o" aria-hidden="true"></span>内容確認</h2>
        </div>
        <div class="mail-form">
          <form action="submit.php" method="post">
            <table>
              <tr>
                <th><label for="name">【お名前】</label></th>
                <td><?php echo h($_POST['name']); ?></td>
              </tr>
              <tr>
                <th><label for="mail">【メールアドレス】</label></th>
                <td><?php echo h($_POST['mail']); ?></td>
              </tr>
              <tr>
                <th><label for="contents">【内容】</label></th>
                <td><?php echo h($_POST['contents']); ?></td>
              </tr>
            </table>
            <button type="submit" class="btn btn-primary">送信</button>
            <input type="button" value="戻る" onclick="history.back(-1)" class="btn btn-primary">
            <input type="hidden" name="re_token" value="<?= $re_token ?>">
            <input type="hidden" name="name" value="<?php echo h($_POST['name']); ?>">
            <input type="hidden" name="mail" value="<?php echo h($_POST['mail']); ?>">
            <input type="hidden" name="contents" value="<?php echo h($_POST['contents']); ?>">
          </form>
        </div>
      </section>
    </div>
  </div>
  <footer>
    <p>
      Copylight Tossy-futa.All Rights Reserved.
    </p>
  </footer>
    </body>
</html>
