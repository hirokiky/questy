<!DOCTYPE html>
<html lang="${request.locale_name}">
<head>
  <meta charset="utf-8">
  <meta name="author" content="Kaede Studios">

  <!-- Styles -->
  <link rel="stylesheet" href="${request.static_url('questy:static/css/bootstrap.css')}" />
  <link rel="stylesheet" href="${request.static_url('questy:static/css/nonresp.css')}" />
  <link rel="stylesheet" href="${request.static_url('questy:static/css/main.css')}" />

  <title></title>

</head>
<body>

<div class="container">
  ## Global Header
<nav class="navbar navbar-default" role="navigation">
  <div class="container-fluid">
    <div class="navbar-header">
      <a class="navbar-brand" href="#">Questy</a>
    </div>

    <!-- Collect the nav links, forms, and other content for toggling -->
    <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
      <ul class="nav navbar-nav">
        <li class="active"><a href="#">TimeLine</a></li>
      </ul>
      <ul class="nav navbar-nav navbar-right">
        <li class="dropdown">
          <a href="#" class="dropdown-toggle" data-toggle="dropdown">TODO<span class="caret"></span></a>
          <ul class="dropdown-menu" role="menu">
            <li><a href="#">Setting</a></li>
            <li class="divider"></li>
            <li><a href="${request.route_path('logout')}">Logout</a></li>
          </ul>
        </li>
      </ul>
    </div><!-- /.navbar-collapse -->
  </div><!-- /.container-fluid -->
</nav>
  <div data-bind="page: {id: 'dashboard', title: 'Dashboard', role: 'start',
                         with: dashboard, sourceOnShow: '${request.static_url('questy:static/views/dashboard.html')}'}"></div>
  <div data-bind="page: {id: 'page2', title: 'Page2'}">
    page2
  </div>
</div>
<!-- Scripts -->
<script type="text/javascript" src="${request.static_url('questy:static/js/libs/jquery.min.js')}"></script>
<script type="text/javascript" src="${request.static_url('questy:static/js/libs/bootstrap.min.js')}"></script>
<script type="text/javascript" src="${request.static_url('questy:static/js/app.js')}"></script>
</body>
</html>
