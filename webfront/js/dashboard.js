var ko = require('knockout');

function MyViewModel() {
  var self = this;
  self.pagetitle = ko.observable('Page Title');
}
ko.applyBindings(new MyViewModel());
