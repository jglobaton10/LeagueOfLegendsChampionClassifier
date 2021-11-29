Dropzone.autoDiscover = false;

function init() {
    $("#image_predicted").hide()
    $("#Champion_predicted").hide()
    let dz = new Dropzone("#dropzone", {
        url: "/",
        maxFiles: 1,
        addRemoveLinks: true,
        dictDefaultMessage: "Some Message",
        autoProcessQueue: false
    });
    dz.on("addedfile", function() {
        if (dz.files[1]!=null) {
            dz.removeFile(dz.files[0]);        
        }
    });
    dz.on("complete", function (file) {
        let imageData = file.dataURL;
        
        
        var url = "http://127.0.0.1:5000/classify_image";

        $.post(url, {
            image_data: file.dataURL.split(',')[1]
        },function(data, status) {
            
            $("#error").hide();
           
            //console.log(data);
            var dic_images = {"Aatrox":"./images/Aatrox lol_1.jpeg" ,"Ahri":"./images/Ahri lol_1.jpeg" ,"Akali":"./images/Akali lol_1.jpeg","Anivia":"./images/Anivia lol_1.jpeg"
            ,"Cassiopeia":"./images/Cassiopeia lol_1.jpeg"}
            document.getElementById("Champion_predicted").innerHTML = data.champion;
            //document.getElementById("Champion_predicted").innerHTML = dic_images[data.champion];
            //document.getElementById("image_predicted").innerHTML = dic_images[data.champion];
            $("#image_predicted").show()
            $("#Champion_predicted").show()
            $("#image_predicted").attr("src", dic_images[data.champion]);
        });
    });
    $("#submitBtn").on('click', function (e) {
        dz.processQueue();		
    });
}
$(document).ready(function() {
    console.log( "ready!" );
    $("#error").hide();
    $("#resultHolder").hide();
    $("#divClassTable").hide();
    init();
});