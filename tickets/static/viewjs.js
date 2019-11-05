document.getElementById("priority").disabled = true;
document.getElementById("module").disabled = true;
document.getElementById("status").disabled = true;
document.getElementById("asign").disabled = true;
document.getElementById("task").disabled = true;
document.getElementById("title").disabled = true;
document.getElementById("summary").disabled = true;
document.getElementById("attachment").disabled = true;
document.getElementById("submit").disabled = true;

$("#edit").click(function () {
    $("#priority").prop('disabled', false);
    $("#status").prop('disabled', false);
    $("#summary").prop('disabled', false);
    $("#submit").prop('disabled', false);     
});