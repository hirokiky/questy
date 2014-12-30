var path = require('path');
var url = require('url');

var ko = require('knockout');
var pager = require('pagerjs');

var config = require('config');


var initial_url = function() {
  var url_parsed = url.parse(window.location.href, true);
  return url_parsed.query.url || '';
};


var arriveViewModel = function() {
  var self = this;
  self.arriveURL = ko.observable(initial_url());
};


var arrivePage = new pager.Page();
arrivePage.valueAccessor = function() {
  return {id: 'arrive', title: 'Arrive',
           with: new arriveViewModel(),
           sourceOnShow: path.join(config.STATIC_URL, 'views/arrive.html')}
};


module.exports = arrivePage;
