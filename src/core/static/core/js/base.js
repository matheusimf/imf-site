$(function() {

  var setHomeContentHeight = function() {
    /* For this to work we needed to comment the function
    handleHomeContentHeight() on core/assets/js/apps.min.js*/

    //Get the image width
    mainImageWidth = window.screen.width

    // Find the image proportion  height x width
    imageProportion = 1363/2364

    // Calculate image height
    mainImageHeight = Math.round( imageProportion * mainImageWidth);

    // Get the padding-top for the image to keep it's dimensions
    imagePadding = $('.main-image').css('padding-top')
    paddingToAdd = parseInt(imagePadding);

    // Giving the home page the proper height
    $('#home').height( mainImageHeight + paddingToAdd );
  };

  $( window ).on( "orientationchange", function( event ) {
    setHomeContentHeight()
  });


  setHomeContentHeight();

});
