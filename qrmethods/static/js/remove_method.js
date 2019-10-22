function remove_method(method) {
  let ids_list = JSON.stringify($("#lesson_list .method_id").map(function() {
    return $.trim($(this).text());
  }).get());
  $("#remove_ids").attr("value", ids_list);
  $("#remove_method").attr("value", method);
  $("#remove_ids_list").submit();
  $("#remove_ids").attr("value", "");
  $("#remove_method").attr("value", "");
}
