<html>
<body>
<form action="${request.route_path('login')}" method="post">
  <label for="input-email">Email: </label><input id="input-email" name="email" type="email" required/>
  <label for="input-password">Password: </label><input id="input-password" name="password" type="password" required/>
  <button type="submit">Login</button>
</form>
</body>
</html>
