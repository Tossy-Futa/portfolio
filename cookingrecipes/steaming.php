<?php
    function h($word) {
    return htmlspecialchars($word, ENT_QUOTES, "UTF-8");
  }
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
            <a href="fry.php">焼く(炒める)</a>
            <a href="simmer.php">煮る</a>
            <a href="steaming.php">蒸す</a>
            <a href="etc.php">その他</a>
          </div>
        </div>
      </header>

    <div class="wrapper">

      <div class="container">
        <div class="section-title-block">
          <h2 class="section-title"><i class="fas fa-mug-hot"></i>蒸す</h2>
        </div>
        <section class="cooking-list" id="list">
          <?php
          $user = "aaaa";
          $pass = "aaaa";
          try {
            $dbh = new PDO("mysql:host=localhost;dbname=cookingrecipes;charset=utf8", $user, $pass);
            $dbh->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
            $sql = "SELECT * FROM recipes";
            $stmt = $dbh->query($sql);
            $result = $stmt->fetchAll(PDO::FETCH_ASSOC);
            foreach ($result as $row) {
              if ($row["cookingmethod"] == 3){
          ?>
          <a href="detail.php?id=<?php echo $row[id];?>"><p>
          <?php echo h($row["name"]) ?>
          </a></p>
          <?php
          } else {
          }
          }
          $dbh = null;
          } catch (Exception $e) {
            echo "エラーです。" . h($e->getMessage());
          }
          ?>
          <a href="index.html"><button type="submit" class="btn btn-primary">ホームへ戻る</button></a>
        </section>
      </div>

    </div>

    <footer>
      <div class="footer-menu">
        <ul>
          <li><a href="fry.php">焼く(炒める)</a> ｜</li>
          <li><a href="simmer.php">煮る</a> ｜</li>
          <li><a href="steaming.php">蒸す</a> ｜</li>
          <li><a href="etc.php">その他</a></li>
        </ul>
      </div>
      <p>
        Copylight Tossy-futa.All Rights Reserved.
      </p>
    </footer>
  </body>
</html>
