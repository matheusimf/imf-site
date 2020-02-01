$(function() {

  var setBackgroundSize = function () {

    imgProportion = 1.67

    backgroundWidth = window.screen.width

    $('body').css("background-size", backgroundWidth + "px " + backgroundWidth/imgProportion + "px");
  };

  setBackgroundSize();

});
