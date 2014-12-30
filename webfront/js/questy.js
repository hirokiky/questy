var $ = require('jquery');
var ko = require('knockout');
var pager = require('pagerjs');

var dashboardPage = require('./pages/dashboardPage.js');
var arrivePage = require('./pages/arrivePage.js');

$(function() {
  var viewModel = {
    dashboard: dashboardPage,
    arrive: arrivePage
  };

  pager.extendWithPage(viewModel);
  ko.applyBindings(viewModel);
  pager.startHistoryJs();
});
