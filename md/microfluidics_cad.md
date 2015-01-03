# CAD for microfluidics

I have been working on methods for representing a library of microfluidics parts in various open-source CAD tools. The idea is that eventually I'll put together some sort of drag-n-drop interface for scientists that don't want to deal with CAD, but understand what their protocol might require from a fluidic system.  
For now I've only implemented some things using [implicitCAD]() and [verbnurbs](https://github.com/pboyer/verb).  

# Parabolic NURBS channel 



<script src="../md/microfluidic-cad/js/numeric-1.2.6.min.js"></script>
<script src="../md/microfluidic-cad/js/binomial.js"></script>
<script src="../md/microfluidic-cad/js/verb.js"></script>
<script src="../md/microfluidic-cad/js/conversions.js"></script>

<script src="../md/microfluidic-cad/js/lightgl.js"></script>
<script src="../md/microfluidic-cad/js/viewer.js"></script>

<link href='http://fonts.googleapis.com/css?family=Open+Sans' rel='stylesheet' type='text/css' />
<link rel="stylesheet" href="../md/microfluidic-cad/css/microfluidic-style.css" />


<div id="container">
  <b>Parabolic Channel</b><pre>USAGE: click and drag to pan around, zoom with middle-mouse button, and CTRL+click to move around.</pre>
  <div id="0" class="viewer"></div>
  <script>
    function parabolic_channel(length, width, depth){
      var half_width = width/2;
      var half_length = length/2;
      var degree = 2
        , knots = [0, 0, 0, 1, 1, 1]
        , pts = [   [ [-half_width, -half_length, 0], [0, -half_length, depth], [half_width, -half_length, 0] ],
              [ [-half_width, 0           , 0], [0, 0           , depth], [half_width, 0           , 0] ],
              [ [-half_width, half_length , 0], [0, half_length , depth], [half_width, half_length , 0] ]
            ]
              
        , wts = [   [ 1, 1, 1],
              [ 1, 1, 1],
              [ 1, 1, 1]
            ];

      srf1 = new verb.NurbsSurface( degree, knots, degree, knots, pts, wts );

      return srf1;
    }

    verb.init();
    var geom = [];
    var srf1, srf2;

    geom.push(parabolic_channel(length=100, width=10, depth=-20));

    geom.map(function(g){
      addViewer(new Viewer( g, 1200, 600, -2 ) );
    });
  </script>  
</div>
