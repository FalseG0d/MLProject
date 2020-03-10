const mongoose=require('mongoose');

var eventSchema=new mongoose.Schema({
    eventName:{
        type:String,
        required:"Event Name is required"
    },
    date:{
        type:Date,
        required:"Event Date is required"
    },
    venue:{
        type:String,
        required:"Event Venue is required"
    },
    comments:{
        type:String
    }
});/*
//Custom Validation
eventSchema.path('date').validate((val)=>{
    dateRegex=/^\d{2}([./-])\d{2}\1\d{4}$/;
    return dateRegex.test(val);
},"Invalid Date");*/
mongoose.model('Event',eventSchema);