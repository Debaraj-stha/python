function validateForm() {
  const name = document.getElementById("name").value;
  if (name.length == 0) {
    alert("name is required");
    return false;
  } else if (name.length >= 15) {
    alert("name length must be between 15 and ");
  } else if (name.trim().length == 0) {
    alert("Please enter a valid name");
    return false;
  } else {
    // document.cookie = "name=" + name;
    return true;
  }
}

console.log("called");
window.load = function () {
  let url = new URL(window.location);
  console.log(url);
};
connectToSocket();

async function sendMessage() {
  let message = document.getElementById("message").value;
  if (message.length == 0) {
    return false;
  } else if (message.trim().length == 0) {
    return false;
  } else {
    let url = new URL(window.location);
    let urlSearchParam = new URLSearchParams(url.search);
    let group = urlSearchParam.get("group");
    let to = urlSearchParam.get("to");
    let data = {
      message: message,
      group: group,
      to: to,
    };
    const xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
      if (this.readyState == 4 && this.status == 200) {
        const res = JSON.parse(this.response);
        console.log(res);
        message = "  ";
      }
    };
    xhttp.open("POST", "http://localhost:8000/message/send", true);
    xhttp.setRequestHeader("Content-Type", "application/json");
    xhttp.send(JSON.stringify(data));
    message = "";
  }
}
function connectToSocket() {
  console.log("called");
  let socket = new WebSocket("ws://localhost:8000/ws/wc?group=demo");
  socket.onopen = function (s, event) {
    console.log(s, event);
  };
  socket.onclose = function (s, event) {
    console.log(event);
  };
  socket.onerror = function (s, event) {
    console.log("error", event);
  };
  socket.onmessage = function (s, event) {
    console.log("s", s);
    console.log("event", event);
    const res = JSON.parse(s.data);
    console.log("res", res);
    console.log(res.message);
    message = "";
    let wrapper = document.getElementById("messages");
    let x = `<div class="card mb-3 mt-5"><a href="#"> <div class="card-body text-decoration-none text-black-50"><blockquote class=" mb-0 text-decoration-none"> <p class="text-decoration-none">${res.from}</p>  <div class="d-flex justify-content-between">
      <span class="text-decoration-none">${res["message"]}</span>
      <span>${res.created_at}</span>
     </div></blockquote></div></a>    </div>`;
    if (res["message"] != null) {
      wrapper.innerHTML += x;
    }
  };
}
