$(document).ready(function() {

  $(".item-qty").change(function() {
     //$(this).next(".btn-update").fadeIn();
     $(this).next(".btn-update").trigger('click');
  });



  var contactForm = $(".contact-form")
  var contactFormMethod = contactForm.attr("method")
  var contactFormEndpoint = contactForm.attr("action")

  function displaySubmitting(submitBtn, defaultText, doSubmit) {
    if (doSubmit) {
      submitBtn.addClass("disabled")
      submitBtn.html("<i class='fa fa-spin fa-spinner'></i> Sending...")
    }
    else {
      submitBtn.removeClass("disabled")
      submitBtn.html(defaultText)
    }
  }

  contactForm.submit(function(event) {
    event.preventDefault()
    var contactFormSubmitBtn = contactForm.find("[type='submit']")
    var contactFormSubmitTxt = contactFormSubmitBtn.text()
    var contactFormData = contactForm.serialize()
    var thisForm = $(this)
    displaySubmitting(contactFormSubmitBtn, "", true)
    $.ajax({
      method: contactFormMethod,
      url: contactFormEndpoint,
      data: contactFormData,
      success: function(data) {
        contactForm[0].reset()
        $.alert({
          title: "Success!",
          content: data.message,
          theme: "modern",
        })
        setTimeout(function(){
          displaySubmitting(contactFormSubmitBtn,contactFormSubmitTxt, false)
        }, 2000)
      },
      error: function(error) {
        console.log(error.responseJSON)
        var jsonData = error.responseJSON
        var msg = ""

        $.each(jsonData, function(key, value) {
          msg +=  key + ": " + value[0].message + "<br/>"
        })
        $.alert({
          title:"Errors",
          content: msg,
          theme: "modern",
        })
      }
    })


  })





  var searchForm = $(".search-form")
  var searchInput = searchForm.find("[name='q']") // input name = 'q'
  var typingTimer;
  var typingInterval = 500 // .5 seconds
  var searchBtn = searchForm.find("[type='submit']")
  searchInput.keyup(function(event) {
      clearTimeout(typingTimer)
      typingTimer = setTimeout(performSearch, typingInterval)
  })

  searchInput.keydown(function(event) {
      clearTimeout(typingTimer)
  })

  function displaySearching() {
    searchBtn.addClass("disabled")
    searchBtn.html("<i class='fa fa-spin fa-spinner'></i> Searching...")
  }

  function performSearch() {
    displaySearching()
    var query = searchInput.val()
    setTimeout(function() {
      window.location.href = '/search/?q=' + query
    }, 1000)
  }

  var productForm = $(".form-product-ajax")

  productForm.submit(function(event) {
    event.preventDefault()
    //console.log("QK: Form is not sending")
    var thisForm = $(this)
    var actionEndpoint = thisForm.attr("data-endpoint")
    var actionEndpoint = thisForm.attr("action")
    var httpMethod = thisForm.attr("method")
    var formData = thisForm.serialize();
    console.log("actionEndpoint");
    console.log(actionEndpoint);
    console.log("http method");
    console.log(httpMethod);
    console.log("formData");
    console.log(formData);
    $.ajax({
      url: actionEndpoint,
      method: httpMethod,
      data: formData,
      success: function(data) {
        console.log("success")
        //whole HTML PAGE
        console.log("data")
        console.log(data)
        //console.log("Removed", data.removed)
        var currentPath = window.location.href
        //if the page is not cart
        if (currentPath.indexOf("cart") == -1) {
            var submitSpan = thisForm.find(".submit-span")
            submitSpan.html("<style> "+
                "@media screen and (min-width: 0px) and (max-width: 700px) { "+
                ".view_desktop { margin-left: 50px;   } " + 
                ".add_to_cart { margin-right: 20px; } "+
                ".remove_from_cart { margin-right: 20px; } "+
                "} "+
                "@media screen and (min-width: 701px) and (max-width: 3000px) { " +
                ".add_to_cart { width: 150px; margin-right: 27px; margin-left: 20px; } "+
                ".remove_from_cart { margin-left: 20px; width: 130px; margin-right: 37px; } "+
                "} </style>");

            if (data.added) {
                submitSpan.html("<span class='submit-span' style='display:flex;'>" +
                                "<input type='hidden' name='product_id' value='" + data.product_id + "' />" + 
                                "<input type='hidden' name='remove_id' value='" + data.product_id + "' />" + 
                                "<button type='submit' class='btn btn-primary remove_from_cart'><i class='fa fa-trash-o'></i> Remove</button>" +
                                "<button type='submit' class='btn btn-primary add_to_wishlist'><i class='fa fa-heart'></i> Add to wishlist</button>" + 
                                "</span>");
            }
            else {
                submitSpan.html("<span class='submit-span' style='display:flex;'>" +
                                "<input type='hidden' name='product_id' value='" + data.product_id + "' />" + 
                                "<button type='submit' class='btn btn-primary add_to_cart'><i class='fa fa-shopping-cart'></i> Add to cart</button>" +
                                "<button type='submit' class='btn btn-primary add_to_wishlist'><i class='fa fa-heart'></i> Add to wishlist</button>" + 
                                "</span>");
            }
        }
        console.log("currentPath");
        console.log(currentPath);
        //if the page is not cart
        if (currentPath.indexOf("cart") != -1) {
          refreshCart()
        }
        //console.log("Count:",data.cartItemCount)
        var cartItemCount = $(".cart-item-count")
        cartItemCount.text(data.cartItemCount)
      },
      error: function(errorData) {
        console.log("error")
        console.log(errorData)
        $.alert({
            title: 'Error with Form Submission',
            content: errorData,
            theme: 'modern',
            type: 'green',
        });
      }
    })
  })

  function refreshCart() {
    console.log("in current cart")
    var cartTable = $(".cart-table")
    var cartBody = cartTable.find(".cart-body")
    var productRows = cartTable.find(".cart-product")
    //console.log(productRows.html())

    var currentUrl = window.location.href
    //var refreshCartUrl = '/cart/update'
    //var refreshCartUrl = '/cart'
    var refreshCartUrl = '/api/cart/'
    var refreshCartMethod = "POST"
    console.log("item-qty")
    var item_qty = $(".item-qty")
    console.log(item_qty.val());
    console.log("item-product-id")
    var item_prd = $(".item-product")
    console.log(item_prd.val());
    var data = {"item_qty": item_qty.val(), "item_prd": item_prd.val() }
    $.ajax({
      url: refreshCartUrl,
      method: refreshCartMethod,
      data: data,
      success: function(data){
        console.log("success | DATA");
        console.log(data);
        var hiddenCartItemRemoveForm = $(".cart-item-remove-form")
        //console.log("Length: ", data.products.length)
        //console.log("item-qty")
        //var item_qty = $(".item-qty")
        //console.log(item_qty.val());
        var hiddenCartItemRemoveForm = $(".cart-item-remove-form")
        window.location.href = currentUrl
        /*
        if (data.products.length > 0) {
          console.log("Hello Qaisar");
          productRows.html(" ")
          i = data.products.length
          $.each(data.products, function(index, value) {
              console.log("Product ID: " + value.id)
              console.log("Product Name: " + value.name)
              console.log("Product QTY: " + value.item_qty)
              var priceMinusDiscount = value.price - value.discount

              var newCartItemRemove = hiddenCartItemRemoveForm.clone()
              newCartItemRemove.find(".cart-item-product-id").val(value.id)
              newCartItemRemove.css("display", "block")
              cartBody.prepend("<tr class='cart-product'>"+
                                "<td><a href='"+value.image_link+"'><img src='"+value.image+"'></a>"+
                                "<td><a href='"+value.url+"'>"+value.id + "=" + value.name+"</a></td>"+
                                "<td><input type='number' class='item-product' name='qty_productid' value='" + value.id + "' class='form-control' style='display:none; '/>" +
                                     "<input type='number' class='item-qty' name='qty' value='" + value.item_qty + "' class='form-control' />"+
                                     "<input type='submit' class='btn-update btn btn-link' value='Update Item' style='display:none'/>" +
                                "</td>"+
                                "<td>"+value.price+"</td>"+
                                "<td>"+value.discount +"</td>"+
                                "<td>"+value.priceMinusDiscount +"</td>"+
                                "<td>"+newCartItemRemove.html()+"</td>"+
                                "</tr>");
              i--
          })
          cartTable.find(".cart-subtotal").text(data.subtotal);
          cartTable.find(".cart-total").text(data.total);
        }
        else {
          window.location.href = currentUrl
        }
        */

        //console.log("data.products.length");
        //console.log(data.products.length);
        /*if (data.products.length > 0) {
          console.log("data.sub_total");
          console.log(data.subtotal);
          productRows.html("<tr><td colspan=3>Coming Soon</td></tr>");
          cartTable.find(".cart-subtotal").text(data.subtotal);
          cartTable.find(".cart-total").text(data.total);
        }
        else {
          window.location.href = currentUrl
        }
        */
      },
      error: function(errorData) {
        console.log("error")
        console.log(errorData)
        //alert("Error with the update")
        $.alert({
            title: 'Error with Refreshing data',
            content: errorData,
            theme: 'modern',
            type: 'green',
        });
      }
    })
  }
})
