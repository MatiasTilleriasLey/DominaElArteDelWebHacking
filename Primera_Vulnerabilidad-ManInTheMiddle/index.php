<?php
if (isset($_POST['username']) && isset($_POST['password'])) {
    $param1 = $_POST['username'];
    $param2 = $_POST['password'];

    if ($param1 == "admin" && $param2 == "secretadminpassword"){
        echo "<h1>Bienvenido Admin</h1>";
    }

}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Domina el Arte del Web Hacking</title>
</head>
<body>
    <h1>Domina el Arte del Web Hacking - MitM</h1>
    <form action="/" method="post">
        <input type="text" name="username">
        <input type="password" name="password">
        <input type="submit" value="Login">
    </form>
</body>
</html>