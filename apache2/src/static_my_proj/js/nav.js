$(document).ready(function() {

	$('.nav_link a').click(function() {
				  var categoryName = $(this).attr('categoryName');
				  console.log(categoryName);
					var prospectName = $(this).attr('prospectName');
					console.log(prospectName);

					// if (prospectName === 'Men') {
					// 		$( "#accordion" ).accordion({ active: 0 });
					// }
					// else if (prospectName === 'Ladies') {
					// 	$( "#accordion" ).accordion({ active: 1 });
					// }
					// else {
					// 	$( "#accordion" ).accordion({ active: 2 });
					// }
 	  //return false; // return false so the browser will not scroll your page
	});

	// $('.clothing_category').click(function(e) {
	//
	// 	var categoryName = $(this).html();
	// 	var product_type
	// 	alert("Hello" + categoryName);
	// 	var product_type = $('h5').html();
	// 	alert(product_type);
	// 	var prospect = $('#prospect_type').html();
	// 	alert(prospect);
	// });

$('#shoe_category').click(function(e) {

	var categoryName = $(this).text();
	var product_type
	//alert("Hello" + categoryName);
	var product_type = $('h5').html();
	//alert(product_type);
});

})
