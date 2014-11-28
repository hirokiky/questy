var path = require('path');
var webpack = require('webpack');

module.exports = {
    entry: "./webfront/js/questy.js",
    output: {
        path: path.join(__dirname, 'questy/static/js/'),
        filename: "app.js"
    },
    resolveLoader: {
        root: path.join(__dirname, "node_modules")
    },
    resolve: {
        alias: {
            historyjs: 'historyjs/scripts/bundled-uncompressed/html4+html5/native.history.js',
            config: path.join(__dirname, 'webfront/js/config/dev.js')
        }
    },
    module: {
        loaders: [
            {test: /knockout\/build\/output\/knockout-latest\.debug\.js/, loader: 'imports?require=>__webpack_require__'},  // For Knockout.js
            {test: /pager\.js/, loader: 'imports?$=>require("jquery"),ko=>require("knockout"),history=>require("historyjs")!exports?window.pager'},  // For pagerjs
            {test: /history\.js/, loader: 'exports?window.History'}
        ],
        noParse: [
            /knockout\/build\/output\/knockout-latest\.debug\.js/  // For Knockout.js
        ]
    }
};
