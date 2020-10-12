const jwt = require('jsonwebtoken');
const authConfig = require('../configs/auth');
const bcrypt = require('bcrypt');
const sendmail = require('../utility/sendMail ');
const database = require('../models/model');
const auth = require('../configs/auth');
const { text } = require('express');

