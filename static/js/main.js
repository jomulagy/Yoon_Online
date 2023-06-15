var cartItems = [];

$(document).ready(function(){
    $(".menuTap").click(function(){
        var name = $(this).children('.menuName').children('.menu_name').text()
        var price = $(this).children('.menuName').children('.menu_price').text()
        var item = {
          name: name,
          price: price,
          quantity : 1,
        };
        var index = cartItems.findIndex(element => element.name === name)
        if(index<0){
            cartItems.push(item);
        }
        else{
            cartItems[index].quantity++;
        }
        updateCart();

    });

    function updateCart() {
        var cartList = $('#mainRightContent');
        var totalPrice = 0;

        cartList.empty();

        $.each(cartItems, function(index, item) {
            var listItem = $("<li style = 'list-style-type: none;'>");
            var menuTab = $('<div>').addClass('selectedMenuTab');
            var menuName = $('<div>').addClass('selectedMenuName').text(item.name);
            var menuDetail = $('<div>').addClass('selectedMenuDetail');
            var priceWrap = $('<div>').addClass('selectedPriceWrap');
            var deleteBt = $('<div>').addClass('deleteBt').text('x');
            var menuPrice = $('<div>').addClass('selectedMenuPrice').text(item.price);
            var numWrapper = $('<div>').addClass('selectedNum');
            var minusBt = $('<div>').addClass('minusBt').text('-');
            var menuNumber = $('<div>').addClass('menuNumber').text(item.quantity).attr('id', 'menuNum');
            var plusBt = $('<div>').addClass('plusBt').text('+');

            priceWrap.append(deleteBt, menuPrice);
            numWrapper.append(minusBt, menuNumber, plusBt);
            menuDetail.append(priceWrap, numWrapper);
            menuTab.append(menuName, menuDetail);

            listItem.append(menuTab);
            cartList.append(listItem);
        });

        $('#total-price').text('$' + totalPrice.toFixed(2));
      }

      $(document).on('click', '.minusBt', function() {
          var curMenu = $(this).parent().parent().parent()
          var name = $(curMenu).children(".selectedMenuName").text()
          var index = cartItems.findIndex(element => element.name === name)
          var item = cartItems[index]

          //1빼기
          item.quantity -= 1;

          //0이되면
          if (item.quantity === 0){
            //리스트에서삭제
            cartItems.splice(index,1);

            //화면에서 삭제
            $(curMenu).remove();

          }

          //아니면
          else{
            $(this).parent().children(".menuNumber").text(item.quantity);
          }

      });

      $(document).on('click', '.plusBt', function() {
          var curMenu = $(this).parent().parent().parent()
          var name = $(curMenu).children(".selectedMenuName").text()
          var index = cartItems.findIndex(element => element.name === name)
          var item = cartItems[index]

          //1더하기
          item.quantity += 1;
          //화면에 적용하기
          $(this).parent().children(".menuNumber").text(item.quantity);

      });

      $(document).on('click', '.deleteBt', function() {
          var index = cartItems.findIndex(element => element.name === name)
          var item = cartItems[index]

          $(this).parent().parent().parent().remove();
          cartItems.splice(index,1);
      });
})
$(function(){
    $('.menuKind').click(function(){
        $(this).siblings('.menuTapWrap').slideUp();
        $(this).next().stop().slideToggle(300);
        $(this).toggleClass('active');
        $(this).siblings().removeClass('active');
    })
})

function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    var cookies = document.cookie.split(';');
    for (var i = 0; i < cookies.length; i++) {
      var cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}
$(".orderBtWrap").click(function(){
    var csrftoken = getCookie('csrftoken');
    $.ajax({
      url: '/food/order/create/',
      type: 'POST',
      headers: {
          'X-CSRFToken': csrftoken
      },
      data: JSON.stringify(cartItems),
      success: function(response) {
        if(response.success){
            alert("주문이 접수되었습니다.")
            location.href = "/food/order/detail/"+response.id;
        }
      },
      error: function(xhr, status, error) {
        if (xhr.status === 400){
            alert("로그인 후 이용해주세요.")
            location.href = "/account/login/"
        }
      }
    });
})

$(".menuTap").click(function(){
    var name = $(this).children('.menuName').children('.menu_name').text()
    var price = $(this).children('.menuName').children('.menu_price').text()
    var cur = $("#mainRightContent").append("<div class='selectedMenuTab'></div>")
    console.log
    cur = cur.append("<div class='selectedMenuName'>야채김밥</div>")
})


