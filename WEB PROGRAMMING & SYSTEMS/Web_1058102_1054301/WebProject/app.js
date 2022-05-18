const express = require('express');//IMPORT EXPRESS FRAMEWORK
const app = express();//EXECUTING EXPRESS
const path = require('path');//Για να χρησιμοποιήσουμε την εντολή μετά path.join
const mongoose = require('mongoose');//IMPORT MONGOOSE.
const session = require('express-session');



/*SESSION*/
app.use(
    session({
      name: "session",
      saveUninitialized: true,
      resave: true,
      secret: "Welcome to our web ",
      cookie: {
        secure: false,
        maxAge: 600000000000000,
      },
    })
  );
var sess;






var upload = require("express-fileupload");
app.use(upload()); 


/*SET EJS AS VIEW ENGINE */
app.set('views',path.join(__dirname,'views'));
app.set('view engine', 'ejs');
app.use(express.static(path.join(__dirname, 'public')));
app.use(express.static(path.join(__dirname)));




app.use(express.urlencoded({ extended: true }));
app.use(express.json());
//app.use(methodOverride('_method'))



//Εδώ κάνω connect την mongoose.
//'mongodb://localhost:27017/WebDatabase'
const mongoURI = 'mongodb://localhost:27017/WebDatabase';
mongoose.connect(mongoURI, {useNewUrlParser: true, useUnifiedTopology: true})
    .then(() => {
        console.log("MONGO CONNECTION OPEN!!!")
    })
    .catch(err => {
        console.log("OH NO MONGO CONNECTION ERROR!!!!")
        console.log(err)
    })




/*INDEX*/
app.get('/',(req,res) => {
    // sess=req.session;
    // if(sess.username){
    //     res.render('index',{name:sess.username}); 
    // }else{
    //     res.render('index');
    // }
    res.render('index');
})



/* MY ROUTES */
const ServerSignUp = require("./routes/ServerSignUp");
app.use('/SignUp', ServerSignUp);

const ServerLogin = require("./routes/ServerLogin");
app.use('/',  ServerLogin);

const ServerUpload = require("./routes/ServerUpload");
app.use('/Upload', ServerUpload);


const ServerEdit = require("./routes/ServerEdit");
app.use('/Edit', ServerEdit);

const ServerLogout = require("./routes/ServerLogout");
app.use('/Logout', ServerLogout);

const ServerAdminLogin = require("./routes/ServerAdminLogin");
app.use('/AdminIndex', ServerAdminLogin);

const morf_stats = require("./routes/morf_stats");
app.use("/morf_stats", morf_stats);

const morf_chart = require("./routes/morf_chart");
app.use("/morf_chart", morf_chart);

const morf_map = require("./routes/morf_map");
app.use("/morf_map", morf_map);

const admin_c = require("./routes/admin_c");
app.use("/admin_c", admin_c);

const ServerHeatmap = require("./routes/ServerHeatmap");
app.use("/Heatmap", ServerHeatmap);

const admin_login = require("./routes/admin_login");
app.use("/admin_login", admin_login);


//Εδώ λέμε στον server οτι ακουεί στο localhost:3000
app.listen(3000,() => {
    console.log("APP IS LISTENING ON PORT 3000")
})