function appendTodiv(div, msg) {
    console.log("Trying to append to div results, the following message" + msg);
    div.append("<p>" + msg + "</p>")
}