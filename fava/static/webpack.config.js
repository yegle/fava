var webpack = require('webpack');
var path = require('path');
var ExtractTextPlugin = require('extract-text-webpack-plugin');

var extractScreenCSS = new ExtractTextPlugin('screen.css', { allChunks: true });
var extractPrintCSS = new ExtractTextPlugin('print.css', { allChunks: true });


module.exports = {
  entry: {
    'app': './javascript/main.js',
    'editor': './javascript/editor.js',
    'screen': './sass/screen.scss',
    'print': './sass/print.scss'
  },
  output: {
    path: __dirname + '/gen',
    filename: '[name].js'
  },
  module: {
    loaders: [
      {
        test: /screen\.scss$/,
        loader: extractScreenCSS.extract('style-loader', 'css-loader!sass-loader')
      },
      {
        test: /print\.scss$/,
        loader: extractPrintCSS.extract('style-loader', 'css-loader!sass-loader')
      },
      {
        test: [/ace-builds.*/, /.*ace-mode-beancount.*/],
        loader: 'script-loader'
      }
    ]
  },
  plugins: [
    new webpack.optimize.UglifyJsPlugin(),
    new webpack.ProvidePlugin({
      $: 'jquery',
      jQuery: 'jquery',
    }),
    extractScreenCSS,
    extractPrintCSS
  ],
}
