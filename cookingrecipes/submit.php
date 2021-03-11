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
                <h2 class="section-title"><span class="fa fa-envelope-o" aria-hidden="true"></span>登録完了</h2>
              </div>
          <?php
            $user = "aaaa";
            $pass = "aaaa";
            $name = $_POST["name"];
            $url = $_POST["url"];
            $cooking_method = (INT) $_POST["cooking-method"];
            $cooking_material = $_POST["cooking-material"];
            $recipe = $_POST["recipe"];
            try {
              $dbh = new PDO("mysql:host=localhost;dbname=cookingrecipes;charset=utf8", $user, $pass);
              $dbh->setAttribute(PDO::ATTR_EMULATE_PREPARES, false);
              $dbh->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
              $sql = "INSERT INTO recipes (name, url, cookingmethod, cookingmaterial, recipe) VALUES(?, ?, ?, ?, ?)";
              $stmt = $dbh->prepare($sql);
              $stmt->bindValue(1, $name, PDO::PARAM_STR);
              $stmt->bindValue(2, $url, PDO::PARAM_STR);
              $stmt->bindValue(3, $cooking_method, PDO::PARAM_INT);
              $stmt->bindValue(4, $cooking_material, PDO::PARAM_STR);
              $stmt->bindValue(5, $recipe, PDO::PARAM_STR);
              $stmt->execute();
              $dbh = null;
              echo "登録が完了しました。";
            } catch (Exception $e) {
              exit( "エラーです。" . $e->getMessage()) ;
              die();
            }
          } else{
          ?>
          <p>登録に失敗しました。</p>
          <?php
            }
          ?>

        <p><a href="index.html"><button type="submit" class="btn btn-primary">ホームへ戻る</button></a></p>

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
