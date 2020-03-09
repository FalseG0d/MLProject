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
});
//Custom Validation
eventSchema.path('date').validate((val)=>{
    dateRegex=/^(0[1-9]|1[012])[- /.] (0[1-9]|[12][0-9]|3[01])[- /.] (19|20)\d\d$/;
    return dateRegex.test(val);
},"Invalid Date");
mongoose.model('Event',eventSchema);