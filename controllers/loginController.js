const express=require('express');
var router=express.Router();
const mongoose=require('mongoose');
const bcrypt=require('bcrypt')
const User=mongoose.model('User');

const Event=mongoose.model('Event');

router.get('/',(req,res)=>{
    res.render("login/login",{name:"Apoorv"});
});

router.get('/register',(req,res)=>{
    res.render("login/register",{name:"Apoorv"});
});

router.post('/register',async (req,res)=>{
    try {
        const hashedPassword=await bcrypt.hash(req.body.password,10);
        var user=new User()
        user.userName=req.body.userName;
        user.email=req.body.email;
        user.password=hashedPassword;

        user.save((err,doc)=>{
            if(!err){
                console.log("User Registered");
                res.redirect('/');
            }else{
                console.log("Error during Registration: "+err);
            }
        })
        
    } catch (err) {
        console.log("Error: "+err);
    }
    
})
router.post('/',(req,res)=>{
    
})

module.exports=router;