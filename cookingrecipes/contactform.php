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
  <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous" rel="stylesheet" >
  <script src="https://kit.fontawesome.com/6a85367f33.js" crossorigin="anonymous"></script>
  <title>料理レシピ</title>
</head>
  <body>

      <header>
        <div class="container">
          <div class="header-menu">
          </div>
        </div>
      </header>

      <div class="wrapper">
        <div class="container">
        <section class="section">
          <div class="section-title-block">
            <h2 class="section-title"><span class="fa fa-envelope-o" aria-hidden="true"></span>内容確認</h2>
          </div>
        <div class="recipe-form">
          <h3<label for="name">【料理名】</label></h3>
          <p><?php echo h($_POST["name"]); ?></p>
          <h3><label for="url">【URL】</label></h3>
          <p><?php echo h($_POST["url"]); ?></p>
          <h3><label for="cooking-method">【調理方法】</label></h3>
          <p><?php if($_POST["cooking-method"] == 1 ){
                    $method = "焼く(炒める)";
                    } elseif($_POST["cooking-method"] == 2 ){
                    $method = "煮る";
                    } elseif($_POST["cooking-method"] == 3 ){
                    $method = "蒸す";
                    } else {
                    $method = "その他";
                    }
                    echo $method; ?></p>
          <h3><label for="cooking-material">【材料】</label></h3>
          <p><?php echo h($_POST["cooking-material"]); ?></p>
          <h3><label for="recipe">【内容】</label></h3>
          <p><?php echo h($_POST["recipe"]); ?></p>
          <div class="form-button">
            <form action="submit.php" method="post">
              <button type="submit" class="btn btn-primary submit-button">送信</button>
              <input type="hidden" name="re_token" value="<?= $re_token ?>">
              <input type="hidden" name="name" value="<?php echo h($_POST['name']); ?>">
              <input type="hidden" name="url" value="<?php echo h($_POST['url']); ?>">
              <input type="hidden" name="cooking-method" value="<?php echo h($_POST["cooking-method"]); ?>">
              <input type="hidden" name="cooking-material" value="<?php echo h($_POST['cooking-material']); ?>">
              <input type="hidden" name="recipe" value="<?php echo h($_POST['recipe']); ?>">
              <input type="button" value="戻る" onclick="history.back(-1)" class="btn btn-primary">
            </form>
          </div>
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
