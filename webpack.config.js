var path = require('path');
var webpack = require('webpack');

module.exports = {
    entry: "./webfront/js/dashboard.js",
    output: {
        path: path.join(__dirname, 'questy/static/js/'),
        filename: "app.js"
    },
    resolveLoader: {
        root: path.join(__dirname, "node_modules")
    },
    module: {
        loaders: [
            {test: /knockout\/build\/output\/knockout-latest\.debug\.js/, loader: 'imports?require=>__webpack_require__'},  // For Knockout.js
            {test: /pager\.js/, loader: 'imports?$=>require("jquery"),ko=>require("knockout")!exports?window.pager'}  // For pagerjs
        ],
        noParse: [
            /knockout\/build\/output\/knockout-latest\.debug\.js/  // For Knockout.js
        ]
    }
};
