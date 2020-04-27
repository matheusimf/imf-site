$(function() {

  var setVideoHeight = function() {
    console.log('entrei')
    proportion = 0.5625

    videoWidth = $('iframe').width()
    console.log('largura')

    videoHeight = Math.round( proportion * videoWidth )

    $('iframe').height( videoHeight )
    console.log(videoHeight)

  };

  $( window ).on( "orientationchange", function( event ) {
    setVideoHeight();
  });

  setVideoHeight();

});
