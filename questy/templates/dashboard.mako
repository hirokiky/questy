<!DOCTYPE html>
<html lang="${request.locale_name}">
<head>
  <meta charset="utf-8">
  <meta name="author" content="Kaede Studios">

  <!-- Styles -->
  <link rel="stylesheet" href="${request.static_url('questy:static/bower_components/bootstrap/dist/css/bootstrap.min.css')}" />

  <title></title>

</head>
<body>

<div class="container">

## Global Header
<nav class="navbar navbar-default" role="navigation">
  <div class="container-fluid">
    <div class="navbar-header">
      <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">
        <span class="sr-only">Toggle navigation</span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
      </button>
      <a class="navbar-brand" href="#">Questy</a>
    </div>

    <!-- Collect the nav links, forms, and other content for toggling -->
    <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
      <ul class="nav navbar-nav">
        <li class="active"><a href="#">TimeLine</a></li>
      </ul>
      <ul class="nav navbar-nav navbar-right">
        <li class="dropdown">
          <a href="#" class="dropdown-toggle" data-toggle="dropdown">Account<span class="caret"></span></a>
          <ul class="dropdown-menu" role="menu">
            <li><a href="#">Setting</a></li>
            <li class="divider"></li>
            <li><a href="#">Logout</a></li>
          </ul>
        </li>
      </ul>
    </div><!-- /.navbar-collapse -->
  </div><!-- /.container-fluid -->
</nav>
</div>

<!-- Scripts -->
<script src="${request.static_url('questy:static/bower_components/jquery/dist/jquery.min.js')}"></script>
<script src="${request.static_url('questy:static/bower_components/bootstrap/dist/js/bootstrap.min.js')}"></script>
</body>
</html>
