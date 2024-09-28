function current_time(){
    let current  = new Date();

    document.write("접속 시간: ", current.getHours(), "시", current.getMinutes(), "분", current.getSeconds(), "초")
}