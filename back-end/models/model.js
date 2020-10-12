const mongoose = require('mongoose');
mongoose.Promise = global.Promise;

const database = {};

database.mongoose = mongoose;

database.User = require('./usermodel');

database.Question = require('./questionModel');

database.Answer = require('./answermodel');

module.exports = database;