var mongoose = require('mongoose');
var Schema = mongoose.Schema;   

const userDetailsSchema = new mongoose.Schema({
    firstname:{type:String,required:true},
    lastname:{type:String,required:false},
    dob:{type:Date,reuiqred:true},
    contact_no:{type:Number,required:false},
});

const useraspirantinfo = new mongoose.Schema({
    details : userDetailsSchema,
    stats:{
        questions:[{type: Schema.Types.ObjectId,ref:'Question'}],
    }
});

const userexpertinfo = new mongoose.Schema({
    details : userDetailsSchema,
    qualifications : {type:Text,required:true},
    current_job : {type:Text,required:true},
    is_verified : {type :Boolean,default:false},
    stats: {
        answers:{type:Number,default:0},
    },
});

const UserSchema = new mongoose.Schema({
    email :{type:String,required :true,unique:true },
    username :{type:String,required:true,unique:true},
    password:{type:String,reuiqred:true},
    created:{type:Date,default:Date.now},
    confirmed:{type:Boolean,default:false},
    recievemails:{type:Boolean,default:true},
    forgotpasswordcode:{type:String,required:false},

    

    useraspirantinfo: useraspirantSchema,

    userexpertinfo :userexpertSchema,

    notifications:[notificationSchema],

    'category' :{type:String,required:true}
});

const usermodel =mongoose.model('User',UserSchema); 

module.exports = usermodel;