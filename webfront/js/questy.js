var $ = require('jquery');
var ko = require('knockout');
var pager = require('pagerjs');


var dashboardViewModel = function() {
  var self = this;
  self.pageTitle = ko.observable('dashboard page');
};

$(function() {
  var viewModel = {
    dashboard: new dashboardViewModel()
  };

  pager.extendWithPage(viewModel);
  ko.applyBindings(viewModel);
  pager.startHistoryJs();
});
