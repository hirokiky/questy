var path = require('path');

var ko = require('knockout');
var pager = require('pagerjs');

var config = require('config');

var dashboardViewModel = function() {
  var self = this;
  self.pageTitle = ko.observable('dashboard page');
};


var dashboardPage = new pager.Page();
dashboardPage.valueAccessor = function() {
  return {id: 'dashboard', title: 'Dashboard', role: 'start',
          with: new dashboardViewModel,
          sourceOnShow: path.join(config.STATIC_URL, 'views/dashboard.html')}
};


module.exports = dashboardPage;
