function WOL(){
    $.get(window.location.origin+"/WOL",function(){
        alert("Completed")
    });
}