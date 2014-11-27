var ko = require('knockout');


var dashboardViewModel = function() {
  var self = this;
  self.pageTitle = ko.observable('dashboard page');
};


module.exports = dashboardViewModel;
