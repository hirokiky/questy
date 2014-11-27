var $ = require('jquery');
var ko = require('knockout');
var pager = require('pagerjs');

var dashboardViewModel = require('./viewmodels/dashboardViewModel.js');

$(function() {
  var viewModel = {
    dashboard: new dashboardViewModel()
  };

  pager.extendWithPage(viewModel);
  ko.applyBindings(viewModel);
  pager.startHistoryJs();
});
