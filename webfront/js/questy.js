var $ = require('jquery');
var ko = require('knockout');
var pager = require('pagerjs');

var dashboardPage = require('./pages/dashboardPage.js');

$(function() {
  var viewModel = {
    dashboard: dashboardPage
  };

  pager.extendWithPage(viewModel);
  ko.applyBindings(viewModel);
  pager.startHistoryJs();
});
