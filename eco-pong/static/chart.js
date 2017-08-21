var count =7;
var max = 100;
var min = 80;

// Creating a bar chart with no labels and a series array with one series. For the series we generate random data with `count` elements and random data ranging from 0 to `max`.
var chart = new Chartist.Bar('.chart', {
  labels: ['Penns Primary School', 'William Cowper Primary School', 'Warren Farm Primary School', 'Chad Vale Primary School', 'Slade Road Primary School', 'Oval Primary School', 'Twickenham Primary School'],
  series: [ [114.03, 121.18, 106.08, 95.88, 113.92, 87.74, 106.22] ]
}, {
  axisX: {
    showLabel: true
  },
  axisY: {
    onlyInteger: true
  }
});

// This is the bit we are actually interested in. By registering a callback for `draw` events, we can actually intercept the drawing process of each element on the chart.
chart.on('draw', function(context) {
  // First we want to make sure that only do something when the draw event is for bars. Draw events do get fired for labels and grids too.
  if(context.type === 'bar') {
    // With the Chartist.Svg API we can easily set an attribute on our bar that just got drawn
    context.element.	attr({
      // Now we set the style attribute on our bar to override the default color of the bar. By using a HSL colour we can easily set the hue of the colour dynamically while keeping the same saturation and lightness. From the context we can also get the current value of the bar. We use that value to calculate a hue between 0 and 100 degree. This will make our bars appear green when close to the maximum and red when close to zero.
      //style: 'stroke: hsl(' + Math.floor((Chartist.getMultiValue(context.value) / (max-min)) + min)  + ', 50%, 50%); stroke-width: 40px;'
    });
  }
});
