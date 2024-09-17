const newsletterUrl = "/newsletter/";
const datePickerId = document.getElementById("datePickerId");

if (datePickerId) {
  datePickerId.max = new Date().toISOString().split("T")[0];
}
$(document).ready(() => {
  /*Alert Toast Auto/Custom Hide */
  hideContent("alert-message");
  $("#alert-message-close-btn").click(() => {
    hideContent("alert-message");
    hideContent("custom-alert-message");
  });

  /*Article Delete Action Handling */
  $(".articleDeleteAction").click((event) => {
    event.preventDefault();
    console.log(event.target);
  });

  /*Newsletter Subscribtion Handling Ajax */
  $("#newsletter-form").submit((event) => {
    event.preventDefault();
    csrfToken = event.target.querySelector(
      '[name="csrfmiddlewaretoken"]'
    ).value;
    email = event.target.querySelector('[name="subscribe"]').value;
    postRequest(newsletterUrl, {
      email: email,
      csrfmiddlewaretoken: csrfToken,
    });
  });
});

/*Custom Alert Trigger */
function alertCustomTrigger(message) {
  const customAlert = document.getElementById("custom-alert-message");
  const customAlertBody = document.getElementById("custom-alert-body");

  customAlertBody.innerText = message;
  customAlert.style.display = "block";
  hideContent("custom-alert-message");
}

/*Hide Content */
function hideContent(id) {
  setTimeout(() => {
    $("#" + id).hide();
  }, 5000);
}

/*Ajax Requests */
function postRequest(url, data) {
  ajaxCall("POST", url, data);
}

function ajaxCall(method, url, data) {
  $.ajax({
    url: url,
    type: method,
    data: data,
    headers: {
      "X-CSRFToken": data.csrfmiddlewaretoken,
    },
    success: function (content, status, xhr) {
      if (xhr.status == 200) {
        alertCustomTrigger(content.message);
      }
    },
    error: function (xhr, error, status) {
      console.error(`An Error Occured with Status ${status} ${xhr.status}`);
    },
  });
}
