

$(document).ready(function() {
  $( "#accordion" ).accordion({
    collapsible: true
  });

  $( "#accordion_sort" )
    .accordion({
      header: "> div > .acc_link"
    })
    .sortable({
      axis: "y",
      handle: ".acc_link",
      stop: function( event, ui ) {
        // IE doesn't register the blur when sorting
        // so trigger focusout handlers to remove .ui-state-focus
        ui.item.children( ".acc_link" ).triggerHandler( "focusout" );

        // Refresh accordion to handle new order
        $( this ).accordion( "refresh" );
      }
    });
});
