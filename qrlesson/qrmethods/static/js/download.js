function download() {
  let ids_list = JSON.stringify($("#lesson_list .method_id").map(function() {
    return $.trim($(this).text());
  }).get());
  $("#ids").attr("value", ids_list);
  $("#ids_list").submit();
  $("#ids").attr("value", "");
}
