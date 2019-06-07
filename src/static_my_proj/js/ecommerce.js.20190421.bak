$(document).ready(function() {

  $(".item-qty").change(function() {
     $(this).next(".btn-update").fadeIn();
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
    console.log("QK: Form is not sending")
    var thisForm = $(this)
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
        console.log(data)
        console.log("Added", data.added)
        console.log("Removed", data.removed)
        var currentPath = window.location.href
        if (currentPath.indexOf("cart") == -1) {
            var submitSpan = thisForm.find(".submit-span")
            if (data.added) {
                submitSpan.html("<button type='submit' class='btn btn-danger'><i class='fa fa-shopping-cart'></i>Remove</button>");
            }
            else {
                submitSpan.html("<button type='submit' class='btn btn-primary'><i class='fa fa-shopping-cart'></i>Add to Cart</button>");
            }
        }
        console.log("currentPath");
        console.log(currentPath);
        if (currentPath.indexOf("cart") != -1) {
          refreshCart()
        }
        console.log("Count:",data.cartItemCount)
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
    //cartBody.html("<h1>Changed</h1>");

    var productRows = cartTable.find(".cart-product")
    console.log(productRows.html)

    var currentUrl = window.location.href
    var refreshCartUrl = '/api/cart/'
    var refreshCartMethod = "GET"
    var data = {}
    $.ajax({
      url: refreshCartUrl,
      method: refreshCartMethod,
      data: data,
      success: function(data){
        console.log("success")
        console.log(data)
        var hiddenCartItemRemoveForm = $(".cart-item-remove-form")
        //console.log("Length: ", data.products.length)
        if (data.products.length > 0) {
          productRows.html(" ")
          //cartBody.prepend("<tr><td colspan=3>Coming Soon</td></tr>")
          i = data.products.length
          $.each(data.products, function(index, value) {
              console.log(value)
              var newCartItemRemove = hiddenCartItemRemoveForm.clone()
              newCartItemRemove.find(".cart-item-product-id").val(value.id)
              newCartItemRemove.css("display", "block")
              cartBody.prepend("<tr class='cart-product'>"+
                                "<td><a href='"+value.image_link+"'><img src='"+value.image+"'></a>"+
                                "<td><a href='"+value.url+"'>"+value.name+"</a></td>"+
                                "<td>2</td>"+
                                "<td>"+value.price+"</td>"+
                                "<td>$0.00</td>"+
                                "<td>$246.00</td>"+
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

        console.log("data.products.length");
        console.log(data.products.length);
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
        alert("Error with the update")
        /*$.alert({
            title: 'Error with Refreshing data',
            content: errorData,
            theme: 'modern',
            type: 'green',
        });
        */
      }
    })
  }
})
