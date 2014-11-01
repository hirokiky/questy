<!DOCTYPE html>
<html lang="${request.locale_name}">
<head>
  <meta charset="utf-8">
  <meta name="author" content="Kaede Studios">

  <!-- Styles -->
  <link rel="stylesheet" href="${request.static_url('questy:static/bower_components/bootstrap/dist/css/bootstrap.min.css')}" />
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

  <div class="row">
    <div class="col-xs-9">
      <div class="dashboard-stream">
        <div class="page">
          <div class="page-detail">
            <div class="row">
              <div class="col-xs-4">
                <img class="page-summary img-responsible img-thumbnail" src="http://dummyimage.com/800x800" />
                <div class="page-total-arrival">10000 arrival</div>
              </div>
              <div class="col-xs-8">
                <h2 class="page-title">Page title</h2>
                <div class="page-description">test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test ...</div>
                <a class="page-link">Readmore</a>
              </div>
            </div>
          </div>
          <div class="comments">
            <div class="comment">
              <div class="row">
                <div class="col-xs-2 col-xs-offset-2">
                  <img class="user-icon img-responsible img-thumbnail" src="http://dummyimage.com/600x600" />
                </div>
                <div class="col-xs-8">
                  <div class="comment-body">test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test</div>
                  <div class="reactions">
                    <div class="row">
                      <div class="col-xs-2">
                        <div class="upvote"><span class="glyphicon glyphicon-thumbs-up"></span><span class="vote-count">8</span></div>
                      </div>
                      <div class="col-xs-2">
                        <div class="downvote"><span class="glyphicon glyphicon-thumbs-down"></span><span class="vote-count">3</span></div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div><!-- /comment -->
        </div><!-- /comments -->
      </div><!-- /dashboard-stream -->
    </div><!-- /col-xs-9 -->
    <div class="col-xs-3">
      <div class="sidebar">
        <div class="row">
          <div class="col-xs-4">
            <img class="user-icon img-responsible img-thumbnail" src="http://dummyimage.com/300x300" />
          </div>
          <div class="col-xs-8">
            <div class="user-name">Hiroki KIYOHARA</div>
            <div class="user-playstyle">Casual</div>
          </div>
        </div>
        <div class="user-achievements">9820 point</div>
        <div class="user-followings">121 following</div>
        <div class="user-followers">132 following</div>
        <div class="user-arrivals">801 arrival</div>
        <div class="user-comments">201 comment</div>
      </div><!-- /sidebar -->
    </div><!-- /col-xs-3 -->
  </div>
</div>
<!-- Scripts -->
<script src="${request.static_url('questy:static/bower_components/jquery/dist/jquery.min.js')}"></script>
<script src="${request.static_url('questy:static/bower_components/bootstrap/dist/js/bootstrap.min.js')}"></script>
</body>
</html>
