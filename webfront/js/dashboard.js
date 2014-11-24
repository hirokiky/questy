var $ = require('jquery');
var ko = require('knockout');
var pager = require('pagerjs');


$(function() {
  pager.Href.hash = '#!/';

  var viewModel = {
    pagetitle: "Page Title"
  };
  pager.extendWithPage(viewModel);
  window.VW = viewModel;
  ko.applyBindings(viewModel);
  pager.start();
});
