$("#downloadfile").attr("disabled", "disabled");
$("#downloadfile").removeAttr("href");
$(document).ready(function() {
  $("#btnSubmit").click(function(event) {

    $("#loader").css("display", "block");

    //stop submit the form, we will post it manually.
    event.preventDefault();

    // Get form
    var form = $('#fileUploadForm')[0];

    // Create an FormData object
    var data = new FormData(form);

    // If you want to add an extra field for the FormData
    data.append("CustomField", "This is some extra data, testing");

    // disabled the submit button
    $("#btnSubmit").prop("disabled", true);

    $.ajax({
      type: "POST",
      enctype: 'multipart/form-data',
      url: "/excel/getExcel/",
      data: data,
      processData: false,
      contentType: false,
      cache: false,
      timeout: 600000,
      success: function(data) {
        console.log("SUCCESS : ", data);
        $("#downloadfile").removeAttr("disabled");
        $("#downloadfile").attr('href', data['link'])
        $("#btnSubmit").prop("disabled", false);
        $("#loader").css("display", "none");
      },
      error: function(e) {
        console.log("ERROR : ", e);
        $("#btnSubmit").prop("disabled", false);
      }
    });
  });
});
