var mongoose = require('mongoose');

const answerSchema = new mongoose.Schema({
    question :{type : mongoose.Schema.Types.ObjectId , ref :"Question"},
    solution : {type: Text,required :true},
    upvotes : {type:Number, default :0},
});

const answermodel = mongoose.model('Answer',answerSchema);

module.exports = answermodel;