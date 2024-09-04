function add_to_cart(id) {
    var ajaxurl = "/add_to_cart/";
    $.ajax({
        headers: { "X-CSRF-TOKEN": $('meta[name="csrf-token"]').attr("content") },
        url: ajaxurl,
        data: { id: id },
        method: "post",
        success: function(response) {
            var cartCount = document.getElementById('cart-count');
            console.log(cartCount);  // This will log null if the element isn't found
            if (cartCount) {
                cartCount.innerHTML = response.count;
                Swal.fire({
                    position: "center",
                    icon: "success",
                    title: "Added to cart successfully",
                    showConfirmButton: false,
                    timer: 1500
                });
            } else {
                console.error("Cart count element not found.");
            }
        }
    });
}
