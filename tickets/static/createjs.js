$.ajax({
    url: "/api/employee/1",
    type: "GET",
    success: function(response) {
        console.log(response)
        for (let emp of response) {
            let myoption = `<option value=${emp.id}>${emp.EmployeeName}</option>`
            $("#asign").append(myoption)
        }
    }
});