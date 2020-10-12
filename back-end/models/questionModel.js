var mongoose = require('mongoose');

const questionSchema = new mongoose.Schema({
    owner : {type : mongoose.Schema.Types.ObjectId,ref :'User'},
    topic : {type:String,requiredL:false},
    desc: {type:Text, required :true},
    otherdetails:{type:Text,required:false},
});

const Questionmodel = mongoose.model('Question',questionSchema);

module.exports = Questionmodel;